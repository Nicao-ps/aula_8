def cadastra_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = input('Informe o valor da venda: ')
        cadastro = {
            'name': nome,
            'price': valor,
        }
    lst_cadastro.append(cadastro)


lst_cadastro = []

qtd = int(input('Quantas pessoas? '))
cadastra_pessoa(qtd)
print(lst_cadastro)
