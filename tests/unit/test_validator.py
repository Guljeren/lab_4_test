import pytest
from app.core.exceptions import ValidationError, InvalidTransactionError

@pytest.mark.parametrize("row, is_valid", [
    ({"id": "1", "amount": "100.0", "category": "Food", "date": "2023-10-10"}, True),
    ({"id": "2", "amount": "0.01", "category": "Food", "date": "2023-10-10"}, True),
    ({"id": "3", "amount": "0", "category": "Food", "date": "2023-10-10"}, False),
    ({"id": "4", "amount": "-50", "category": "Food", "date": "2023-10-10"}, False),
    ({"id": "5", "amount": "abc", "category": "Food", "date": "2023-10-10"}, False),
    ({"id": "", "amount": "10", "category": "Food", "date": "2023-10-10"}, False),
    ({"amount": "10", "category": "Food", "date": "2023-10-10"}, False),
    ({"id": "6", "category": "Food", "date": "2023-10-10"}, False),
    ({"id": "7", "amount": "10", "date": "2023-10-10"}, False),
    ({"id": "8", "amount": "10", "category": "Food"}, False),
    ({"id": "9", "amount": None, "category": "Food", "date": "2023-10-10"}, False),
])
def test_validate_row_parametrize(processor, row, is_valid):
    if is_valid:
        transaction = processor.validate_row(row)
        assert transaction.id == str(row["id"])
    else:
        with pytest.raises(ValidationError):
            processor.validate_row(row)

def test_garbage_input_raises_invalid_transaction_error(processor):
    with pytest.raises(InvalidTransactionError):
        processor.validate_row({}) # Мусор/пустая строка
