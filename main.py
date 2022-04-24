import subprocess
import os

from dotenv import load_dotenv
from github_webhook import Webhook
from flask import Flask

load_dotenv()

secret = os.getenv("SIMPLE_DEPLOY_SECRET")
port = int(os.getenv("SIMPLE_DEPLOY_PORT"))

app = Flask(__name__)
webhook = Webhook(app, secret=secret)  # Defines '/postreceive' endpoint

@app.route("/")
def hello_world():
    return "OK"


@webhook.hook()  # Defines a handler for the 'push' event
def on_push(data):
    subprocess.run(["sh", "deploy.sh"])
    return "OK"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=port)