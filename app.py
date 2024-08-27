from flask import Flask
app = Flask(__name__)

@app.route('/')
def eventlogger():
    return 'Hello, World!'
