def validate_data(df):
    """Проверяет корректность данных."""
    errors = []
    if 'planned' not in df.columns or 'actual' not in df.columns:
        errors.append("Отсутствуют обязательные колонки 'planned' и/или 'actual'")
    if df.isnull().values.any():
        errors.append("Обнаружены пропущенные значения")
    is_valid = len(errors) == 0
    return {'is_valid': is_valid, 'errors': errors}
