from ..forms import StudentForm
from ..models import Student
from flask import Flask, render_template, flash, redirect, url_for

from .. import db
from . import home

# Student Views

@home.route('/students')
def list_students():
    """
    List all students
    """
    #return 'Welcome to "Student marksrrrrrrrrrrr" app!'

    students = Student.query.all()
    return render_template('students.html', students=students, title='Students')
    
    
@home.route('/students/add', methods=['GET', 'POST'])
def add_student():
    """
    Add a student to the database
    """

    add_student = True

    form = StudentForm()

    if form.validate_on_submit():
        student = Student(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    student_number=form.student_number.data)

        try:
            # add student to the database
            db.session.add(student)
            db.session.commit()
            flash('You have successfully added a new student.')
        except:
            # in case role name already exists
            flash('Error: student number ' + student.student_number +' already exists.')   

        # redirect to the roles page
        return redirect(url_for('home.list_students'))

    # load role template
    return render_template('student.html', add_student=add_student,
                           form=form, title='Add Student')
