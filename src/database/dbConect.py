import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQLHOST'),
            user=config('PGSQLUSER'),
            password=config('PGSQLPASSWORD'),
            database=config('PGSQLDATABASE')
        )
    except DatabaseError as error:
        raise error