SWAPI Data Collector

Скрипт на Python для сбора данных о вселенной «Звёздных войн» через публичный SWAPI API с сохранением результатов на диск.

Что делает
Запрашивает у API список доступных категорий данных (people, films, planets, species, starships, vehicles).
Для каждой категории делает отдельный запрос и сохраняет ответ в текстовый файл в папке data/.
Обрабатывает сетевые ошибки — при сбое запроса выводится сообщение, а не падение программы.
Архитектура
APIRequester — базовый класс-обёртка над requests: собирает URL из base_url и переданного пути, обрабатывает RequestException.
SWRequester(APIRequester) — наследник под конкретный API SWAPI, добавляет методы get_sw_categories() и get_sw_info(sw_type).
save_sw_data() — точка входа: создаёт директорию data/, проходит по всем категориям и сохраняет каждую в свой файл.

Технологии

Python 3, requests, pathlib, pytest (тесты).

Как запустить
bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

python3 swapi.py       # запускает сбор данных
pytest                  # прогоняет тесты
