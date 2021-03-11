import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        self.file_path = file_path
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params = {'path': os.path.basename(self.file_path)},
                                headers = {'Authorization': 'OAuth ' + self.token})
        href = response.json()['href']
        with open(self.file_path, 'rb') as f:
            requests.put(href, files={'file': f})
            print('Файл успешно загружен')


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('c:\my_folder\file.txt')

