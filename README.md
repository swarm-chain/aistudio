
# 🚧 Swarm AI Studio Installation Guide

*This project is currently under active development. You might encounter some issues during setup or usage. We appreciate your understanding and welcome any feedback to improve the experience.*

![Swarm AI Studio Introduction](docs/intro.gif)

---

## Important Note

**Swarm AI Studio** is an AI agent application designed to handle real-time interactions through phone calls, web-based voice user interfaces (VUI), and SIP capabilities. This open-source platform allows you to create advanced AI-driven communication systems. If you need an on-premise solution, customization, or a secure app setup without third-party APIs, please contact us at **info@swarmchain.org**. We are available to assist with setup and provide tailored solutions to meet your requirements.

---

Welcome to the **Swarm AI Studio** installation guide! This document will guide you through setting up the backend server, SIP server, and the user interface (UI). The **Swarm AI Studio** leverages powerful technologies like **Groq**, a highly optimized LLM processing system, and **LlamaIndex** for retrieval-augmented generation (RAG) to provide real-time communication and data management.

The code repository for **Swarm AI Studio** is available on GitHub: [swarm-chain/aistudio](https://github.com/swarm-chain/aistudio.git).

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Set Up Swarm AI Studio Backend](#step-1-set-up-swarm-ai-studio-backend)
3. [Step 2: LiveKit On-Premise Installation](#step-2-livekit-on-premise-installation)
4. [Step 3: SIP Server On-Premise Installation](#step-3-sip-server-on-premise-installation)
5. [Step 4: Set Up the User Interface (UI)](#step-4-set-up-the-user-interface-ui)
6. [Step 5: Run Swarm AI Studio and UI](#step-5-run-swarm-ai-studio-and-ui)
7. [Step 6: Start Services in `tmux` Sessions](#step-6-start-services-in-tmux-sessions)
8. [Credits](#credits)
9. [Support](#support)

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8+**
- **MongoDB** (or access to a MongoDB instance)
- **Node.js and npm** (for the UI)
- **Git**
- **tmux** (for managing multiple terminal sessions)

---

## Step 1: Set Up Swarm AI Studio Backend

### 1.1 Clone the Repository

```bash
git clone https://github.com/swarm-chain/aistudio.git
cd aistudio
```

### 1.2 Create a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux and macOS
# For Windows:
# venv\Scripts\activate
```

### 1.3 Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 1.4 Configure Environment Variables

Create a `.env` file in the `app/env/` directory:

```bash
mkdir -p app/env
touch app/env/.env
```

Add the following content to `app/env/.env`:

```ini
# MongoDB settings
MONGO_USER=your_mongo_user
MONGO_PASSWORD=your_mongo_password
MONGO_HOST=your_mongo_host

# API Keys
OPENAI_API_KEY=your_openai_api_key
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
DEEPGRAM_API_KEY=your_deepgram_api_key

# LiveKit URL
LIVEKIT_URL=ws://localhost:7880
```

**Note:** Replace placeholders (e.g., `your_mongo_user`, `your_openai_api_key`) with actual credentials.

### 1.5 Install the Swarm AI Studio Package

```bash
pip install -e .
```

---

## Step 2: LiveKit and SIP Server On-Premise Installation

For setting up the LiveKit server and enabling SIP voice communication features, refer to the guides below. These guides will walk you through downloading, configuring, and running LiveKit and the SIP server for real-time communication:

- **[LiveKit On-Premise Installation Guide](https://github.com/swarm-chain/aistudio/blob/main/docs/livkit_server_setup.md)**
- **[SIP Server On-Premise Installation Guide](https://github.com/swarm-chain/aistudio/blob/main/docs/livkit_sip_server_setup.md)**

---

## Step 4: Set Up the User Interface (UI)

This section will guide you in setting up the Swarm Voice Agent and Swarm Bot projects. These two UI components are interlinked and must be configured correctly.

### 4.1 Clone the Repositories

Clone both repositories to your local machine:

```bash
# Clone Swarm Voice Agent repository
git clone https://github.com/swarm-chain/aistudio_ui.git
cd aistudio_ui  # Swarm Voice Agent directory

# Clone Swarm VUI (Swarm Bot) repository
git clone https://github.com/swarm-chain/aistudio_vui_widget.git
cd aistudio_vui_widget  # Swarm Bot directory
```

### 4.2 Install Dependencies

Install the dependencies for both projects separately.

**Swarm Voice Agent:**

```bash
cd aistudio_ui
npm install
# or
yarn install
# or
pnpm install
```

**Swarm Bot:**

```bash
cd aistudio_vui_widget
npm install
# or
yarn install
# or
pnpm install
```

### 4.3 Environment Configuration

Both projects require environment variables for configuration. Set up the environment variables for each project before running them.

#### Swarm Voice Agent Environment Variables

Create a `.env` file in the `aistudio_ui` directory and add the following variables:

```ini
MONGODB_URI=your_mongodb_uri
NEXTAUTH_SECRET=your_nextauth_secret

LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
NEXT_PUBLIC_LIVEKIT_URL=ws://localhost:7880

GMAIL_ID=your_gmail_id
GMAIL_PASS=your_gmail_password

NEXT_PUBLIC_ML_BACKEND_URL=http://localhost:8000
ALLOWED_BOT_ORIGINS=[]
NEXT_PUBLIC_BOT_LIVE_URL=http://localhost:5000  # Adjust the port if necessary
```

**Note:** Refer to the `.env.example` file in the repository for details on each variable.

#### Swarm Bot Environment Variables

Create a `.env` file in the `aistudio_vui_widget` directory and add the following variables:

```ini
VITE_API_LIVEKIT_URL=ws://localhost:7880
VITE_API_NEXT_backend=http://localhost:3000  # Swarm Voice Agent backend URL
VITE_API_ML_Backend=http://localhost:8000  # Swarm AI Studio backend URL
```

**Note:** Check the `.env.example` file in the repository for more details.

### 4.4 Running the Development Servers

#### 4.4.1 Start the Swarm Voice Agent Development Server

Navigate to the `aistudio_ui` directory and run:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to access the Swarm Voice Agent.

#### 4.4.2 Start the Swarm Bot Development Server

Navigate to the `aistudio_vui_widget` directory and run:

```bash
npm run build
# or
yarn build
# or
pnpm build

# Install serve globally if not already installed
npm install -g serve
# or
yarn global add serve
# or
pnpm add -g serve

# Serve the build
serve -s dist
```

Now, Swarm Bot will be accessible and can be integrated with the Swarm Voice Agent.

### 4.5 Project Integration

Both projects are interdependent and must be configured correctly to interact:

- **Swarm Voice Agent** relies on **Swarm Bot** for bot communication capabilities. Ensure that `NEXT_PUBLIC_BOT_LIVE_URL` in Swarm Voice Agent's `.env` file points to the correct URL of the Swarm Bot (e.g., `http://localhost:5000`).
- **Swarm Bot** needs to communicate with the Swarm Voice Agent backend. Ensure that the `VITE_API_NEXT_backend` environment variable is correctly set to point to the Swarm Voice Agent’s backend URL (`http://localhost:3000`).

---

## Step 5: Run Swarm AI Studio and UI

### 5.1 Start Swarm AI Studio Backend

In one terminal window, activate your virtual environment and run:

```bash
aistudio start api
```

### 5.2 Start the Agent

In another terminal window, activate your virtual environment and run:

```bash
aistudio start agent
```

### 5.3 Access the Application

- **Swarm AI Studio Backend API Docs:** [http://localhost:8000/docs](

http://localhost:8000/docs)
- **Swarm Voice Agent UI:** [http://localhost:3000](http://localhost:3000)
- **Swarm Bot UI:** Accessible through the Swarm Voice Agent interface.

---

## Step 6: Start Services in `tmux` Sessions

For continuous logging and management, we’ll start the following scripts in separate `tmux` sessions:

1. **Chat Log Creation Service**
2. **SIP Log Creation Service**
3. **Swarm AI Studio App**

To do this, follow the instructions below.

### 6.1 Open a `tmux` Session for Chat Log Creation

Start `chat_log_creation.py` in a new `tmux` session:

```bash
tmux new-session -d -s chat_log "python /app/log_service/chat_log_creation.py"
```

This will create a detached `tmux` session named `chat_log` running `chat_log_creation.py`. You can attach to this session using:

```bash
tmux attach -t chat_log
```

### 6.2 Open a `tmux` Session for SIP Log Creation

Start `sip_log_creation.py` in a new `tmux` session:

```bash
tmux new-session -d -s sip_log "python /Users/kesavan/aistudio/app/log_service/sip_log_creation.py"
```

This will create a detached `tmux` session named `sip_log` running `sip_log_creation.py`. You can attach to this session using:

```bash
tmux attach -t sip_log
```

### 6.3 Open a `tmux` Session for Swarm AI Studio

To start the main `aistudio` app in a `tmux` session:

```bash
tmux new-session -d -s aistudio "aistudio start"
```

This will create a detached `tmux` session named `aistudio`. You can attach to this session using:

```bash
tmux attach -t aistudio
```

To view or manage any of these sessions, list them using:

```bash
tmux list-sessions
```

---

## Credits

Swarm AI Studio integrates several powerful technologies:

- **Groq**: The fastest large language model (LLM) processing system, offering unparalleled speed for AI model deployment.
- **LlamaIndex**: Optimized for retrieval-augmented generation (RAG), LlamaIndex enhances the application’s ability to access and generate relevant, contextually informed responses.
- **LiveKit**: For real-time communication capabilities.

---

## Support

For inquiries or support, please contact us at **info@swarmchain.org**.

---

Thank you for trying out **Swarm AI Studio**! Your feedback is invaluable in helping us improve the platform.