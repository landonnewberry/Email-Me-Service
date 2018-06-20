import os
import smtplib
from flask import jsonify
import json
from ..models.email import Email

class EmailController(object):

	def __init__(self, user_email, user_password, smtp_server="smtp.gmail.com", smtp_socket=465):
		self._user_email = user_email
		self._user_password = user_password
		self._smtp_server = smtp_server
		self._smtp_socket = smtp_socket


	def _send_email(self, email):
		try:
			server = smtplib.SMTP_SSL(self._smtp_server, self._smtp_socket)
			server.ehlo()
			server.login(self._user_email, self._user_password)
			server.sendmail(self._user_email, self._user_email, email.text)
			server.close()
		except:
			raise ValueError("Either could not authenticate user or could not send email.")


	def post_email(self, data):
		if not (("sender" in data) &
#                        ("recipients" in data) &
                        ("subject" in data) &
                        ("body" in data)):
			raise ValueError("REQUIRED FIELDS: sender, recipients, subject, body")
		else:
			# later save to a database
			try:
				e = Email(
					sender=data["sender"],
#					recipients=json.loads(data["recipients"]),
					recipients=[ self._user_email ],
					subject=data["subject"],
					body=data["body"]
				)
			except:
				raise ValueError("Improper input to Email contructor")

			try:
				self._send_email(e)
			except:
				raise RuntimeError("Email not available for sending")

			return jsonify({ "msg": 200 })


