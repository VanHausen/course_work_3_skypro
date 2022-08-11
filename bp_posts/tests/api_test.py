import os

import pytest

import main

class TestApi:

    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    @pytest.fixture
    def app_instance(self):
        app = main.app
       # app.config.from_pyfile('testing.py')
        test_clients = app.test_client()
        return test_clients

    def test_all_posts_has_correct_status(self, app_instance): # All post
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

    def test_all_posts_has_correct_keys(self, app_instance): # All post
        result = app_instance.get("/api/posts", follow_redirects=True)
        list_of_posts = result.get_json()
        for post in list_of_posts:
            assert post.keys() == self.post_keys, "Неправильные ключи у полученного словаря"

    def test_single_post_has_correct_status(self, app_instance): # Single post
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200

    def test_single_post_has_404(self, app_instance): # 404
        result = app_instance.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404

    def test_single_post_has_corect_keys(self, app_instance): # 404
        result = app_instance.get("/api/posts", follow_redirects=True)
        post = result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys

    @pytest.mark.parametrize("pk", [(1), (2), (3), (4)])
    def tes_single_post_has_correct_data(self, app_instance, pk):
        result = app_instance(f"/api/posts/{pk}", follow_redirects=True)
        post = result.get_json()
        assert post["pk"] == pk, f"Неправильный pk при запросе поста {pk}"