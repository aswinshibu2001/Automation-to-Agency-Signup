import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
PASSWORD=os.getenv("mail_password")
MAIL=os.getenv("mail_id")