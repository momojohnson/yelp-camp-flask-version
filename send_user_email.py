import os
from flask_mail import Message
from app import mail

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


def send_email(to, subject, template):
	msg = Message(subject,
		recipients= [to],
		sender=app.config['MAIL_USERNAME'])
	msg.html = template
	mail.send(msg)
