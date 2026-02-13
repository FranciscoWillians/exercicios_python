#atividade:5. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.


import math
import cmath

numero = int(input("Digite um número real: ")) # Ler o número e depois converte para int 


if numero % 2 == 0 : #Verificamos se o resto da divisão é igual a zero
    
    
    print("O número é Par.")

else:
    
    print("O número é impar.")