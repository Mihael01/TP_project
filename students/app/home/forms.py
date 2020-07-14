from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    """
    Form to add or edit a role
    """
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    student_number = StringField('Student number', validators=[DataRequired()])
    submit = SubmitField('Submit')
