import os
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
  response = {
    'message': 'API Bookmark',
    'version': '1.0.0',
    'code': 200,
  }
  return jsonify(response)

#return app
  
if __name__ == '__main__':
  app.run()