from typing import List, Dict, Any
from app.core.models import Transaction
from app.core.exceptions import ValidationError, InvalidTransactionError


class DataProcessor:
    """Класс для проверки данных и их трансформации."""

    def __init__(self):
        # Здесь мы будем хранить итоговые суммы по категориям
        self.aggregated_data: Dict[str, float] = {}

    # Замените метод validate_row в вашем processor.py на этот:
    def validate_row(self, row: Dict[str, Any]) -> Transaction:
        if not isinstance(row, dict) or not row:
            raise InvalidTransactionError("Передан пустой объект или мусор")
        
        required_fields = ['id', 'amount', 'category', 'date']
        for field in required_fields:
            if field not in row or row[field] is None or str(row[field]).strip() == "":
                raise ValidationError(f"Отсутствует обязательное поле: {field}")

        try:
            amount = float(row['amount'])
        except (ValueError, TypeError):
            raise ValidationError(f"Сумма '{row['amount']}' не является числом")

        if amount <= 0:
            raise ValidationError(f"Недопустимая сумма: {amount} (должна быть > 0)")
        
        return Transaction(
            id=str(row['id']),
            amount=amount,
            category=str(row['category']),
            date=str(row['date'])
    )
        
    def aggregate(self, transaction: Transaction):
        """Добавляет сумму транзакции в общую копилку по категориям."""
        cat = transaction.category
        if cat not in self.aggregated_data:
            self.aggregated_data[cat] = 0.0
        self.aggregated_data[cat] += transaction.amount
