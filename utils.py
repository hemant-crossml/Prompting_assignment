import time

def print_output(System_prompt, User_prompt,output):
    print("\n" + "-" * 60)
    print("PROMPT:")
    print(System_prompt,"\n",User_prompt)
    print("\nOUTPUT:")
    print(output)
    print("-" * 60)

def retry_delay(seconds=2):
    time.sleep(seconds)
