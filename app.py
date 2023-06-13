from dotenv import load_dotenv

load_dotenv()  
import os
# take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
API_KEY = os.getenv("API_KEY")
url = f"https://example.com/{API_KEY}"
print("The url is ", url )