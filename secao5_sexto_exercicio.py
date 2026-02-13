#atividade:Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos


import math
import cmath

numero = int(input("Digite um número inteiro: ")) # Ler o número e depois converte para int 
numero2 = int(input("Digite outro número inteiro: "))
diferenca = numero - numero2

if numero > numero2 : #Verificamos se o número é maior que o outro
        
    print(f"O primeiro número ({numero:.2f}), é maior que o segundo ({numero2:.2f}).")
    print(f"E sua diferença é de {diferenca}")

else:
    
    print(f"O segundo numero ({numero2:.2f}), é maior que o primeiro.")
    print(f"E sua diferença é de {diferenca}")