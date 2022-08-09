import logging

from config_logger import create_logger

create_logger()

from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk

from flask import Flask

from main import main_blueprint

logger = logging.getLogger("basic")

POST_PATH = "data.json"
STATIC_IMG_FOLDER = "/static/img"
STATIC_CSS_FOLDER = "/static/css"

app = Flask(__name__)

app.register_blueprint(main_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)

logger.info("Приложение завершается")

app.run(host='127.0.0.2', port=80)
