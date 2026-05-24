import pytest
from app.services.processor import DataProcessor

@pytest.fixture
def processor():
    """
    Фикстура для создания объекта DataProcessor перед каждым тестом.
    Это позволяет не писать 'processor = DataProcessor()' в каждом тесте.
    """
    return DataProcessor()
