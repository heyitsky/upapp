import os
from dotenv import load_dotenv

def get_auth_info():
    load_dotenv(dotenv_path='./upapp/auth.env')
    return ("https://api.up.com.au/api/v1/", os.getenv('API_TOKEN'))