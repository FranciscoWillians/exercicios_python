#atividade: 4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:

#O número digitado ao quadrado

#A raiz quadrada do número digitado



import math

numero = float(input("Digite um número real: "))# Ler o número e depois converte para float (número real)


if numero >= 0: #Verificamos se é positivo
    raiz = math.sqrt(numero)
    quadrado = numero ** 2
    
    
    print(f"O número é positivo. A raiz quadrada é {raiz:.2f}")   #2f serve para mostrar apenas 2 casas decimais
    print(f"E seu resultado ao quadradro é {quadrado:.2f}")

else:
    
    print(f"O número é negativo. Digite um número positivo")