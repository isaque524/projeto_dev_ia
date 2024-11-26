def codigosdePecas():
   #ler peca 1
    codigoPeca1,quantidadeDePecas1,valorUnitarioPecas1 = input("Digite o codigo, quantidade e valor da primeira peça, separados por espaço ").split()
    codigoPeca1 = int(codigoPeca1)
    quantidadeDePecas1 = int(quantidadeDePecas1)
    valorUnitarioPecas1 = float(valorUnitarioPecas1)
   
   #ler peça 2
    codigoPeca2,quantidadeDePecas2,valorUnitarioPecas2 = input("Digite o codigo, quantidade e valor da segunda peça, separados por espaço ").split()
    codigoPeca2 = int(codigoPeca2)
    quantidadeDePecas2 = int(quantidadeDePecas2)
    valorUnitarioPecas2 = float(valorUnitarioPecas2)

    #Calcular e imprimir.
    valorTotal = (quantidadeDePecas1 * valorUnitarioPecas1) + (quantidadeDePecas2 * valorUnitarioPecas2)

    print(f"valor total a pagar: R$ {valorTotal:.2F}")
codigosdePecas()

