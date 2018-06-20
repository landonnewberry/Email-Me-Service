
import os
from flask import Flask, request

# controllers
from api.controllers.email import EmailController

app = Flask(__name__)

API_PREFIX = "/api/v1"

try:
	USER_EMAIL = os.environ["USER_EMAIL"]
	USER_PASSWORD = os.environ["USER_PASSWORD"]
	APP_PORT = os.environ["APP_PORT"]
except:
	raise ValueError("You must provide environment variables USER_EMAIL, USER_PASSWORD, APP_PORT")


email_controller = EmailController(USER_EMAIL, USER_PASSWORD)


@app.route("{}/email".format(API_PREFIX), methods=["POST"])
def email():
	if request.method == "POST":
		return email_controller.post_email(request.form)
	else:
		return jsonify({ "ERROR": "Method not allowed" })




if __name__ == "__main__":
	app.run(port=APP_PORT)

