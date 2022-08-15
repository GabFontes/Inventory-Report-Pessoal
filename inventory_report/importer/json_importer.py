from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith('.json') is False:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            products = json.load(file)
            return products
