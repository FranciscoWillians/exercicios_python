#8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.

import os
import math
import cmath

def obter_nota_valida(mensagem):
    #Solicita e valida uma nota entre 0 e 10.
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("Erro: A nota deve estar entre 0.0 e 10.0")
        except ValueError:
            print("Erro: Digite um número válido")

def calcular_media():
    """Calcula a média de duas notas válidas."""
    print("Cálculo de Média Escolar \n")
    
    nota1 = obter_nota_valida("Digite a primeira nota: ")
    nota2 = obter_nota_valida("Digite a segunda nota: ")
    
    media = (nota1 + nota2) / 2
    print(f"\nA média do aluno é {media:.2f}")

if __name__ == "__main__":
    calcular_media()
