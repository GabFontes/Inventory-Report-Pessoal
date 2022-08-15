from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith('.csv') is False:
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(products)
