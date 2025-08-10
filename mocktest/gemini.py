import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
# Set your Google Gemini API key
genai.configure(api_key= os.getenv("API_KEY"))

def getData(payload: str):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        # response = model.generate_content(payload["messages"][0]["content"])
        response = model.generate_content(payload)
        if response and response.text:
            return json.dumps({'status': True, 'message': response.text})
        else:
            return json.dumps({'status': False, 'message': "No response received from Gemini."})

    except Exception as e:
        return json.dumps({'status': False, 'message': str(e)})