import subprocess
from github_webhook import Webhook
from flask import Flask

secret = open("secret", "r").readline().strip()

app = Flask(__name__)
webhook = Webhook(app, secret=secret)  # Defines '/postreceive' endpoint


@app.route("/")
def hello_world():
    return "Hello, World!"


@webhook.hook()  # Defines a handler for the 'push' event
def on_push(data):
    subprocess.run(["sh", "deploy.sh"])
    return "OK"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=40148)