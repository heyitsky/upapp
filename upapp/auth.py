from dotenv import load_dotenv
import os

def initialise():
    load_dotenv(dotenv_path='./auth.env')

def get_url():
    return "https://api.up.com.au/api/v1/"

def get_token():
    initialise()
    return os.getenv('API_TOKEN')