from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self._get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file(self, file_path: str, file_name_path):
        href = self._get_upload_link(disk_file_path=file_path).get('href', '')
        response = requests.put(href, data=open(file_name_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    file_name_path = 'task_2.txt'
    path_to_file_yandex = 'task_2.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload_file(path_to_file_yandex, file_name_path)
