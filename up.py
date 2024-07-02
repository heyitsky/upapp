from dotenv import load_dotenv
import requests
import os

load_dotenv(dotenv_path='./auth.env')

def get_token():
    return os.getenv('API_TOKEN')

if __name__ == "__main__":
    token = get_token()
    print(token)