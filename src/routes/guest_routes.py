from flask import jsonify, Blueprint, request
from models.entities.guests import Guest
from models.GuestModels import GuestModel
from utils.id_generator import generate_id
from utils.carnet_verification import verification
from utils.date_manage import get_date_now, get_presentation_date, get_age, create_date, get_day


guest_routes = Blueprint('GuestRoutes', __name__)

@guest_routes.route('/register', methods=['POST'])
def register():
    try:
        id = generate_id()
        carnet = request.json['carnet']

        
        if verification(carnet):
            complete_name = request.json['complete_name']
            address = request.json['address']
            gender = request.json['gender']
            phone= request.json['phone']
            date = str(request.json['date_of_birth'])
            date_of = date.split('-')

            guest_age = get_age(int(date_of[0]),int(date_of[1]),int(date_of[2]))
            date_of_birth = create_date(int(date_of[0]),int(date_of[1]),int(date_of[2]))
            student_career = request.json['student_career']
            poetry_genre = request.json['poetry_genre']
            enrollment_date = get_date_now()
            presentation_date = get_presentation_date(enrollment_date, carnet[5], poetry_genre)

            
            guest = Guest(id, carnet, complete_name, address , gender, phone, date_of_birth,guest_age, student_career, poetry_genre, enrollment_date, presentation_date)

            affected_rows = GuestModel.add_guest(guest)

            if affected_rows == 1:
                return jsonify({
                    'id': id,
                    'carnet': carnet,
                    'complete_name': complete_name ,
                    'guest_age': guest_age,
                    'student_career': student_career,
                    'poetry_genre': poetry_genre ,
                    'enrollment_date': enrollment_date,
                    'presentation_date': presentation_date,
                    'presentation_day': get_day(presentation_date)})
            else:
                return jsonify({'message': "Error on insert"}), 500

        else:
            return jsonify({
                'message' : 'carnet invalid'
            })
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500