from utils import print_output, retry_delay

def generate_text(client, model_name, System_prompt,User_prompt, config):
    try:
        response = client.models.generate_content(
            model=model_name,  
            contents=[System_prompt,User_prompt],
            config=config
        )

        print_output(System_prompt,User_prompt, response.text)

    except Exception as e:
        print("Error occurred:", e)
        retry_delay()
