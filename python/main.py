import os
import requests
from threading import Thread

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

    # Запускаем несколько потоков для параллельного скачивания
    threads = []
    for i in range(1, 571521):
        thread = Thread(target=download_json, args=(i,))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
