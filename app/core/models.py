from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    """
    Класс-модель для одной финансовой операции.
    Использование dataclass автоматически создает методы __init__ и __repr__.
    """
    id: str          # Уникальный номер
    amount: float    # Сумма (обязательно число)
    category: str    # Категория (еда, транспорт и т.д.)
    date: str        # Дата операции