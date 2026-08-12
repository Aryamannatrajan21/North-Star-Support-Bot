# North Star Support Bot

This repository contains a simple, highly-testable command-line chatbot built with Python and OpenAI. 
It exactly fulfills the requirements for the Upwork Talent Accelerator AI Chatbot Contract.

## 🎥 Video Demo
<video src="https://github.com/Aryamannatrajan21/North-Star-Support-Bot/raw/main/AI%20CHatbot%20Video.mp4" width="800" controls></video>

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

## 🎥 Recording the Video Demo
Use QuickTime or Loom to record your screen for 2-3 minutes. 
Run the `python chatbot.py` command and demonstrate the 4 flows EXACTLY as outlined:
1. **Order Tracking**: Type "where is my order", then when prompted, enter `#111`.
2. **Returns**: Type "What is your return policy?"
3. **Recommendations**: Type "Can you recommend some gear?". Answer the clarifying question, then receive the recommendation.
4. **Human Handoff (Fallback)**: Type gibberish (e.g. "asdfghjkl") or explicitly ask "I want to speak to a human". Ensure you type `menu` to return after the handoff.


