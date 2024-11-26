def salarioVendedor():
    nome = input("Digite o nome do vendedor: ")
    salarioBase = float("Digite o salario fixo: ")
    totalVendas = float(input("Digite o total em vendas: "))

    comissao = totalVendas * 0.15

    salarioTotal = salarioBase + comissao

    print(f"O salario do vendedor {nome} é {salarioTotal:.2f}")

salarioVendedor()