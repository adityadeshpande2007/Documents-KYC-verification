import json

def parse_json(text):
    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    except:
        return {}

def validate(data):
    required = ["name", "date_of_birth", "id_number"]
    missing = [f for f in required if f not in data or not data[f]]
    
    errors = []
    
    if "id_number" in data and len(data["id_number"]) < 5:
        errors.append("Invalid ID number")
    
    return missing, errors