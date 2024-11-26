#leia o salario do funcionario e calcule e mostre o novo salário.
def main():

    print("Digite o valor do seu salario atual: ")
    salarioAtual = float(input())

    #Definição de ajustes
    if salarioAtual <= 400.00:
        percentual = 15
    elif salarioAtual <= 800.00:
        percentual = 12
    elif salarioAtual <= 1200.00:
        percentual <= 10
    elif salarioAtual <= 2000.00:
        percentual = 7
    else:
        percentual = 4

    reajuste = salarioAtual * (percentual / 100)
    novoSalario = salarioAtual + reajuste

    # Mostrar o calculo do novo salario

    print(f"O novo salário é: {novoSalario:.2f}")
    print(f"O reajuste foi de: {reajuste:.2f}")
    print(f"O percentual ganho foi de: {percentual}%")

main()

