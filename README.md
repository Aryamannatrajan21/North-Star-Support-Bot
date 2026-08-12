# North Star Support Bot

This repository contains a simple, highly-testable command-line chatbot built with Python and OpenAI. 
It exactly fulfills the requirements for the Upwork Talent Accelerator AI Chatbot Contract.

## 🎥 Video Demo
👉 [**Click here to watch the Video Demo on GitHub!**](https://github.com/Aryamannatrajan21/North-Star-Support-Bot/blob/main/AI%20CHatbot%20Video.mp4)

## 🚀 How to Run Locally (For you)

1. **Install Dependencies:**
   ```bash
   pip install openai python-dotenv
   ```
2. **Set up API Key:**
   - Copy `.env.example` to `.env`
   - Add your Nvidia API key to the `.env` file.
3. **Run the Bot:**
   ```bash
   python chatbot.py
   ```

> [!NOTE]
> **API Latency Notice:** This chatbot utilizes Nvidia's massive `nemotron-3-ultra-550b-a55b` model via their free public API tier. Because this model contains 550 Billion parameters and utilizes deep internal "chain-of-thought" reasoning, you may occasionally experience latency spikes (up to 30-60 seconds) during peak hours before the model begins streaming its response. This is due to server-side congestion on Nvidia's free tier, not a bug in the code!
