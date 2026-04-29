import google.generativeai as genai
import json

# 🔑 Add your API key here
genai.configure(api_key="AIzaSyBsa-UpzC-qPQdXF30SAWxoR5k5YbfnILU")

model = genai.GenerativeModel("gemini-2.5-flash")

PROMPT = """
Extract the following fields from the document image:
- name
- date_of_birth
- address
- id_number

Return ONLY valid JSON in this format:
{
  "name": "",
  "date_of_birth": "",
  "address": "",
  "id_number": ""
}
"""

def extract_data(image_bytes):
    response = model.generate_content([
        PROMPT,
        {"mime_type": "image/jpeg", "data": image_bytes}
    ])
    
    return response.text