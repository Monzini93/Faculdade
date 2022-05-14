#Programa cálculo de Fatorial.
#Por Yuri Monzini

#calculo de fatorial negativo
Num = int(input("Qual o número para Fatorar: ")) #Num = Var para "Número"
#inico do contador
Fact=1 #Fatorial = var para Fatorial
Calc=1 #Calculo = var para Calculo
#Inicio do calculo
while Calc <= Num:
   Fact *= Calc
   Calc +=1
#Final do programa, apresentação do calculo
print("O fatorial do",Num, "é", Fact)

