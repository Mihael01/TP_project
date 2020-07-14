from app import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, ForeignKey, Integer
from sqlalchemy.orm import relationship, sessionmaker

class Student(db.Model):
    """
    Create a student table
    """

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    student_number = db.Column(db.Integer, unique=True)
    student_marks = db.relationship('Mark', backref='student',
                                lazy='dynamic')

    def __repr__(self):
        return '<Student: {}>'.format('N0 %i)' % (self.student_number))

class Mark(db.Model):
    """
    Create a student table
    """

    __tablename__ = 'marks'

    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return '<Student: {}>'.format('Mark %i)' % (self.mark))
