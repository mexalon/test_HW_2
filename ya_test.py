from stuff import *
from main import YaUploader


def rc(code):
    """read code"""
    return list(code.values())[0]


class TestYaD:

    def setup_class(self):
        self.token = TOKEN
        self.uploader = YaUploader(self.token)
        self.uploader.mkdir('some_random_dir')

    def teardown_class(self):
        """подчищаем созданные"""
        self.uploader.del_dir('some_random_dir')
        self.uploader.del_dir('new_shiny_dir')

    def test_get_dir(self):
        """проверка метода проверки папки"""
        code = self.uploader.get_dir('some_random_dir')
        assert rc(code) == 200

    def test_mkdir(self):
        """проверка метода создания папки"""
        code = self.uploader.mkdir('new_shiny_dir')
        assert rc(code) == 201

    def test_get_new_dir(self):
        """проверка что папка действительно создана"""
        code = self.uploader.get_dir('new_shiny_dir')
        assert rc(code) == 200

    def test_exist_dir(self):
        """проверка создания существующей папки"""
        code = self.uploader.mkdir('new_shiny_dir')
        assert rc(code) == 409

    def test_bad_dir_name(self):
        """проверка создания некорректной папки"""
        code = self.uploader.mkdir('')
        assert rc(code) == 400

    def test_bad_token(self):
        """проверка создания папки без авторизации"""
        bad_uploader = YaUploader('bad_token')
        code = bad_uploader.mkdir('bad_dir')
        assert rc(code) == 401

