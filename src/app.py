from flask import Flask
from config import configuration

app = Flask(__name__)


if __name__ == '__main__':
    app.config.from_object(configuration['config'])
    app.run()