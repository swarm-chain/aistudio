
# 🚧 Swarm AI Studio Installation Guide

*This project is currently under active development. You might encounter some issues during setup or usage. We appreciate your understanding and welcome any feedback to improve the experience.*

![Swarm AI Studio Logo](https://swarm-agent-website.vercel.app/logo.png)

---

## Important Note

This solution provides an open-source platform for building AI applications. If you require an on-premise solution, customization, or a secure app without third-party APIs, please contact us at **info@swarmchain.org**. We can assist you with setup and provide tailored solutions to meet your needs.

---

Welcome to the **Swarm AI Studio** installation guide! This document will guide you through setting up the backend server, SIP server, and the user interface (UI). The **Swarm AI Studio** leverages powerful technologies like **Groq**, **LlamaIndex**, and **LiveKit** for real-time communication and data management.

The code repository for **Swarm AI Studio** is available on GitHub: [swarm-chain/aistudio](https://github.com/swarm-chain/aistudio.git).

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Set Up Swarm AI Studio Backend](#step-1-set-up-swarm-ai-studio-backend)
3. [Step 2: LiveKit On-Premise Installation](#step-2-livekit-on-premise-installation)
4. [Step 3: SIP Server On-Premise Installation](#step-3-sip-server-on-premise-installation)
5. [Step 4: Set Up the User Interface (UI)](#step-4-set-up-the-user-interface-ui)
6. [Step 5: Run Swarm AI Studio and UI](#step-5-run-swarm-ai-studio-and-ui)
7. [Roadmap](#roadmap)
8. [Credits](#credits)
9. [Support](#support)

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8+**
- **MongoDB** (or access to a MongoDB instance)
- **Node.js and npm** (for the UI)
- **Git**

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

- **Swarm AI Studio Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Swarm Voice Agent UI:** [http://localhost:3000](http://localhost:3000)
- **Swarm Bot UI:** Accessible through the Swarm Voice Agent interface.

---

## Roadmap

The **Swarm AI Studio** team is focused on continuous improvement to enhance functionality, usability, and performance. Here are some upcoming initiatives:

1. **UI Improvements**
   - Enhance

 the UI for a more intuitive and streamlined user experience.
   - Update the Swarm Bot and Voice Agent interfaces for improved interactivity and responsiveness.
   - Introduce customizable themes to allow users to personalize the interface.

2. **Backend Optimization**
   - Optimize backend code for faster processing and response times.
   - Improve data handling and resource management to support larger workloads efficiently.
   - Implement modular, microservices-based architecture for better scalability and performance.

3. **Code Enhancements**
   - Regular code refactoring to improve maintainability and readability.
   - Enhanced error handling and logging for smoother troubleshooting and debugging.
   - Improve security protocols for managing API keys and sensitive data.

4. **Video Agent Support**
   - Integrate a **Video Agent** feature that allows real-time video interactions, supporting both voice and visual communication.
   - Implement screen sharing and recording functionalities for video calls, enhancing collaboration and support.

5. **Auto Call Disconnect Feature**
   - Add an **Auto Call Disconnect** feature to terminate inactive or timed-out calls automatically, freeing resources and improving user experience.
   - Customizable inactivity timeout settings to allow for flexibility in call handling.

6. **Freshdesk and CRM Integrations**
   - Integrate with **Freshdesk** and other popular CRM platforms to streamline customer support workflows.
   - Provide seamless data syncing between Swarm AI Studio and CRM systems to manage customer information, track interactions, and automate support processes.

7. **Improved Bot Training and Management**
   - Add an **Interactive Bot Training** interface for easier model training and tuning.
   - Enable multi-language support for the bot, expanding its usability to a global audience.
   - Provide detailed analytics on bot interactions to improve bot training and performance tracking.

8. **Advanced Analytics and Insights**
   - Develop an **Analytics Dashboard** for tracking metrics such as call duration, response times, user engagement, and conversion rates.
   - Real-time insights for monitoring platform usage and making data-driven optimizations.

9. **Multi-Channel Communication Support**
   - Expand support for **SMS** and **Email** communication alongside voice and video, allowing agents to reach users through preferred channels.
   - Unified inbox for tracking all communication channels, making it easier for agents to manage user interactions.

10. **Automated Transcriptions and Summaries**
    - Implement automated transcription and call summaries for voice and video interactions, facilitating easy review and follow-up.
    - Option for text-based sentiment analysis on transcripts to understand user sentiment in real-time.

11. **Auto-Scheduling and Callback Features**
    - Add an **Auto-Scheduling** feature to allow users to book calls or callbacks based on availability.
    - Callback management system for prioritizing follow-ups and missed calls.

12. **Integration with Knowledge Bases**
    - Integrate with popular knowledge bases to allow the AI to pull answers and solutions from existing content.
    - Auto-suggest answers during calls, leveraging both internal and external resources to enhance support quality.

---

## Credits

Swarm AI Studio integrates several powerful technologies:

- **Groq**: For high-performance computing.
- **LlamaIndex**: As a versatile data management tool.
- **LiveKit**: For real-time communication capabilities.

---

## Support

For inquiries or support, please contact us at **info@swarmchain.org**.

---

Thank you for trying out **Swarm AI Studio**! Your feedback is invaluable in helping us improve the platform.