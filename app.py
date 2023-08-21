from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Business Applications- Cloud Solution Architect Copilot"
