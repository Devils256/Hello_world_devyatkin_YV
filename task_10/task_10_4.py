from typing import Any, List, Tuple

def process_samples(records: List[dict]) -> Tuple[List[dict], List[str]]:
    """
    Обрабатывает список записей с результатами анализов.

    Для каждой записи:
    - Преобразует поле "value" из строки в число с плавающей точкой.
    - Добавляет поле "quality" на основе числового значения:
        * "low" если value < 5
        * "normal" если 5 <= value <= 10
        * "high" если value > 10
    - Корректно обработанные записи сохраняются в первый список,
      ошибки — во второй.

    Args:
        records: Список словарей, каждый из которых должен содержать
                 ключи "id" (идентификатор пробы) и "value" (строковое
                 представление числа).

    Returns:
        Кортеж (processed_records, errors):
        - processed_records: список словарей с обновлёнными полями
          "value" (float) и добавленным полем "quality" (str).
        - errors: список строк с сообщениями об ошибках в формате
          "Sample <id>: <сообщение>".
    """
    processed: List[dict] = []
    errors: List[str] = []

    for record in records:
        # Пытаемся получить id и значение
        try:
            sample_id = record["id"]
            value_str = record["value"]
        except KeyError as e:
            # Если нет id или value, используем "unknown" для id
            missing_key = e.args[0]
            sample_id = record.get("id", "unknown")
            errors.append(f"Sample {sample_id}: Missing required field '{missing_key}'")
            continue

        # Преобразование value в float
        try:
            value = float(value_str)
        except ValueError as e:
            errors.append(f"Sample {sample_id}: Invalid value '{value_str}' - {e}")
            continue

        # Определение качества
        if value < 5:
            quality = "low"
        elif value <= 10:  # охватывает 5 <= value <= 10
            quality = "normal"
        else:
            quality = "high"

        # Создаём новую запись: копируем все исходные поля,
        # заменяем value на число и добавляем quality
        new_record = dict(record)
        new_record["value"] = value
        new_record["quality"] = quality
        processed.append(new_record)

    return processed, errors