from flask import Flask, jsonify, make_response, request
from google import genai
from google.genai import types
import json

app = Flask(__name__)
with open('../config.json', 'r') as config_file:
    client = genai.Client(api_key=json.load(config_file)['API'])

chat = client.chats.create(model="gemini-2.0-flash", 
                           config=types.GenerateContentConfig(
                               system_instruction="You are a senior Data Scientist from Google. Your name is Datagment AI.",
                               temperature=1.0)
                            )

@app.route("/query/text", methods=["GET"])
def ask():
    try:
        question = request.headers['question']
        print(question)
        response = chat.send_message(question)
        return response.text
    except Exception:
        return jsonify({'Error': 'Gemini failed to answer the query.'}), 500

if __name__ == "__main__":
    # Run on localhost
    app.run(host="0.0.0.0", port=8080, debug=True)
    