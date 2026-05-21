import json
from typing import Dict

def analyze_process_logs(jsonl_path: str, report_path: str) -> Dict[str, int]:
    """
    Анализирует JSONL-файл с событиями процесса и создаёт отчёт.

    Параметры:
        jsonl_path (str): путь к входному JSONL-файлу (поля: timestamp, level, message)
        report_path (str): путь для сохранения текстового отчёта

    Возвращает:
        Dict[str, int]: словарь с количеством событий для каждого уровня
    """
    counts = {}

    # Чтение JSONL файла
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                level = record.get('level')
                if level is not None:
                    counts[level] = counts.get(level, 0) + 1
            except json.JSONDecodeError:
                # Пропускаем некорректные строки (по условию их быть не должно)
                continue

    # Формирование отчёта
    total = sum(counts.values())
    with open(report_path, 'w', encoding='utf-8') as report:
        report.write("Process Log Report\n")
        report.write("==================\n")
        for level in sorted(counts.keys()):
            report.write(f"{level}: {counts[level]}\n")
        report.write(f"Total: {total}\n")

    return counts