from client import get_client
from config import generation_config
from prompts import System_Prompt, User_prompt
from text_generator import generate_text

def main():
    client = get_client()
    model_name = "gemini-2.5-flash"
    generate_text(client, model_name, System_Prompt, User_prompt,generation_config)

if __name__ == "__main__":
    main()
