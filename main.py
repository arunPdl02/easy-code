import os
from dotenv import load_dotenv
from google import genai
import argparse



def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    user_prompt = args.user_prompt

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Gemini API Key Not found!")

    client = genai.Client(api_key= api_key)
    response = client.models.generate_content(
        model ='gemini-2.5-flash',
        contents = user_prompt
        )

    token_metadata = response.usage_metadata
    if not token_metadata:
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
