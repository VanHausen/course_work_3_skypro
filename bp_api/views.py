import logging
from os import abort

from flask import Blueprint, jsonify, abort

from bp_posts.dao.post import Post
from bp_posts.views import post_dao

api_logger = logging.getLogger("api_logger")

bp_api = Blueprint('bp_api', __name__)


@bp_api.route('/posts/')
def api_posts_all():
    """ Эндпоинт для всех постов """
    all_posts: list[Post] = post_dao.get_all()
    all_posts_as_dicts: list[dict] = [post.as_dict() for post in all_posts]
    api_logger.debug("Запрошены все посты")
    return jsonify(all_posts_as_dicts), 200


@bp_api.route('/posts/<int: pk>')
def api_posts_single(pk: int):
    """ Эндпоинт для одного поста """
    post: Post | None = post_dao.get_by_pk(pk)
    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)
    api_logger.debug(f"Запрошен пост {pk}")
    return jsonify(post.as_dict()), 200

@bp_api.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка {error}")
    return jsonify({"error": str(error)}), 404


@bp_api.route('/')
def api_posts_hello():
    return "Это api. Доступные эндпоинты - api/posts и api/posts/pk." \
            "Смотри документацию на github."

















