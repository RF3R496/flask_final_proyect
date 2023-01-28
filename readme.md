# Technical Test
                

Esto es una prueba técnica de creación de una API con Flask y PostgreSQL. En este caso encontraran dos ramas:
-  **main** utilizando Psycopg2.
-  **withSqlAl** utilizando el ORM SQLAlchemy instegrado en Flask.

####Requerimientos

#####Paquetes necesarios

Para instalar los paquetes necesarios utiliza:

`$ pip install -r requirements.txt`

Ten en cuenta que las ramas requieren diferentes paquetes por lo tanto el contenido del archivo *requirements.txt*  es distinto en las ramas.

#####Archivo env


Con el fin de tener privacidad a la hora de conectarnos a la base de datos utlizamos un archivo especial *.env* en el directorio principal para guardar datos privados y acceder a ellos por medio de *python-decouple*, necesitamos lo siguente(ejemplos):

Rama **main**:

```
SECRET_KEY = qwerty
PGSQLHOST = localhost
PGSQLPORT = 5432
PGSQLUSER = username
PGSQLPASSWORD = qwerty2
PGSQLDATABASE = example

```
Rama **withSqlAl**
```
SECRET_KEY =  qwerty
PGSQLHOST2 = localhost:5432
PGSQLUSER = username
PGSQLPASSWORD = qwerty2
PGSQLDATABASE = example

```

#####Base de Datos

En la base de datos necesitaremos la siguiente estructura en PostgreSQL:

Rama **main**

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

Rama **withSqlAl**

Necesitamos utilizar la funcion de *create_all()* de *Flask-SqlAlchemy*.

------------


------------


####Peticiones
#####POST
Lo utilizaremos para el regiistro la siguiente ruta:

` localhost:5000/api/show/register`

Y la siguiente estructura JSON(ejemplo):
``` 
{ 
	"carnet": "A05ty3",
	"complete_name": "Guillermo Gustavo Guerra Guilla" ,
	"address": "San Pablo, San Marcos, Guatemala", 
	"gender": "Masculinoi" , 
	"phone": "12345678" ,
	"date_of_birth":"2000-02-30", 
	"student_career":"Electronica",
	"poetry_genre":"Lyric"
}
```
#####Observaciones
**carnet** : Longitud de 6 caracteres, el primero tendrá que ser una 'A' mayúscula, el tecero un '5' y el último entre ('1', '3' 0 '9').

**phone**: De longitud no mayor a 15 números.

**date_of_birth**: Debe tener el siguiente formato "Año-Mes-Dia"

**poetry_genre***: Deberá estar entre los siguientes valores  (Lyric, Drama, Epic)

#### GET
##### Obtener todos los registros
`localhost:5000/api/show/all`

##### Obtener por genero de Poesía
`localhost:5000/api/show/search/poetry-genre/<poetry-genre>`

##### Obtener por Edad
`localhost:5000/api/show/search/age/<age>`


##### Obtener por carrera del estudiante
`localhost:5000/api/show/search/career/<student_career>`
