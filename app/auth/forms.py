from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, ValidationError

from wtforms.validators import DataRequired, Email, EqualTo

from .. models import User

class RegistrationForm(FlaskForm):
    """
    Form for user registration

    """
    email = StringField('Email', validators=[DataRequired('Please enter an email'), Email()])
    username = StringField('Username', validators=[DataRequired('Please enter a username')])
    first_name = StringField('First Name', validators=[DataRequired("Please enter a first name")])
    last_name = StringField('Last Name', validators=[DataRequired("Please enter a last name")])
    profile_pic = StringField('Profile Picture', validators=[DataRequired("Please provide image url")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password"),
                EqualTo('confirm_password', message="Password field must match confirm password field")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired("Confirm password is required")])


    def validate_email(self, field):
        """
        Validate user email
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has already been registered')

    def validate_username(self, field):
        """
        Vaidate username
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already is use')


class LoginForm(FlaskForm):
    """
    A Login Form for website users
    """
    email = StringField('Email', validators=[DataRequired("Please enter an email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter password")])

class PasswordResetForm(FlaskForm):
	"""
	A form that handles user password reset when a user forgets his/her password
	"""
	password = PasswordField("New Password",
			 	validators=[DataRequired("Please enter your new password"),
			 	EqualTo("confirm_password")])
	confirm_password = PasswordField("Confirm Password",
				validators=[DataRequired("Please Confirm your password")])


class EmailForm(FlaskForm):
	"""
	A form that handles getting a user email
	"""
	user_email = StringField('Email',
				validators=[DataRequired("Please enter the email address"),
				Email()])


	def validate_user_email(self, field):
		if not User.query.filter_by(email=field.data).first():
			raise ValidationError("This email isn't registered.")
