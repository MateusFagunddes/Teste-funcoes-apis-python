
def contador(inicio, fim , passo):
    if passo != 0:
        if passo < 0 and inicio > fim:
            for i in range(inicio, fim, passo):
                print(i, end=" ")
            
        if inicio > fim :
            for i in range(inicio, fim, -passo):
                print(i, end=" ")

        else:
            for i in range(inicio, fim, passo):
                print(i, end=" ")
    else:
        print('numero de progressão não pode ser zero!')



inicio  = int(input('insira um valor para iniciar: '))
fim= int(input('insira um valor para terminar: '))
passo = int(input('insira um valor para a progressão: '))

contador(inicio, fim, passo)