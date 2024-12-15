import os
from groq import Groq

class ChatBot:
    def __init__(self):
        # Initialize API key from environment variable or direct assignment
        self.groq_api_key = os.getenv("GROQ_API_KEY", "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")
        if not self.groq_api_key:
            raise ValueError("Please set the GROQ_API_KEY environment variable.")

        self.client = Groq(api_key=self.groq_api_key)

    def generate_response(self, user_input, prompt_type="default", custom_prompt="", model="mixtral-8x7b-32768"):
        """
        Generates a chatbot response based on user input.

        :param user_input: The message from the user.
        :param prompt_type: Predefined prompt type or "custom" for a custom prompt.
        :param custom_prompt: Custom base prompt if `prompt_type` is "custom".
        :param model: The model to use for generating responses.
        :return: Chatbot response as a string.
        """
        try:
            # Predefined prompts
            prompts = {
                "default": "You are a helpful and friendly assistant. Answer the user's questions politely and concisely.",
                "detailed": "You are an expert assistant. Provide detailed and insightful answers to the user's queries.",
                "funny": "You are a witty assistant. Respond to the user's questions with humor and creativity.",
            }

            # Select the base prompt
            if prompt_type == "custom" and custom_prompt.strip():
                base_prompt = custom_prompt
            else:
                base_prompt = prompts.get(prompt_type, prompts["default"])

            # Construct the message payload
            system_message = base_prompt
            user_message = f"User: {user_input}"

            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ]

            # Make the API call to Groq
            completion = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=512,
                top_p=0.95,
                stream=False,
            )

            # Extract the response content
            output = completion.choices[0].message.content.strip()

            # Remove assistant prefix if present
            if output.lower().startswith("assistant:"):
                output = output[len("assistant:"):].strip()

            return output

        except Exception as e:
            print(f"An error occurred: {e}")
            return f"Sorry, I encountered an error: {str(e)}"

if __name__ == "__main__":
    # Initialize the chatbot
    chatbot = ChatBot()

    print("Welcome to the Groq-based ChatBot! Type 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break

        # Generate and display the response
        response = chatbot.generate_response(user_input)
        print(f"ChatBot: {response}")
