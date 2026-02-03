#Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math
import cmath

numero_cliente = int(input("Digite um numero para saber a raiz quadrada: "))

if numero_cliente >= 0:
    
    raiz_quadrada = (math.sqrt(numero_cliente))
    
    if raiz_quadrada.is_integer():
        
        print(f"A raiz quadrada de {numero_cliente} é {int(raiz_quadrada)}")
    else:
        print(f"O número {numero_cliente} não possui raiz exata.")
else:
    print("O número é inválido, digite um número positivo")



