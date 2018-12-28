from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class DateForm(FlaskForm):
    day = IntegerField('Day', validators=[DataRequired()], render_kw={"class": "custom-select mr-sm-2","id" : "inlineFormCustomSelect"})
    month = IntegerField('Month', validators=[DataRequired()], render_kw={"class": "custom-select mr-sm-2","id" : "month"})
    year = IntegerField('Year', validators=[DataRequired()], render_kw={"class": "custom-select mr-sm-2","id" : "year"})
    charts = StringField('Charts', validators=[DataRequired()], render_kw={"class": "custom-select mr-sm-2","id" : "chart"})
    search = SubmitField('Search', render_kw={"class": "btn btn-primary"})

# day = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])