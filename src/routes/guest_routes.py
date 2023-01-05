from flask import jsonify, Blueprint, request
from models.GuestModels import Guest
from database.dbConect import db
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
            phone = request.json['phone']

            # Only for get an age from the string in the request 'date of birth' with the sintax 'year-month-day'
            date = str(request.json['date_of_birth'])
            date_of = date.split('-')
            date_of_birth = create_date(
                int(date_of[0]), int(date_of[1]), int(date_of[2]))

            # Here we get the age based on the date of birth variable
            guest_age = get_age(int(date_of[0]), int(
                date_of[1]), int(date_of[2]))
            
            # Here verify if the guest is an adult 

            is_adult = False
            if  guest_age >= 18: is_adult = True

            student_career = request.json['student_career']
            poetry_genre = request.json['poetry_genre']
            enrollment_date = get_date_now()
            presentation_date = get_presentation_date(
                enrollment_date, carnet[5], poetry_genre)
            
            is_saved = False
            if is_adult:
                guest = Guest( id = id, carnet = carnet, complete_name = complete_name, address = address ,gender = gender, phone = phone, date_of_birth = date_of_birth, guest_age = guest_age, student_career = student_career,  poetry_genre = poetry_genre, enrollment_date = enrollment_date, presentation_date = presentation_date)

                db.session.add(guest)
                db.session.commit()

                is_saved = True



            if is_saved == True:
                return jsonify({
                    'id': id,
                    'carnet': carnet,
                    'complete_name': complete_name,
                    'guest_age': guest_age,
                    'student_career': student_career,
                    'poetry_genre': poetry_genre,
                    'enrollment_date': enrollment_date,
                    'presentation_date': presentation_date,
                    'presentation_day': get_day(presentation_date)})
            else:
                return jsonify({'message': "Error on insert"}), 500

        else:
            return jsonify({
                'message': 'carnet invalid'
            })
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500



@guest_routes.route('/all', methods=['GET'])
def get_all():
    try:
        guests = []
        data = Guest.query.all()
        for guest in data:
            guests.append(guest.to_JSON())

        return jsonify(guests)
    except Exception as ex:
        return jsonify({
            'message':'Internal server rrror'
        }),500