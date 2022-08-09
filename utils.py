
from flask import json

import logging

logger = logging.getLogger("basic")


def get_posts_all() -> list[dict]:# Возвращает посты
    with open('data.json', 'r', encoding='utf-8') as file:
        logger.debug("Функция get_posts_all вызвана")
        return json.load(file)


def get_posts_by_user(user_name: str) -> list[dict]: # Возвращает посты определенного пользователя.
    try:
        result = []
        for post in get_posts_all():
            if user_name.lower() in post['poster_name'].lower():
                result.append(post)
        logger.debug("Функция get_posts_by_user вызвана")
        return result
    except ValueError:
        print("Такого поста нет!")


def get_comments_by_post_id(post_id: int) -> list[dict]: # Возвращает комментарии определенного поста.
    try:
        with open('comments.json', 'r', encoding='utf-8') as file:
            json.load(file)
        result = []
        for post in get_posts_all():
            if post_id in post['post_id']:
                result.append(post)
        logger.debug("Функция get_comments_by_post_id вызвана")
        return result
    except ValueError:
        print("Такого поста нет!")



def search_for_posts(query: list) -> list[dict]: # Возвращает список постов по ключевому слову
    result = []
    for post in get_posts_all():
        if query in post["content"]:
            result.append(post)
    logger.debug("Функция search_for_posts вызвана")
    return result


def get_post_by_pk(pk: list) -> int: # Возвращает один пост по его идентификатору
    for post in get_posts_all():
        if pk in post["pk"]:
            result = int(post["pk"])
    logger.debug("Функция get_post_by_pk вызвана")
    return result