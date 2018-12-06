from flask import Flask
from flask import request
from flask.json import jsonify
import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from random import randint

users = []

@app.route('/api/routes/status', methods=['POST'])
def status():
    user = request.args.get('user')
    if user not in users:
        return 'User not registered!', 400
    try:
        response = {
            'front': {
                'name' : 'Moe',
                'time' : '1min',
                'distance' : randint(0, 9)
                },
            'back': {
                'name' : 'Elie',
                'time' : '3min',
                'distance' : randint(0, 9)
                }
            }
        return jsonify(response)
    except Exception as e:
        return jsonify(e)

@app.route('/api/routes/register')
def register():
    user = request.args.get('user')
    if user in users:
        return user + ' already exists!', 400
    users.append(user)
    return jsonify(users)
    
@app.route('/api/routes/remove')
def remove():
    user = request.args.get('user')
    if user not in users:
        return user + ' does not exist!', 400
    users.remove(user)
    return jsonify(users)    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

