import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exceptions import DataSourceError


class BookmarkDAO:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """ Загружает данные из JSON и возвращает список словарей """

        try:
            with open(self.path, "r", encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        return posts_data

    def _load_comments(self):
        """ Возвращает список элементов Comment """
        comments_data = self._load_data()
        comments = [Comment(**comment_data) for comment_data in comments_data]
        # for one_comment in comment_data:
        #     Comment(
        #         pk=one_comment['pk'],
        #         post_pk=one_comment['post_pk'],
        #         comment=one_comment['comment'],
        #         commenter_name=one_comment['commenter_name']
        #     )

        return comments

    def get_comment_by_post_pk(self, post_pk: int) -> list[Comment] :
        """ Получает все коментарии к определенному посту по его pk """
        comments: list[Comment] = self._load_comments()

        comments_match: list[Comment] = [c for c in comments if c.post_pk == post_pk]
        return comments_match


cd = BookmarkDAO("data/comments.json")

print(cd.get_comment_by_post_pk(2))