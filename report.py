class ReportBuilder:
    def build_report(self, processor) -> str:
        stats = processor.calculate_statistics()
        report_lines = []
        report_lines.append("=" * 50)
        report_lines.append("ОТЧЕТ")
        report_lines.append("=" * 50)
        report_lines.append("")
        report_lines.append(
            f"Общее количество записей: {len(processor.valid_records) + len(processor.invalid_records)}")
        report_lines.append(f"Количество корректных записей: {len(processor.valid_records)}")
        report_lines.append(f"Количество некорректных записей: {len(processor.invalid_records)}")
        report_lines.append("")
        report_lines.append("=" * 50)
        report_lines.append("СТАТИСТИКА:")
        report_lines.append("=" * 50)
        report_lines.append(f"Коррентных записей: {stats['Коррентных записей']}")
        report_lines.append(f"Сумма: {stats['Сумма']:.2f}")
        report_lines.append(f"Среднее значение: {stats['Среднее значение']:.2f}")
        report_lines.append(f"Минимальное значение: {stats['Минимальное значение']:.2f}")
        report_lines.append(f"Максимальное значение: {stats['Максимальное значение']:.2f}")
        report_lines.append("")
        report_lines.append("ОШИБКИ:")
        if processor.errors:
            report_lines.extend(processor.errors)
        else:
            report_lines.append("Нет ошибок")
        return "\n".join(report_lines)

    def save_report(self, report: str, output_path: str):
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
