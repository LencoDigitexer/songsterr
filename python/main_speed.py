import os
import requests
from concurrent.futures import ThreadPoolExecutor

def download_json(i):
    url = f"https://www.songsterr.com/api/meta/{i}/revisions"
    filename = f"api/{i}.json"

    try:
        # Проверяем, существует ли файл
        if os.path.exists(filename):
            print(f"File {filename} already exists.")
            return

        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса

        # Сохраняем JSON в файл
        with open(filename, 'w') as file:
            file.write(response.text)

        print(f"File {filename} downloaded successfully.")
    except requests.exceptions.RequestException as req_exc:
        print(f"Request error for file {filename}: {req_exc}")
    except Exception as e:
        print(f"Error for file {filename}: {e}")

def main():
    # Создаем папку 'api', если её нет
    if not os.path.exists("api"):
        os.makedirs("api")

    # Используем ThreadPoolExecutor для параллельного скачивания
    max_threads = 500  # Вы можете увеличить это значение в зависимости от вашего желаемого количества потоков
    with ThreadPoolExecutor(max_threads) as executor:
        # Запускаем несколько потоков для параллельного скачивания
        for i in range(12000, 571521):
            executor.submit(download_json, i)

if __name__ == "__main__":
    main()
