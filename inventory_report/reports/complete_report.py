from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
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
        super().__init__(
            id,
            nome_do_produto,
            nome_da_empresa,
            data_de_fabricacao,
            data_de_validade,
            numero_de_serie,
            instrucoes_de_armazenamento,
        )

    def get_products_stocked_by_company(products):
        companies = dict()
        for product in products:
            company = product["nome_da_empresa"]
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1

        product_by_company = []
        for key, value in companies.items():
            product_by_company.append(f"""- {key}: {value}\n""")
        return f'{"".join(item for item in product_by_company)}'

    def generate(products):
        simple_report = SimpleReport.generate(products)
        products_by_company = CompleteReport.get_products_stocked_by_company(
            products)
        return f"""{simple_report}
Produtos estocados por empresa:
{products_by_company}"""


p = CompleteReport.generate([
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    }
])
print(p)
