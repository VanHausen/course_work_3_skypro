import json
from json import JSONDecodeError

from bp_posts.dao.post import Post
from exceptions.data_exceptions import DataSourceError


class PostDAO:
    """ Менеджер постов """

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

    def _load_posts(self):
        """ Возвращает список экземпляров класса Post """

        posts_data = self._load_data()
        list_posts = [Post(**post_data) for post_data in posts_data]

        return list_posts

    def get_all(self):
        """
        Получает все посты
        :return: Список экземпляров класса Post
        """

        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        """
        Получает пост по его pk
        :return:
        """
        if type(pk) != int:
            raise TypeError(f"{pk} должен быть числом(int)")

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_content(self, substring):
        """ Ищет пост, где в контенте(content) встречается substring """

        if type(substring) != str:
            raise TypeError(f"{substring} должна быть строкой(str)")

        substring = str(substring).lower()
        posts = self._load_posts()

        match_posts = [post for post in posts if substring in post.content.lower()]

        return match_posts

    def get_by_poster(self, user_name):
        """ Ищет посты с автором """

        if type(user_name) != str:
            raise TypeError(f"{user_name} должен быть строкой(str)")

        user_name = str(user_name).lower()
        posts = self._load_posts()

        match_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return match_posts