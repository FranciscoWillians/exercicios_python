#Os Números Reais (representados pelo símbolo $\mathbb{R}$) são, de forma simplificada, todos os números que você consegue localizar em uma reta numérica contínua.


#atividade: Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.

import math

numero = float(input("Digite um número real: "))# Ler o número e depppois converte para float (número real)


if numero >= 0: #Verificamos se é positivo
    raiz = math.sqrt(numero)
    
    print(f"O número é positivo. A raiz quadrada é {raiz:.2f}")   #2f serve para mostrar apenas 2 casas decimais


else:
    quadrado = numero ** 2
    print(f"O número é negativo. O quadrado dele é {quadrado:.2f}")