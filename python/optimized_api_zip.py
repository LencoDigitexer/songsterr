import json
import os
import gzip

def process_json_file(input_path, output_path):
    # Проверяем, не пустой ли файл
    if os.path.getsize(input_path) == 0:
        print(f"File {input_path} is empty.")
        return

    with open(input_path, 'r') as input_file:
        try:
            data = json.load(input_file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {input_path}: {e}")
            return

    processed_data = []
    for entry in data:
        processed_entry = {
            "d": entry.get("description", ""),
            "u": entry.get("source", "").split("/")[-1].split(".")[0],
            "t": entry.get("title", ""),
            "a": entry.get("artist", "")
        }
        processed_data.append(processed_entry)

    with gzip.open(output_path, 'wt', encoding='utf-8') as output_file:
        json.dump(processed_data, output_file, indent=2)

def main():
    input_folder = "api"
    output_folder = "processed_api_zip"

    # Создаем папку 'processed_api', если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Обрабатываем каждый файл в папке 'api'
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json.gz")

        process_json_file(input_path, output_path)

if __name__ == "__main__":
    main()
