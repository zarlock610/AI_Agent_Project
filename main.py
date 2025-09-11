import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if len(sys.argv) < 2:
        print("You must provide a prompt as a command line argument.", file=sys.stderr) 
        sys.exit(1)
    elif len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            user_prompt = sys.argv[1]
            messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
            client = genai.Client(api_key=api_key)
            GenCliRes = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
            ptokens = GenCliRes.usage_metadata.prompt_token_count
            rtokens = GenCliRes.usage_metadata.candidates_token_count
            
            print(f"Response: {GenCliRes.text}")
            print(f"User prompt: {sys.argv[1]}")
            print(f"Prompt tokes: {ptokens}")
            print(f"Response tokens: {rtokens}")
        else: print("Improper Argument. Use --verbose for detailed output.", file=sys.stderr)  
    else: 
        user_prompt = sys.argv[1]
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        client = genai.Client(api_key=api_key)
        GenCliRes = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
        
        print(f"Response: {GenCliRes.text}")
    
   
    
    
    
    
    
    


if __name__ == "__main__":
    main()






