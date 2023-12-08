import json
import os

def process_json_file(input_path, output_path):
    try:
        with open(input_path, 'r') as input_file:
            data = json.load(input_file)
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON in file {input_path}: {e}")
        return

    processed_data = []
    for entry in data:
        processed_entry = {
            "d": entry.get("description", ""),
            "u": entry.get("source", ""),
            "t": entry.get("title", ""),
            "a": entry.get("artist", "")
        }
        processed_data.append(processed_entry)

    with open(output_path, 'w') as output_file:
        json.dump(processed_data, output_file, indent=2)

def main():
    input_folder = "api"
    output_folder = "processed_api"

    # Создаем папку 'processed_api', если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Обрабатываем каждый файл в папке 'api'
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        process_json_file(input_path, output_path)

if __name__ == "__main__":
    main()
