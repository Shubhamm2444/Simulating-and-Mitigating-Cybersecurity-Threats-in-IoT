Authentication
Use token-based authentication for secure access.
Code Example: Token-Based Authentication

from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Function to generate a token
def generate_token(user):
    token = jwt.encode({
        'user': user,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'])
    return token

# Endpoint to authenticate a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'password':
        token = generate_token(data['username'])
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Protected endpoint
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': f'Hello {data["user"]}'})
    except:
        return jsonify({'message': 'Token is invalid'}), 401

if __name__ == '__main__':
    app.run(debug=True)
