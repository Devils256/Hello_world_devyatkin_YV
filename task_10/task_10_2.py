def parse_config(text: str) -> dict:
    """
    Парсит текстовую конфигурацию формата KEY=VALUE.
    Игнорирует пустые строки и комментарии (начинающиеся с #).
    Разделяет только по первому символу '='.
    Возвращает словарь с ключами и значениями (тип str).
    """
    config = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' not in line:
            # По условию такого быть не должно, но на всякий случай пропускаем
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
        config[key] = value
    return config