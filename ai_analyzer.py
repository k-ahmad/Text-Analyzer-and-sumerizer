import os
from dotenv import load_dotenv
from google import genai

text = str(input('Enter your question: '))
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = 'gemini-3.5-flash',
    contents= text
)

print(response.text)
