import os
import requests
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]

        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}

        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")

        #response = requests.put(href, data=open(file_path, 'rb'))
        file_size = os.stat(file_path).st_size
        with open(file_path, "rb") as f:
            with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
                wrapped_file = CallbackIOWrapper(t.update, f, "read")
                response = requests.put(href, data=wrapped_file)
                response.raise_for_status()
                if response.status_code == 201:
                    return 'OK'
                else:
                    return f'Ошибка загрузки! Код ошибки: {response.status_code}'


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:/Users/leviv/Downloads/rufus-3.20.exe'
    token = ''
    uploader = YaUploader(token)
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)