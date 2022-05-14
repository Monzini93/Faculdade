#Códio para ler 10 Valores inteios e positivos e:
#A)Encontre o maior valor;
#B)Encontre o menor valor;
#C)Calcule a média dos números lidos;
#Por Yuri Monzini

list_num = [] #variavel lista
maior = menenor = soma_list = media = 0 #variaveis
for cont in range(0, 10): #variavel para loop
    list_num.append(int(input(f'Digite o {cont+1}º número: ')))
    if cont == 0:
        maior = menor = list_num[cont] #aqui foi como vi em varios lugares para fazer
        # para que precisace fazer gambiarra de "menor = 9999"
    else: #listando as variaveis maior e menor para pegar seus respectivos valores
        if list_num[cont] > maior:
            maior = list_num[cont]
        if list_num[cont] < menor:
            meneor: int = list_num[cont]
soma_list = sum(list_num)
media = soma_list / len(list_num)
print('*-' * 20, end="*") #linha visual de separação
print() #coloquei esse pq a linha de baixos esta ficando junto da linha de sima
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'A média entre os números é: ', media)
print('*-' * 20, end="*") #linha visual de separação
