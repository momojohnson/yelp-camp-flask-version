from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,TextAreaField, ValidationError
from wtforms.validators import DataRequired


class CampgroundForm(FlaskForm):
    """
    form for a users to add campgrounds
    """
    name = StringField('Campground name', validators=[DataRequired('Please enter campground name')])
    image = StringField('Image url', validators=[DataRequired('Please enter image usr')])
    location = StringField('Location', validators=[DataRequired('Please enter a location')])
    price = StringField('Price', validators=[DataRequired('Please enter Price')])
    description = TextAreaField('Description', validators=[DataRequired('Please enter descriptoin of campground')])