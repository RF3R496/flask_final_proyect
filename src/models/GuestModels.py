from database.dbConect import db
from utils.date_manage import get_day

class Guest(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    carnet = db.Column(db.String(6), nullable = False)
    complete_name = db.Column(db.String(100), nullable = False)
    address = db.Column(db.String(75), nullable = False)
    gender = db.Column(db.String(20), nullable = False)
    phone = db.Column(db.String(15), nullable = False)
    date_of_birth = db.Column(db.Date)
    guest_age = db.Column(db.Integer, nullable = False)
    student_career = db.Column(db.String(50), nullable = False)
    poetry_genre = db.Column(db.String(20), nullable = False)
    enrollment_date =  db.Column(db.Date)
    presentation_date = db.Column(db.Date)


    def __repr__(self):
        return self.carnet


    def to_JSON(self):
        return {
            'id': self.id,
            'carnet': self.carnet,
            'complete_name': self.complete_name ,
            'address': self.address ,
            'gender': self.gender ,
            'phone': self.phone ,
            'date_of_birth':self.date_of_birth,
            'guest_age': self.guest_age,
            'student_career':self.student_career,
            'poetry_genre':self.poetry_genre ,
            'enrollment_date':self.enrollment_date,
            'presentation_date':self.presentation_date,
            'presentation_day': get_day(self.presentation_date)
        }
"""

id VARCHAR(36) primary key,
	carnet VARCHAR(6) not null,
	complete_name VARCHAR(100) not null,
	address VARCHAR(75) not null,
	gender VARCHAR(20) not null,
	phone character(15) not null,
	Date_of_birth date not null,
	guest_age integer not null,
	student_career VARCHAR(50) not null,
	poetry_genre VARCHAR(20) not null,
	enrollment_date date,
	presentation_date date
)
"""