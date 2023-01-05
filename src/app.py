from flask import Flask
from config import configuration
from database.dbConect import db
from models.GuestModels import Guest

from routes import guest_routes

app = Flask(__name__)
app.config.from_object(configuration['config'])

db.init_app(app)


if __name__ == '__main__':
    app.register_blueprint(guest_routes.guest_routes, url_prefix='/api/show')
    app.run()