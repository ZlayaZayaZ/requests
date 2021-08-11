import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, name_file, path_to_file=''):
        if path_to_file == '':
            path_to_file = os.path.join(os.getcwd(), name_file)
        api_base_url = 'https://cloud-api.yandex.net/'
        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {self.token}'
        }
        path_files = requests.get(api_base_url + 'v1/disk/resources/upload', params={'path': '/images/' + name_file},
                                  headers=headers)
        upload_url = path_files.json()['href']
        r = requests.put(upload_url, headers=headers, files={'file': open(path_to_file, 'rb')})
        return 'Файл загружен'

    def upload_folder(self, name_folder):
        path_folder = os.path.join(os.getcwd(), name_folder)
        list_file = os.listdir(path_folder)
        for file in list_file:
            path_file = os.path.join(os.getcwd(), name_folder, file)
            self.upload(file, path_file)
        return 'Папка загружена'


if __name__ == '__main__':
    'Получить токен от пользователя и имя загружаемого файла или папки с файлами'
    token = ...
    name_folder = ...
    name_file = ...
    uploader = YaUploader(token)
    result1 = uploader.upload_folder(name_folder)
    result2 = uploader.upload(name_file)
    print(result1)
    print(result2)