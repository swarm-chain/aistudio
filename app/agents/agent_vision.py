import os
import asyncio
import numpy as np
from dotenv import load_dotenv
from PIL import Image
from livekit import rtc
from livekit.agents import JobContext, JobRequest, WorkerOptions, cli,JobProcess,llm
from livekit.agents.llm import (
    ChatContext,
    ChatMessage,
    ChatImage
)
from livekit.agents.voice_assistant import AssistantCallContext, VoiceAssistant
from livekit.plugins import deepgram, openai, silero


# Load environment variables
load_dotenv()

def prewarm_fnc(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load() 
# Set up environment variable reloading and printing
def reload_env_variables():
    livekit_url = os.environ.get('LIVEKIT_URL')
    livekit_api_key = os.environ.get('LIVEKIT_API_KEY')
    livekit_api_secret = os.environ.get('LIVEKIT_API_SECRET')
    eleven_api_key = os.environ.get('ELEVEN_API_KEY')
    deepgram_api_key = os.environ.get('DEEPGRAM_API_KEY')
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    speech_region = os.environ.get('AZURE_SPEECH_REGION')
    speech_key = os.environ.get('AZURE_SPEECH_KEY')
    
    return {
        'livekit_url': livekit_url,
        'livekit_api_key': livekit_api_key,
        'livekit_api_secret': livekit_api_secret,
        'eleven_api_key': eleven_api_key,
        'deepgram_api_key': deepgram_api_key,
        'openai_api_key': openai_api_key,
        'speech_region': speech_region,
        'speech_key': speech_key
    }

async def _will_synthesize_assistant_reply(assistant: VoiceAssistant, chat_ctx: llm.ChatContext, latest_image: Image.Image):
    system_msg = chat_ctx.messages[0].copy()  # copy system message
    user_msg = chat_ctx.messages[-1]  # last message from user

    # Add the latest image to the context
    if latest_image:
        chat_ctx.messages.append(ChatMessage(role="user", content=[ChatImage(image=latest_image)]))

    return assistant.llm.chat(chat_ctx=chat_ctx)

env_vars = reload_env_variables()
# Merging the video track capture and publishing logic
async def get_video_track(room: rtc.Room):
    """Get the first video track from the room. We'll use this track to process images."""

    video_track = asyncio.Future[rtc.RemoteVideoTrack]()

    for _, participant in room.remote_participants.items():
        for _, track_publication in participant.track_publications.items():
            if track_publication.track is not None and isinstance(
                track_publication.track, rtc.RemoteVideoTrack
            ):
                video_track.set_result(track_publication.track)
                print(f"Using video track {track_publication.track.sid}")
                break

    return await video_track

async def entrypoint(ctx: JobContext):
    # Ensure prewarm_fnc was executed, and userdata contains the vad key
    if "vad" not in ctx.proc.userdata:
        raise KeyError("VAD not found in process userdata. Ensure prewarm_fnc is being called.")

    await ctx.connect()

    while ctx.room.connection_state != rtc.ConnectionState.CONN_CONNECTED:
        await asyncio.sleep(0.1)

    chat = rtc.ChatManager(ctx.room)
    chat_context = ChatContext(messages=[
        ChatMessage(
                    role="system", 
                    content="""
                      When interacting with users, follow these guidelines:
                1. Always introduce yourself as arjun.
                2. Maintain a consistently happy and positive demeanor in your responses.
                3. Acknowledge and utilize your vision and voice capabilities when appropriate. For example, if a user asks about an image, assume you can see it and respond accordingly.
                4. Provide clear and concise answers, avoiding unnecessary jargon.
                5. Do not use emojis in your responses.
                6. you can see user so if user ask example: can you see me or how i am looking etc respond properly

                When formulating your responses, follow this process:
                1. Analyze the user's input, considering both text and potential visual elements.
                2. If the input involves an image, describe what you see briefly before addressing the user's question or request.
                3. Craft your response in a way that demonstrates your happy personality while remaining helpful and informative."""
                    )
    ])

    gpt = openai.LLM(model="gpt-4o-mini")
    latest_image = None
    assistant = VoiceAssistant(
        vad=ctx.proc.userdata["vad"],  # Now we are sure the vad model is loaded
        stt=deepgram.STT(),
        llm=gpt,
        tts=openai.TTS(model="tts-1-hd"),
        chat_ctx=chat_context,
        will_synthesize_assistant_reply=lambda assistant, chat_ctx: _will_synthesize_assistant_reply(assistant, chat_ctx, latest_image)
    )


    assistant.start(ctx.room)
    await asyncio.sleep(3)
    await assistant.say("Hey, how can I help you today?", allow_interruptions=True)

    while ctx.room.connection_state == rtc.ConnectionState.CONN_CONNECTED:
        video_track = await get_video_track(ctx.room)
        async for event in rtc.VideoStream(video_track):
            latest_image = event.frame


async def request_fnc(req: JobRequest):
    await req.accept(entrypoint)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm_fnc))

