import os
import json
import logging
from pathlib import Path
from app.io.readers import get_reader
from app.services.processor import DataProcessor
from app.core.exceptions import BaseAppError

logging.basicConfig(level=logging.INFO)

def save_report(processor: DataProcessor, output_path: Path):
    """Сохранение отчета с обработкой ошибок диска (для Advanced Mocking)."""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(processor.aggregated_data, f, indent=4)
    except Exception as e:
        logging.error(f"Не удалось сохранить итоговый отчет: {e.__class__.__name__}")

def main():
    data_dir = Path("data")
    if not data_dir.exists():
        return

    processor = DataProcessor()
    
    for file_name in os.listdir(data_dir):
        file_path = data_dir / file_name
        try:
            reader = get_reader(file_path)
            raw_data = reader.read(file_path)
            for row in raw_data:
                try:
                    transaction = processor.validate_row(row)
                    processor.aggregate(transaction)
                except BaseAppError:
                    pass # Пропускаем плохие строки согласно ТЗ
        except BaseAppError:
            pass # Пропускаем битые файлы
            
    save_report(processor, Path("result.json"))

if __name__ == "__main__":
    main()
