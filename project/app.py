# -*- coding: utf-8 -*-
import argparse

from flask import Flask, request
from services.mailgun import mailgun

app = Flask(__name__)


@app.route("/mailgun/status/", methods=["GET"])
def status():
    return "Up & running...", 200


@app.route("/mailgun/email/", methods=["POST"])
def send_email():
    return mailgun().send(request.data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", help="Port Number to run the server on, default=5000"
    )
    args = vars(parser.parse_args())
    app.run(debug=True, port=args["port"] or 5000)
