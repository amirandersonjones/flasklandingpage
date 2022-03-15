from flask_wtf import FlaskForm #the base form object for forms in our flask app
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    moviename = StringField('Movie Name', validators=[DataRequired()])
    submit = SubmitField()