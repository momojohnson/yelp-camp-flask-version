import os
import secrets
from itsdangerous import URLSafeTimedSerializer
from app import create_app

config_name = os.environ.get('FLASK_CONFIG')
app = create_app(config_name)
def generate_confirmation_token(email):
    """
    Generate  a confirmation token using the email address
    submitted through registration form
    """
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=app.config["SECURITY_PASSWORD_SALT"])

def confirm_token(token, expiration=3600):
    """
    confirm token with for a user with 1hr expiration.
    If the confirmation is valid, an email will be returned
    """
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(token,
		salt=app.config["SECURITY_PASSWORD_SALT"],
		max_age=expiration)
    except:
        return False
    return email
