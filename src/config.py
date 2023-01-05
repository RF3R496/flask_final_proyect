from decouple import config

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('PGSQLUSER')}:{config('PGSQLPASSWORD')}@{config('PGSQLHOST2')}/{config('PGSQLDATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



configuration = {
    'config': DevelopmentConfig
}