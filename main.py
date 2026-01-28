import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Gemini API Key Not found!")

from google import genai

client = genai.Client(api_key= api_key)


def main():
    user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model ='gemini-2.5-flash',
        contents = user_prompt
        )
    token_metadata = response.usage_metadata
    if token_metadata == None:
        raise RuntimeError("failed API request, no metadata recieved")
    response_text = response.text
    prompt_token_count = token_metadata.prompt_token_count
    response_token_count = token_metadata.candidates_token_count

    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {response_token_count}")
    print("Response:")
    print(response_text)


if __name__ == "__main__":
    main()
