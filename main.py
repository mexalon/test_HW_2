import requests


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
        href = response.json()['href']
        with open(file_name, 'rb') as f:
            response = requests.put(href, files={'file': f})
            response.raise_for_status()
            code = {response.reason: response.status_code}

        return code

    def mkdir(self, dir_name: str):
        """На всякий случай метод для создания папки"""
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources/',
                                headers={'Authorization': f'OAuth {self.token}'},
                                params={'path': dir_name})
        response.raise_for_status()
        code = {response.reason: response.status_code}
        return code


if __name__ == '__main__':
    TOKEN = '*********************************'
    source_file = 'iCdeIdjeZ2o.jpg'
    target_folder = 'my_target_folder'
    uploader = YaUploader(TOKEN)
    result = uploader.upload(source_file, target_folder)
    print(f'File {list(result.keys())[0].lower()}')











