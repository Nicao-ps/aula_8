product = {
    'name': 'Notebook',
    'price': 3500.00,
    'stock': 15
}
print(product)

product.pop(str(input('Informe a chave que deseja excluir: ')))
print('A chave foi excluída.')
for pkeys in product.keys():
    print(pkeys)

product['price'] = 4000.00
print(product['name'], '= R$ '+'{:.2f}'.format(product['price']))
