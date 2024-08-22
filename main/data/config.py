import os

from dotenv import dotenv_values, load_dotenv

# dotenv_values() - returns only empty dict, cannot fine .env file for some reason....

load_dotenv()
token = os.getenv("TOKEN")
admin = 7210542141