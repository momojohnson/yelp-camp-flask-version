from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class commentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired("Please enter a comment")])