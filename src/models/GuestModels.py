from database.dbConect import get_connection

class GuestModel():

    @classmethod
    def add_guest(self, guest):
        try:
            connection = get_connection()
            

            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO guest (id, carnet, complete_name, address, gender, phone, date_of_birth, guest_age, student_career, poetry_genre, enrollment_date, presentation_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (guest.id, guest.carnet, guest.complete_name, guest.address , guest.gender, guest.phone , guest.date_of_birth,guest.guest_age , guest.student_career , guest.poetry_genre, guest.enrollment_date, guest.presentation_date))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise ex