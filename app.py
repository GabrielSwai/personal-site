from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Gabriel Swai</h1><p>Welcome to my site!</p>"
