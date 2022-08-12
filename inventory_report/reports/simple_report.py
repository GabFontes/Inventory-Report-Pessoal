from datetime import datetime

class SimpleReport:
    def __init__(
        self,
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    ):
        self.id = id
        self.nome_do_produto = nome_do_produto
        self.nome_da_empresa = nome_da_empresa
        self.data_de_fabricacao = str(data_de_fabricacao)
        self.data_de_validade = str(data_de_validade)
        self.numero_de_serie = numero_de_serie
        self.instrucoes_de_armazenamento = instrucoes_de_armazenamento

    def get_oldest_manufacturing_date(list):
        # how to convert string to date
        # https://www.google.com/search?q=how+to+convert+string+to+date+python&oq=how+to+convert+string+to+date&aqs=chrome.6.69i57j0i512l7.23065j0j4&sourceid=chrome&ie=UTF-8
       
        dts = []
        for dt in list:
            dts.append(datetime.strptime(dt["data_de_fabricacao"], "%Y-%m-%d"))
        return min(dts).date()

    def get_company_with_more_products(list):
        # find the item with maximum occurrences in a list
        # https://stackoverflow.com/questions/6987285/find-the-item-with-maximum-occurrences-in-a-list
        
        companies = []
        for item in list:
            companies.append(item["nome_da_empresa"])
        return max(companies, key=companies.count)

    def get_closest_expiration_date(list):
        now = datetime.now()
        dts = []
        for dt in list:
            if datetime.strptime(dt["data_de_validade"], "%Y-%m-%d") > now:
                dts.append(datetime.strptime(
                    dt["data_de_validade"], "%Y-%m-%d"))
        return min(dts).date()

    def generate(products):
        oldest_manufacturing_date = SimpleReport.get_oldest_manufacturing_date(products)
        company_with_more_products = SimpleReport.get_company_with_more_products(products)
        closest_expiration_date = SimpleReport.get_closest_expiration_date(products)

        return f"""Data de fabricação mais antiga: {oldest_manufacturing_date}
Data de validade mais próxima: {closest_expiration_date}
Empresa com mais produtos: {company_with_more_products}"""
