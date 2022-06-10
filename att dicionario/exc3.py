
ano_atual = 2022
pessoa = {}

pessoa['nome'] = input('nome: ')
ano_nasc = int(input('ano de nascimento: '))
pessoa['idade'] = ano_atual - ano_nasc
ctps = int(input('insira o numero da carteira de trabalho:[insira zero caso não tenha] '))
if ctps > 0:
    pessoa['ctps'] = ctps
    pessoa['ano de contratação'] = int(input('insira o ano de contratação: '))
    pessoa['salario'] = float(input('salario: '))
    pessoa['ano da aposentadoria'] = (pessoa['ano de contratação']-ano_nasc) + 35
else:
    pessoa['ctps'] = ctps
print('__'*20)
for k,v in pessoa.items():
    print(f'{k}: {v}')