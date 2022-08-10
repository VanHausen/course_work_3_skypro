import logging

from config_logger import create_logger

from flask import Flask

from bp_posts.views import main_blueprint


logger = logging.getLogger("basic")
create_logger(logger)

POST_PATH = "data.json"
STATIC_IMG_FOLDER = "/static/img"
STATIC_CSS_FOLDER = "/static/css"

app = Flask(__name__)

app.register_blueprint(main_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)

logger.info("Приложение завершается")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
