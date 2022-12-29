from database.dbConect import get_connection
from models.entities.guests import Guest

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



    @classmethod
    def get_all(self):

        try:
            connection = get_connection()
            guests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, carnet, complete_name, address, gender, phone, date_of_birth, guest_age, student_career, poetry_genre, enrollment_date, presentation_date FROM guest ORDER BY complete_name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    guest = Guest(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                    guests.append(guest.to_JSON())

            connection.close()
            return guests
        except Exception as ex:
            raise Exception(ex)




    @classmethod
    def get_by_poetry_genre(self, condition):

        try:
            connection = get_connection()
            guests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, carnet, complete_name, address, gender, phone, date_of_birth, guest_age, student_career, poetry_genre, enrollment_date, presentation_date FROM guest WHERE poetry_genre = %s",( condition,))
                resultset = cursor.fetchall()

                for row in resultset:
                    guest = Guest(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                    guests.append(guest.to_JSON())

            connection.close()
            return guests
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_age(self, age):

        try:
            connection = get_connection()
            guests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, carnet, complete_name, address, gender, phone, date_of_birth, guest_age, student_career, poetry_genre, enrollment_date, presentation_date FROM guest WHERE guest_age = %s",( age,))
                resultset = cursor.fetchall()

                for row in resultset:
                    guest = Guest(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                    guests.append(guest.to_JSON())

            connection.close()
            return guests
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def get_by_presentation_date(self, date):

        try:
            connection = get_connection()
            guests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, carnet, complete_name, address, gender, phone, date_of_birth, guest_age, student_career, poetry_genre, enrollment_date, presentation_date FROM guest WHERE presentation_date = %s",( date,))
                resultset = cursor.fetchall()

                for row in resultset:
                    guest = Guest(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                    guests.append(guest.to_JSON())

            connection.close()
            return guests
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def get_by_career(self, career):

        try:
            connection = get_connection()
            guests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, carnet, complete_name, address, gender, phone, date_of_birth, guest_age, student_career, poetry_genre, enrollment_date, presentation_date FROM guest WHERE student_career = %s",( career,))
                resultset = cursor.fetchall()

                for row in resultset:
                    guest = Guest(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                    guests.append(guest.to_JSON())

            connection.close()
            return guests
        except Exception as ex:
            raise Exception(ex)