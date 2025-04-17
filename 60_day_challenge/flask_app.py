from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from your Dockerized Flask app!"

app.run(host='0.0.0.0', port=5000)