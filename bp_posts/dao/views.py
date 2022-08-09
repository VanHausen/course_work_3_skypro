import os
from os import abort

from flask import Blueprint, render_template, request

from bp_posts.dao.bookmark_dao import BookmarkDAO
from bp_posts.dao.comment import Comment
from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# Создаем объекты доступа к данным
DATA_PATH_POSTS = os.path.join("../../data", "data.json")
DATA_PATH_COMMENTS = os.path.join("../../data", "comments.json")
#DATA_PATH_BOOKMARKS = os.path.join("../../data", "bookmarks.json")
post_dao = PostDAO("DATA_PATH_POSTS")
comments_dao = CommentDAO("DATA_PATH_COMMENTS")
#bookmarks_dao = BookmarkDAO("DATA_PATH_BOOKMARKS")

@main_blueprint.route('/')
def page_posts_index():
    """ Страница всех постов """

    all_posts = post_dao.get_all()
    return render_template("posts_index.html", posts=all_posts)

@main_blueprint.route('/post/<int:pk>/')
def page_posts_single(pk):
    """ Страница одного поста """

    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comments_dao.get_comment_by_post_pk(pk)

    if post is None:
        abort(404, "Такой страницы не существует")

    return render_template("posts_single_post.html",
                           post=post,
                           comments=comments,
                           comment_len=len(comments))

@main_blueprint.route('/post/<str:user_name>/')
def page_posts_by_user(user_name: str):
    """ Возвращает посты пользователя """

    posts: list[Post] = post_dao.get_by_poster(user_name)

    if not posts:
        abort(404, "Такого пользователя не существует")

    return render_template("posts_user-feed.html",
                           posts=posts,
                           user_name=user_name
                           )

@main_blueprint.route('/search/')
def page_posts_by_user():
    """ Возвращает результаты поиска """

    query: str = request.args.get("s", "")

    if query == "":
        posts: list = []
    else:
        posts: list[Post] = post_dao.search_content(query)

    return render_template("posts_search.html",
                           posts=posts,
                           query=query,
                           post_len=len(posts)
                           )