import os
import sys

try:
    from openai import OpenAI
except ImportError:
    print("Please install required packages: pip install openai")
    sys.exit(1)

# API Key (Hardcoded for Upwork Evaluator, but hidden on GitHub)
API_KEY = "YOUR_NVIDIA_API_KEY_HERE"

client = OpenAI(api_key=API_KEY, base_url="https://integrate.api.nvidia.com/v1")

# Load Master Prompt
try:
    with open("master_prompt.md", "r") as f:
        SYSTEM_PROMPT = f.read()
except FileNotFoundError:
    print("[ERROR] master_prompt.md not found. Please ensure it is in the same directory.")
    sys.exit(1)

def print_bot(msg, end="\n"):
    # Print bot message in Green
    print(f"\033[92m{msg}\033[0m", end=end, flush=True)

def print_reasoning(msg, end=""):
    # Print reasoning in dim purple/magenta
    print(f"\033[95m{msg}\033[0m", end=end, flush=True)

def print_system(msg):
    # Print system messages in Yellow
    print(f"\n\033[93m{msg}\033[0m")

def main():
    print_system("=== Starting North Star Support Bot ===")
    print_system("Type 'quit' or 'exit' to close the chat.")
    print_system("=======================================")
    
    # Initialize conversation history with the Master Prompt
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    # Initial greeting
    greeting = "Hello! I'm the North Star Support Bot. How can I help you with your outdoor gear today?"
    messages.append({"role": "assistant", "content": greeting})
    print("\n\033[92mNorth Star Bot: \033[0m", end="")
    print_bot(greeting)

    while True:
        # Get user input
        user_input = input("\n\033[94mYou:\033[0m ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print_system("Exiting chatbot. Happy trails!")
            break
            
        if not user_input:
            continue

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        try:
            # Call Nvidia API with Nemotron-3-Ultra and reasoning enabled
            print("\n\033[95m[Thinking...]\033[0m", end="", flush=True)
            completion = client.chat.completions.create(
                model="meta/llama-3.1-8b-instruct",
                messages=messages,
                temperature=0.2, # Keep low for strict rule adherence
                top_p=0.95,
                max_tokens=1024,
                stream=True
            )
            
            bot_reply = ""
            first_content = True
            chunk_count = 0
            
            for chunk in completion:
                if not chunk.choices:
                    continue
                
                chunk_count += 1
                
                # Check for reasoning to animate the [Thinking...] indicator (Legacy from Nemotron, keeping for UX)
                reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
                if reasoning and chunk_count % 10 == 0:
                    print("\033[95m.\033[0m", end="", flush=True)
                
                # Check for actual content (we ignore printing the reasoning_content now)
                if chunk.choices[0].delta.content is not None:
                    if first_content:
                        # Erase the [Thinking...] line and print the bot prefix
                        print("\r\033[K\033[92mNorth Star Bot: \033[0m", end="")
                        first_content = False
                        
                    content = chunk.choices[0].delta.content
                    bot_reply += content
                    print_bot(content, end="")
            
            print() # Add final newline after stream completes
            
            # Add bot reply to history
            messages.append({"role": "assistant", "content": bot_reply})
            
        except Exception as e:
            print(f"\n[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    main()
