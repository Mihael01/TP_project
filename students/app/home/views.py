from forms import StudentForm
from ..models import Student, Mark
from flask import Flask, render_template, flash, redirect, url_for

from .. import db
from . import home

# Student Views
class StudentView():
    """
    Student with average makr
    """
    average_mark=0.0
    
    def __init__(self, student):
		self.id = student.id
		self.first_name = student.first_name
		self.last_name = student.last_name
		self.student_number = student.student_number
		self.student_marks = student.student_marks
		for mark in student.student_marks:
			self.average_mark += mark.mark
		self.average_mark /= 5

@home.route('/students')
def list_students():
    """
    List all students
    """
    
    selectedStudents = Student.query.all()
    students = []
    for student in selectedStudents:
		students.append(StudentView(student))
             
        
    	       
    
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
            flash('Error: Student number ' + str(student.student_number) +' already exists.')  
            
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
        
        # update studentin database
        db.session.merge(student)
        db.session.commit()
        #create all marks for current student        
        for mark in form.student_marks.data:
        	student_mark = Mark(mark, student.id)
        	# update student marks in database
        	db.session.merge(student_mark)
        	db.session.commit()

        flash('You have successfully updated student and student marks.')

        # redirect to the students page
        return redirect(url_for('home.list_students'))
        
        #marks=Mark.query.filter_by(Mark.student_id == id).all()
        selected_marks = Mark.query.filter_by(Mark.student_id == id).all()
        

        form.first_name.data=student.first_name
        form.last_name.data=student.last_name
        form.student_number.data=student.student_number
        form.student_marks.data=selected_marks
    return render_template('student.html', add_student=add_student,
                           form=form, title='Add Student')


@home.route('/students/delete/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
    """
    Delete a student from the database
    """

    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('You have successfully deleted the student.')

    # redirect to the students page
    return redirect(url_for('home.list_students'))
        

    return render_template(title="Delete Student")

