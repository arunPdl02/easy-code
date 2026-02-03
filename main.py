import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function



def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
        

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Gemini API Key Not found!")

    client = genai.Client(api_key= api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model ='gemini-2.5-flash',
        contents = messages,
        config = types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction = system_prompt),
        )
    token_metadata = response.usage_metadata
    if not token_metadata:
        raise RuntimeError("Gemini API response is incomplete, no metadata recieved")
    
    if verbose:
        print(f"Prompt tokens: {token_metadata.prompt_token_count}")
        print(f"Response tokens: {token_metadata.candidates_token_count}")

    function_result = []

    if response.function_calls:
        print("Function calls")
        for call in response.function_calls:
            function_call_result = call_function(call, verbose)
            if not function_call_result.parts:
                raise Exception("funciton call doesn't have parts property")
            if not function_call_result.parts[0]:
                raise Exception
            if not function_call_result.parts[0].function_response.response:
                raise Exception("no response from the function call")
            function_result.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print("Response:")
        print(response.text)




if __name__ == "__main__":
    main()
