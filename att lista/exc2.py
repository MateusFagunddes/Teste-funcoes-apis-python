continuar = ''
lista = []
while True:
    if continuar != 'n':
        valor = int(input('insira um valor: '))
        if valor not in lista:
            lista.append(valor)
            print('valor inserido com sucesso!')
        else:
            print('o valor informado já esta na lista!')
    else:
        break
    continuar = input('deseja continura?[s,n]').lower()
lista.sort()
print(f'Ao todo foram informados {len(lista)} valores válidos, aqui está a lista {lista} com seus valores formatados.')