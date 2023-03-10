from flask import Flask, request, jsonify
import chatbot_model

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']
    response = chatbot_model.get_response(user_input)
    return jsonify({'response': response})
