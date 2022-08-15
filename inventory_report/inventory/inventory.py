from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import csv
import json


class Inventory:
    @staticmethod
    def get_products(path):
        products = list()

        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                products = list(csv.DictReader(
                    file, delimiter=",", quotechar='"'))

        elif path.endswith(".json"):
            with open(path) as file:
                products = json.load(file)

        elif path.endswith(".xml"):
            with open(path) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                products = [
                    {element.tag: element.text for element in record}
                    for record in root
                ]
        return products

    def import_data(path, report_type):
        products = Inventory.get_products(path)
        if report_type == 'simples':
            return SimpleReport.generate(products)
        elif report_type == 'completo':
            return CompleteReport.generate(products)
