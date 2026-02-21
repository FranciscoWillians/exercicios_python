#9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: "Empréstimo não concedido", caso contrário imprima: "Empréstimo concedido".

import os
import math
import cmath


def obter_valores(mensagem):
    """Obtém um valor positivo do usuário."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: O valor deve ser positivo")
        except ValueError:
            print("Erro: Digite um número válido")

def verificar_emprestimo():
   #Verifica se o empréstimo pode ser concedido.
    
    print("Verificação de Empréstimo\n")
    
    # Entrada dos dados
    salario = obter_valores("Digite o salário do trabalhador: R$ ")
    prestacao = obter_valores("Digite o valor da prestação do empréstimo: R$ ")
    
    # Cálculo do limite (20% do salário)
    limite = salario * 0.20
    
    # Verificação e resultado
    print(f"\nSalário: R$ {salario:.2f}")
    print(f"Prestação: R$ {prestacao:.2f}")
    print(f"Limite (20% do salário): R$ {limite:.2f}")
    
    if prestacao > limite:
        print("\nResultado: O Empréstimo não pode ser concedido (cliente mais liso que quiabo)")
    else:
        print("\nResultado: Empréstimo concedido")

if __name__ == "__main__":
    verificar_emprestimo()
