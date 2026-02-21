#7. Faça um programa que receba dois números e mostre o maior. Se por acaso os dois números forem iguais, imprima a mensagem "Números iguais".

import os
import math
import cmath

numero = int(input("Digite um número inteiro: ")) # Ler o número e depois converte para int 
numero2 = int(input("Digite outro número inteiro: "))
diferenca = numero - numero2

if numero > numero2 : #Verificamos se o número é maior que o outro
        
    print(f"O primeiro número ({numero:.2f}), é maior que o segundo ({numero2:.2f}).")
    print(f"E sua diferença é de {diferenca}")
    
elif numero == numero2 :
    print ("Os dois numeros são iguais")
    
    pass

else:
    
    print(f"O segundo numero ({numero2:.2f}), é maior que o primeiro.")
    print(f"E sua diferença é de {diferenca}")