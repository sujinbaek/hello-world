import logging
from flask import Flask, request

app = Flask(__name__)
# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def root():
    return "Hello, World!"

@app.route('/healthz', methods=['GET'])
def health_check():
    return {'status': 'OK'}

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True, port=8080)
