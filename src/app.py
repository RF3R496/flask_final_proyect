from flask import Flask
from config import configuration

from routes import guest_routes

app = Flask(__name__)


if __name__ == '__main__':
    app.config.from_object(configuration['config'])
    app.register_blueprint(guest_routes.guest_routes, url_prefix='/api/show')
    app.run()