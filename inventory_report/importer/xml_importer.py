from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith('.xml') is False:
            raise ValueError("Arquivo inválido")
        products = list()
        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            products = [
                {element.tag: element.text for element in record}
                for record in root
            ]
        return products
