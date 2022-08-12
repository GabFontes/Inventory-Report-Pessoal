from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        000,
        "Cachaça",
        "Bar do seu Zé",
        "03/03/2003",
        "03/03/2013",
        "333",
        "...",
    )
    assert product.id == 000
    assert product.nome_do_produto == "Cachaça"
    assert product.nome_da_empresa == "Bar do seu Zé"
    assert product.data_de_fabricacao == "03/03/2003"
    assert product.data_de_validade == "03/03/2013"
    assert product.numero_de_serie == "333"
    assert product.instrucoes_de_armazenamento == "..."
