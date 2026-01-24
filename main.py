import argparse
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    #print("Hello from ai-agent!")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    prompt = args.user_prompt
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    if response.usage_metadata is None:
        raise RuntimeError("Something went wrong. LLM API response does not contain expected data.")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n {response.text}")


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API Key registered!")
    main()
