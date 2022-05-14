# Programa que colete os dados de sexo (0-feminino, 1-masculino), idade e altura de 20 pessoas
# e mostre as seguintes informações:
# a) média da idade do grupo coletado;
# b) média da altura das mulheres;
# c) média da idade dos homens;
# d) percentual de pessoas com idade entre 18 e 35 anos (inclusive).
# Por Yuri Monzini!

#eu vi em um video o cara explicando que posso declarar todas as variaveis em uma unica linha
#caso fosse todos com o mesmo resultado como nessa linha abaixo que todos são "=0"
somaI = medG = medH = medAM = porc_18_35 = idadeM = sxh = idh = altM = alM = 0
for gruP in range(1, 21): #aqui é a quantidade de pessoas que vai ter no loop (sempre contando -1)
    print('**** {}ª Pessoa ****'.format(gruP)) #essa linha é só para demonstrar em qual pessoa você já está no cadastro
    idade = int(input('Idade: ')) #-----------
    sexo = str(input('Sexo [M/F]: ')).strip()#Nestas linhas são para a capitura das informações do grupo
    altura = int(input('Altura em cm: '))#----
    somaI += idade #-----
    if sexo in 'Mm': #---
        idadeM += idade #calculo para fazer a média da idade do grupo
    if sexo in 'Mm': #Calculo para a média de idade dos Homens
        idh += 1
    if idade >= 18 <= 35: #soma de quantas pessoas tem no grupo com as idades entre 18 a 35 anos
        porc_18_35 += 1
    if sexo in 'Ff':  #calculando a media da altura das mulheres
        altM += altura
        alM += 1

medAM = altM / alM  #calculo final média da altura das mulheres
medH = idadeM / idh #calculo final média idade dos homens
medG = somaI / gruP #calculo final édia idade do grupo
print(f'A média da idade do grupo: {medG} anos')
print(f'A média da altura em cm das mulheres é de: {medAM}cm')
print(f'A média da idade dos homens é: {medH} anos')
print(f'Total de pessoas com idade entre 18 a 35 anos é de: {porc_18_35}')


