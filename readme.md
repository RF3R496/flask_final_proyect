structure of database table

create table guest(
	id VARCHAR(36) primary key,
	carnet VARCHAR(6) not null,
	complete_name VARCHAR(100) not null,
	address VARCHAR(75) not null,
	gender VARCHAR(20) not null,
	phone character(15) not null,
	date_of_birth date not null,
	guest_age integer not null,
	student_career VARCHAR(50) not null,
	poetry_genre VARCHAR(20) not null,
	enrollment_date date,
	presentation_date date
)

structure of .env file

SECRET_KEY = 
PGSQLHOST = 
PGSQLPORT = 
PGSQLUSER = 
PGSQLPASSWORD = 
PGSQLDATABASE = 

structure of json to make request on localhost:5000/api/show/register with POST method for register an guest
{
    "carnet": "carnet",
    "complete_name": "complete name" ,
    "address": "address",
    "gender": "gender" ,
    "phone": "pone number" ,
    "date_of_birth":"year-month-day",
    "student_career":"career student",
    "poetry_genre":"poetry genre (Lyric, Drama, Epic)"
}

