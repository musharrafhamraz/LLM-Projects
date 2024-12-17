import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def handle_response(user_input: str) -> str:
    """
    Takes user input, passes it to the LLM model via the Groq client, and returns the response.
    """
    try:
        print(f"User input: {user_input}")
        system_message = "You are an AI assistant"
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input},
        ]

        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Adjust the model name if necessary
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            top_p=0.95,
            stream=False,
        )

        output = completion.choices[0].message.content.strip()

        if output.startswith("Assistant:"):
            output = output[len("Assistant:"):].strip()

        return output
    except Exception as e:
        print(f"Error during response generation: {e}")
        return f"An error occurred: {e}"
