import pytest
from unittest.mock import patch
import logging
from main import save_report

def test_disk_error_logging(processor, caplog):
    caplog.set_level(logging.ERROR)
    processor.aggregated_data = {"Test": 10.0}
    
    with patch("builtins.open", side_effect=PermissionError("No access")):
        save_report(processor, "result.json")
        
    assert any("Не удалось сохранить итоговый отчет" in record.message for record in caplog.records)
