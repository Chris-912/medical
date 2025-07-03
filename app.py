# app.py

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ai_helper import get_ai_response
import requests  # Added for making HTTP requests

app = Flask(__name__)
CORS(app)


@app.route('/check', methods=['POST'])
def check():
    symptoms = request.json.get('symptoms')
    if not symptoms:
        return jsonify({'error': 'No symptoms provided'}), 400
    try:
        # If you want to call another API in Python, use requests.post(...)
        # Example:
        # response = requests.post('http://example.com/other-api', json={'symptoms': symptoms})
        # result = response.json().get('analysis', 'No analysis found.')

        # Your existing AI helper call
        result = get_ai_response(symptoms)
        return jsonify({'analysis': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET'])
def home():
    return render_template('Recovery.html')


if __name__ == '__main__':
    app.run(debug=True)






