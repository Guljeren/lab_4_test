import json
from app.io.readers import CSVReader

def test_csv_integration_with_bad_rows(tmp_path, processor):
    # Arrange: создаём временный CSV с 1 хорошей и 2 плохими строками
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    csv_file = data_dir / "test.csv"
    
    csv_content = (
        "id,amount,category,date\n"
        "good1,100.5,Food,2023-10-10\n"
        "bad1,0,Zero,2023-10-10\n"          # сумма 0 -> невалидно
        "bad2,-50,Negative,2023-10-10\n"     # отрицательная сумма -> невалидно
    )
    csv_file.write_text(csv_content)
    
    # Act: читаем, валидируем, агрегируем
    reader = CSVReader()
    raw_data = reader.read(csv_file)
    for row in raw_data:
        try:
            transaction = processor.validate_row(row)
            processor.aggregate(transaction)
        except Exception:
            # плохие строки игнорируем (как в main.py)
            pass
    
    # Сохраняем результат в JSON (как в main.py)
    result_path = tmp_path / "result.json"
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(processor.aggregated_data, f, indent=4)
    
    # Assert: проверяем, что в JSON только одна запись (Food)
    with open(result_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert len(data) == 1           # только одна категория
    assert data.get("Food") == 100.5