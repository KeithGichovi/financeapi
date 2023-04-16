from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class CheckData(FlaskForm):
    symbol = StringField("Company Symbol", validators=[DataRequired()])
    submit = SubmitField("Check information")
