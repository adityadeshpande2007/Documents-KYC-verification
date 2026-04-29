from flask import Flask, request, jsonify
from gemini_api import extract_data
from database import save_data, init_db
from utils import parse_json, validate

app = Flask(__name__)

init_db()

@app.route('/verify', methods=['POST'])
def verify():
    file = request.files['file']
    image_bytes = file.read()

    raw_text = extract_data(image_bytes)
    data = parse_json(raw_text)

    if not data:
        return jsonify({"error": "Failed to parse AI response"})

    missing, errors = validate(data)

    if missing:
        return jsonify({
            "status": "incomplete",
            "missing_fields": missing,
            "data": data
        })

    if errors:
        return jsonify({
            "status": "invalid",
            "errors": errors,
            "data": data
        })

    save_data(data)

    return jsonify({
        "status": "success",
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True)