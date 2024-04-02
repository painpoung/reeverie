import openai

# Replace "your_openai_api_key_here" with your actual OpenAI API key
openai.api_key = "your_openai_api_key_here"


def ask_gpt(user_message):
    """
    Sends a message to GPT-3.5 and returns the response.

    Parameters:
    - user_message (str): The message from the user to send to GPT-3.5.

    Returns:
    - str: The response from GPT-3.5.
    """
    try:
        # Call the OpenAI API, specifying the model, the prompt (user message),
        # and any other parameters relevant to your use case.
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # or another model name if you prefer
            prompt=user_message,
            temperature=0.7,  # Adjusts randomness in the responses, tweak based on your needs
            max_tokens=150,  # Limits the length of the response
        )

        # Extracting the text from the response object
        gpt_text = response.choices[0].text.strip()

        return gpt_text

    except Exception as e:
        print(f"An error occurred: {e}")
        # Return a default message or handle the error as you see fit
        return "I'm sorry, I couldn't process that message."
