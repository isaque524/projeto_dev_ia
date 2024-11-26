numerofuncionario = int(input("Digite o numero do funcionario "))
horasTrabalhadas = int(input("Digite as horas trabalhadas "))
valorPorHora = float(input("Digite quanto ele ganha por hora "))

salario = horasTrabalhadas * valorPorHora
 
print(f"Salario é = R$ {salario:.2f}")