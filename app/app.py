from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def main():
    return f"You're seeing this page from Container ID: {socket.gethostname()}"

if __name__ == "__main__":
    app.run(debug=True)
