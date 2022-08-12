from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        000,
        "Cachaça",
        "Bar do seu Zé",
        "03/03/2003",
        "03/03/2013",
        "333",
        "...",
    )

    string = 'O produto Cachaça fabricado em '\
        '03/03/2003 por Bar do seu Zé com validade até '\
        '03/03/2013 precisa ser armazenado ....'

    message = False

    if string in str(product.__repr__):
        message = True

    assert message is True
