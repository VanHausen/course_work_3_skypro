import pytest

from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO


def check_fields(post):
    fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


class TestPostsDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO("bp_posts/tests/data_test.json")
        return post_dao_instance

# Функция получения всех

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, "Некорректный тип для result"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "Некорректный тип для result(одиночный результат)"

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_all()

        correct_pks = {1, 2, 3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Не совпадают полученные id"

    ### Функция получения одного по pk

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, "Некорректный тип для result(одиночный результат)"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_by_pk(666)
        assert post is None, "None"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, f"Некорректный пост"

    ### Функция получения постов по имени автора

    def test_search_content_types(self, post_dao):
        posts = post_dao.search_content("ага")
        assert type(posts) == list, "Некорректный тип для result"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "Некорректный тип для result(одиночный результат)"

    def test_search_content_fields(self, post_dao):
        posts = post_dao.search_content("ага")
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_search_content_not_found(self, post_dao):
        posts = post_dao.search_content("66666666666666")
        assert posts == [], "Может [] не найдена в посте"

    @pytest.mark.parametrize("s, expected_pks", [
        ("Ага", {1}),
        ("Вышел", {2}),
        ("на", {1, 2, 3})
    ])
    def test_search_content_result(self, post_dao, s, expected_pks):
        posts = post_dao.search_content(s)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"Некорректный результат поиска для {s}"
