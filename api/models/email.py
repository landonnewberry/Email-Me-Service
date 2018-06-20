
class Email(object):

	def __init__(self, sender, recipients, subject, body):
		if not (isinstance(sender, str) &
			isinstance(recipients, list) &
			isinstance(subject, str) &
			isinstance(body, str)):
			raise ValueError("sender: str, recipients: list, subject: str, body: str")
		else:
			self.sender = sender
			self.recipients = recipients
			self.subject = subject
			self.body = body
			self.text = """\
To: {}
Subject: {}

{} sent this message:

{}
""".format(', '.join(recipients), subject, sender, body)




