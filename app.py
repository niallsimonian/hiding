from dotenv import load_dotenv

load_dotenv()  
import os
# take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
API_KEY = os.getenv("API_KEY")
ANOTHER_KEY = os.getenv("ANOTHER_KEY")
print(ANOTHER_KEY)
url = f"https://example.com/{API_KEY}"
print("The url is ", url )

#if you are in jupyter notebook and use print function for a variable in .env, people will still be able to see it in your jupyter file. 
# So, if the data is sensitive, keep the use of the variable to requests (and related) functions that will hide it. or just don't put it in an .env if its not secret then. 