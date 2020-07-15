from forms import StudentForm
from ..models import Student, Mark
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
            #create all marks for current student        
            for mark in form.student_marks.data:
                student_mark = Mark(mark, student.id)

                # add student marks to the database
                db.session.add(student_mark)
                db.session.commit()

            flash('You have successfully added a new student.')
        except:
            # in case student number already exists
            flash('Error: student number ' + str(student.student_number) +' already exists.')  
            
        # redirect to the students page
        return redirect(url_for('home.list_students'))

    # load student template
    return render_template('student.html', add_student=add_student,
                           form=form, title='Add Student')

@home.route('/students/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    """
    Edit a student
    """
    add_student = False

    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.first_name=form.first_name.data
        student.last_name=form.last_name.data
        student.student_number=form.student_number.data

        db.session.add(student)
        db.session.commit()
        flash('You have successfully edited the student.')

        # redirect to the students page
        return redirect(url_for('home.list_students'))

        form.first_name.data=student.first_name
        form.last_name.data=student.last_name
        form.student_number.data=student.student_number
        form.student_marks.data=student.student_marks
    return render_template('student.html', add_student=add_student,
                           form=form, title='Add Student')

