import json
import csv
import os
from pathlib import Path

def create_test_files():
    # Создаем папку data, если её нет
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # 1. Хороший JSON файл
    with open(data_dir / "dept_it.json", "w", encoding="utf-8") as f:
        json.dump([
            {"id": "IT-01", "amount": 500.50, "category": "Software", "date": "2023-10-01"},
            {"id": "IT-02", "amount": 1200.00, "category": "Hardware", "date": "2023-10-02"}
        ], f)

    # 2. Хороший CSV файл
    with open(data_dir / "dept_sales.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "amount", "category", "date"])
        writer.writerow(["S-01", "300.00", "Marketing", "2023-10-01"])
        writer.writerow(["S-02", "150.75", "Software", "2023-10-03"])

    # 3. Файл с ОШИБКОЙ (отрицательная сумма - ValidationError)
    with open(data_dir / "dept_bad_finance.json", "w", encoding="utf-8") as f:
        json.dump([
            {"id": "ERR-01", "amount": -100.00, "category": "Fraud", "date": "2023-10-01"}
        ], f)

    # 4. Файл с ОШИБКОЙ (битый формат JSON - DataFormatError)
    with open(data_dir / "broken_format.json", "w", encoding="utf-8") as f:
        f.write("[ {'id': 'B-01', 'amount': 100 ... ЧТО-ТО СЛОМАЛОСЬ ]")

    # 5. Файл с ОШИБКОЙ (пропущено поле - ValidationError)
    with open(data_dir / "missing_fields.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "category"]) # Забыли поле amount и date
        writer.writerow(["M-01", "Office"])

    print(" Тестовые файлы созданы в папке 'data/'")

if __name__ == "__main__":
    create_test_files()
