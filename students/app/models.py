from app import db

class Student(db.Model):
    """
    Create a student table
    """

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    student_number = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<Student: {}>'.format('N0 %i)' % (self.student_number))

class Mark(db.Model):
    """
    Create a student table
    """

    __tablename__ = 'marks'

    id = db.Column(db.Integer, primary_key=True)
    mark_value = db.Column(db.Integer, unique=True)
    mark_name = db.Column(db.String(60))

    def __repr__(self):
        return '<Student: {}>'.format('Mark %i)' % (self.mark_value))
