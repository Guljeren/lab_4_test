"""
Модуль кастомных исключений. 
Здесь мы описываем дерево ошибок, специфичных для нашего приложения.
"""

class BaseAppError(Exception):
    """Базовый класс для всех ошибок нашего приложения."""
    pass

class DataFormatError(BaseAppError):
    """Выбрасывается, если структура файла (CSV/JSON) повреждена."""
    pass

class ValidationError(BaseAppError):
    """Выбрасывается, если данные не проходят проверку бизнес-логики (например, сумма <= 0)."""
    pass

class CurrencyMismatchError(BaseAppError):
    """Бонусная ошибка: если в одном отчете встречаются разные валюты."""
    pass

class InvalidTransactionError(ValidationError):
    """Выбрасывается при подаче абсолютно некорректных структур (мусора)."""
    pass
