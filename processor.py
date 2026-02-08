from typing import List, Tuple
from models import Record


class DataProcessor:
    def __init__(self, delimiter: str = ";"):
        self.delimiter = delimiter
        self.valid_records: List[Record] = []
        self.invalid_records: List[str] = []
        self.errors: List[str] = []

    def read_file(self, file_path: str) -> List[str]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            raise Exception(f"Файл не найден: {file_path}")
        except Exception as e:
            raise Exception(f"Ошибка чтения: {str(e)}")

    def validate_line(self, line: str, line_number: int) -> Tuple[bool, Record | None]:
        parts = line.strip().split(self.delimiter)
        if len(parts) != 3:
            self.errors.append(
                f"На строке {line_number}: неверное количество полей"
            )
            return False, None
        raw_id, name, raw_value = parts
        if not raw_id or not name or not raw_value:
            self.errors.append(
                f"Строка {line_number} пустая"
            )
            return False, None
        try:
            record_id = int(raw_id)
        except ValueError:
            self.errors.append(
                f"На строке {line_number}: ID должен быть integer"
            )
            return False, None
        try:
            value = float(raw_value)
        except ValueError:
            self.errors.append(
                f"На строке {line_number}: Value должен быть float"
            )
            return False, None
        return True, Record(record_id, name, value)

    def process(self, file_path: str):
        lines = self.read_file(file_path)
        for i, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            is_valid, record = self.validate_line(line, i)
            if is_valid:
                self.valid_records.append(record)
            else:
                self.invalid_records.append(line.strip())

    def calculate_statistics(self):
        if not self.valid_records:
            return {
                "Коррентных записей": 0,
                "Сумма": 0,
                "Среднее значение": 0,
                "Минимальное значение": 0,
                "Максимальное значение": 0,
            }
        values = [r.value for r in self.valid_records]
        return {
            "Коррентных записей": len(values),
            "Сумма": sum(values),
            "Среднее значение": sum(values) / len(values),
            "Минимальное значение": min(values),
            "Максимальное значение": max(values),
        }
