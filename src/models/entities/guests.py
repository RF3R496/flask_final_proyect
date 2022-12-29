from utils.date_manage import get_day
class Guest():
    def __init__(self, id = None, carnet = None, complete_name = None, address = None, gender = None, phone = None, date_of_birth = None,guest_age = None, student_career = None, poetry_genre = None, enrollment_date = None, presentation_date = None):
        
        self.id = id
        self.carnet = carnet
        self.complete_name = complete_name
        self.address = address
        self.gender = gender
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.guest_age = guest_age
        self.student_career = student_career
        self.poetry_genre = poetry_genre
        self.enrollment_date = enrollment_date
        self.presentation_date = presentation_date


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