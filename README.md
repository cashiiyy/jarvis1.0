# Jarvis: AI Assistant 🤖

![Livekit](https://img.shields.io/badge/Livekit-agents?style=flat-square&logo=livekit&logoColor=white&labelColor=black&color=black)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-886FBF?logo=googlegemini&logoColor=fff)](#)
![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=visualstudiocode&logoColor=white)

Jarvis is a real-time, voice-capable AI assistant built using Python and LiveKit. Designed for seamless, low-latency conversational interactions, Jarvis leverages external tools to interact with the world, fetch real-time data, and automate tasks.

## 🚀 Features

- **Real-Time Voice Interface**: Powered by LiveKit for ultra-low latency audio streaming and conversational AI.
- **Extensible Tool Integration**: Equipped with function calling capabilities to execute Python scripts on demand.
- **Built-in Tools**:
  - 🌐 **Web Search**: Searches the live internet to answer queries with up-to-date information.
  - ☀️ **Get Weather**: Fetches current weather conditions and forecasts for any location.
  - 📧 **Send Email**: Drafts and sends emails automatically via automated scripts.

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Streaming Framework**: [LiveKit Agents SDK](https://github.com)
- **AI Ecosystem**: Google Gemini (via LiveKit Google plugin)

## 📋 Prerequisites

Before running Jarvis, ensure you have the following:
- A [LiveKit Cloud](https://livekit.io) account or a self-hosted LiveKit server.
- A Gemini API Key from Google AI Studio.
- API credentials for the integrated tools (e.g., Weather API, Email SMTP/OAuth, Search API).

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd jarvis-assistant
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   LIVEKIT_URL=your-livekit-url
   LIVEKIT_API_KEY=your-api-key
   LIVEKIT_API_SECRET=your-api-secret
   GEMINI_API_KEY=your-gemini-key
   
   # Tool Credentials
   WEATHER_API_KEY=your-weather-key
   SEARCH_API_KEY=your-search-key
   SMTP_EMAIL=your-email@example.com
   SMTP_PASSWORD=your-app-password
   ```

## 🏃 Running Jarvis

Start the LiveKit agent locally:
```bash
python agent.py dev
```

Once the agent is running, connect to it via your LiveKit playground or frontend application to start speaking with Jarvis.
