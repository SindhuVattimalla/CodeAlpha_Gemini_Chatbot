from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('intents.json') as f:
    responses = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot():
    user_message = request.json['message'].lower()

    reply = responses.get(
        user_message,
        "Sorry, I didn't understand that."
    )

    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)