import os
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from ai-agent-bootdev!")


if __name__ == "__main__":
    main()



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)

GenCliRes = client.models.generate_content(model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.')
print(GenCliRes.text)
ptokens = GenCliRes.usage_metadata.prompt_token_count
rtokens = GenCliRes.usage_metadata.candidates_token_count
print(f"Prompt tokens: {ptokens}\n"
      f"Response tokens: {rtokens}")
