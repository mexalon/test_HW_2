import requests
from stuff import *
from time import sleep
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_name: str, dir_name=None):
        """Метод загруджает файл file_path на яндекс диск"""
        if dir_name is not None and isinstance(dir_name, str):
            self.mkdir(dir_name)
            target_path = f'{dir_name}/{file_name}'
        else:
            target_path = file_name

        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers={'Authorization': f'OAuth {self.token}'},
                                params={'path': target_path, 'overwrite': True})
        response.raise_for_status()
        sleep(0.5)
        href = response.json()['href']
        with open(file_name, 'rb') as f:
            response = requests.put(href, files={'file': f})
            response.raise_for_status()
            code = {response.reason: response.status_code}

        return code

    def mkdir(self, dir_name: str):
        """метод для создания папки"""
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources/',
                                headers={'Authorization': f'OAuth {self.token}'},
                                params={'path': dir_name})
        sleep(1)
        code = {response.reason: response.status_code}
        return code

    def get_dir(self, dir_name: str):
        """метод для получения информации папки"""
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/',
                                headers={'Authorization': f'OAuth {self.token}'},
                                params={'path': dir_name})

        sleep(1)
        code = {response.reason: response.status_code}
        return code

    def del_dir(self, dir_name: str):
        """метод для удаления файла или папки"""
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources/',
                                headers={'Authorization': f'OAuth {self.token}'},
                                params={'path': dir_name})

        sleep(1)
        code = {response.reason: response.status_code}
        return code



if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    result = uploader.upload(source_file, target_folder)
    print(f'File {list(result.keys())[0].lower()} code {list(result.values())[0]}')











