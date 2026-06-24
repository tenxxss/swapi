from pathlib import Path
import requests


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, addition=''):
        url = f'{self.base_url}{addition}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):
    def __init__(self, base_url='https://swapi.dev/api'):
        super().__init__(base_url)

    def get_sw_categories(self):
        response = self.get('/')
        data = response.json()
        return data.keys()

    def get_sw_info(self, sw_type):
        response = self.get(f'/{sw_type}/')
        return response.text


def save_sw_data():
    directory = Path('data')
    directory.mkdir(exist_ok=True)
    requester = SWRequester('https://swapi.dev/api')
    categories = requester.get_sw_categories()

    for category in categories:
        try:
            data_str = requester.get_sw_info(category)
            file_path = f'data/{category}.txt'

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data_str)
            print(f'Категория {category} сохранена.')
        except Exception:
            print(f'Ошибка при сохранении категории {category}')


if __name__ == '__main__':
    save_sw_data()
