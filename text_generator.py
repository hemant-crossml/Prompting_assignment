"""
text_generator.py
-----------------
Contains helper functions responsible for interacting with
the Gemini model to generate text responses.

This module separates the text generation logic from
configuration and application flow.
"""

from utils import print_output, retry_delay

def generate_text(client, model_name, System_prompt,User_prompt, config):
    """
    Generates text using the Gemini model based on a user prompt.

    Args:
        client: Initialized Gemini client instance.
        model_name (str): Name of the Gemini model to be used.
        System_prompt (str): System instruction guiding model behavior.
        User_prompt (str): User-provided input prompt.
        config: Generation configuration containing parameters
                such as temperature and token limits.

    Returns:
        None
    """
    
    try:
        # Send the user prompt to the Gemini model for text generation
        response = client.models.generate_content(
            model=model_name,  
            contents=User_prompt,
            config=config
        )
        # Print formatted output including prompts and model response
        print_output(System_prompt,User_prompt, response.text)

    except Exception as e:
        # Handle runtime or API-related errors gracefully
        print("Error occurred:", e)

        # Apply a delay before retrying or exiting
        retry_delay()
