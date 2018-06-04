from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,TextAreaField, ValidationError
from wtforms.validators import DataRequired

from flask_wtf.file import FileField, FileAllowed, FileRequired

class CampgroundForm(FlaskForm):
    """
    form for a users to add campgrounds
    """
    name = StringField('Campground name', validators=[DataRequired('Please enter campground name')])
    image = FileField('image', validators=[DataRequired('Please upload an image'),FileAllowed(['jpg', 'png', 'jpeg'], 'image must be a jpg, png or jpeg')])
    location = StringField('Location', validators=[DataRequired('Please enter a location')])
    price = StringField('Price', validators=[DataRequired('Please enter Price')])
    description = TextAreaField('Description', validators=[DataRequired('Please enter descriptoin of campground')])

    
