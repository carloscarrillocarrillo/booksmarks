import os
from flask import Flask
from flask import jsonify
from flask import request
from Security.user.create import create_user

app = Flask(__name__)

@app.route('/')
def hello():
  response = {
    'message': 'API Security',
    'version': '1.0.0',
    'code': 200,
  }
  return jsonify(response)

@app.route('/user', methods=['POST'])
def cu():
  res = create_user('','','')
  form = request.form
  username = form['username']
  response = {
    'message': str.format('user created {} {}', username, str(res)),
    'code': 200,
  }
  return jsonify(response)

#return app
  
if __name__ == '__main__':
  app.run()