from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, IntegerField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.widgets import html5

class StudentForm(FlaskForm):
    """
    Form to add or edit a role
    """
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    student_number = StringField('Student number', validators=[DataRequired()])
    student_marks = FieldList(IntegerField('Student mark', widget=html5.NumberInput(min=2,max=6)), validators=[DataRequired()], min_entries = 5,  render_kw={'style':'display: inline-block'})
    submit = SubmitField('Submit')
