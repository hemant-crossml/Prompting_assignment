"""
main.py
-------
Application entry point for the LLM text generation project.

This module orchestrates the overall flow by:
- Loading the Gemini client
- Importing model configuration and prompts
- Triggering the text generation process
"""

from client import client
from config import CONFIG, MODEL_NAME
from prompts import system_prompt, user_prompt
from text_generator import generate_text

def main():
    """
    Summary:
        Calls the text generation function with the configured client,
        model name, system prompt, user prompt, and generation settings.

    Args:
        None

    Return:
        None
    """
    generate_text(client, MODEL_NAME, system_prompt, user_prompt,CONFIG)


# Ensures the main function runs only when this file
# is executed directly, not when imported as a module
if __name__ == "__main__":
    main()
