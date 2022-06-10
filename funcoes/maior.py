def maior(*num):
    contador = maior=0 
    for i in range(0,len(num)):
        
        if num[i] > maior:
            maior = num
            contador = i
        contador+=1
        print(f'foram lidos um total de {contador} numeros, sendo o maior {maior}')



maior(1,2,3,4,5,6)


