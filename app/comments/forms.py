from flask_wtf import FlaskForm
from wtforms import TextAreaField, ValidationError
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired('Please enter a comment')])
