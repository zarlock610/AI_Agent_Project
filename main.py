import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("You must provide a prompt as a command line argument.", file=sys.stderr) 
        sys.exit(1)  
    else: print(f"Generating content for: {sys.argv[1]}")
    GenCliRes = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
    print(GenCliRes.text)
    ptokens = GenCliRes.usage_metadata.prompt_token_count
    rtokens = GenCliRes.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {ptokens}\n"
      f"Response tokens: {rtokens}")


if __name__ == "__main__":
    main()






