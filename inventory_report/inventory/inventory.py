from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        path_extension = path.split('.')
        file_content = []
        with open(path, encoding="utf-8") as file:
            if path_extension == 'csv':
                headers, *data = csv.reader(file, delimiter=",", quotechar='"')
                file_content = [
                    dict(zip(headers, item))
                    for item in data
                ]
            elif path_extension == 'json':
                file_content = json.load(file)
        if report_type == 'simples':
            return SimpleReport.generate(file_content)
        elif report_type == 'completo':
            return CompleteReport.generate(file_content)


print(Inventory.import_data('inventory_report/data/inventory.csv', 'simples'))
