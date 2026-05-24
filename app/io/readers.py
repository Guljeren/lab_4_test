import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Type
from app.core.models import Transaction
from app.core.exceptions import DataFormatError

class BaseReader(ABC):
    """Абстрактный базовый класс для всех читателей файлов."""
    
    @abstractmethod
    def read(self, file_path: Path) -> List[Dict]:
        """Метод, который должен реализовать каждый дочерний класс."""
        pass

class CSVReader(BaseReader):
    """Класс для чтения данных из CSV файлов."""
    def read(self, file_path: Path) -> List[Dict]:
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                # DictReader сразу превращает строку в словарь
                return list(csv.DictReader(f))
        except Exception as e:
            raise DataFormatError(f"Ошибка в структуре CSV: {e}")

class JSONReader(BaseReader):
    """Класс для чтения данных из JSON файлов."""
    def read(self, file_path: Path) -> List[Dict]:
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise DataFormatError(f"Ошибка в структуре JSON: {e}")

# --- REGISTRY PATTERN ---
# Этот словарь связывает расширение файла с нужным классом
READER_REGISTRY: Dict[str, Type[BaseReader]] = {
    '.csv': CSVReader,
    '.json': JSONReader
}

def get_reader(file_path: Path) -> BaseReader:
    """Фабричная функция для получения нужного ридера."""
    extension = file_path.suffix.lower() # Получаем .csv или .json
    reader_class = READER_REGISTRY.get(extension)
    
    if not reader_class:
        raise DataFormatError(f"Формат {extension} не поддерживается")
    
    return reader_class() # Создаем объект класса (экземпляр)
