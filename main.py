import sys
from processor import DataProcessor
from report import ReportBuilder


def main():
    if len(sys.argv) < 3:
        print("Пример использования: python main.py <input_file> <output_file>")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    processor = DataProcessor(delimiter=";")
    processor.process(input_file)
    report_builder = ReportBuilder()
    report = report_builder.build_report(processor)
    print(report)
    report_builder.save_report(report, output_file)


if __name__ == "__main__":
    main()


