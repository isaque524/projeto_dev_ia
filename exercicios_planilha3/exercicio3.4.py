A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

somaCeD =  C + D
somaAeB = A + B

if B > C and D > A:
    if somaCeD > somaAeB:
        if C and B > 0:
            if A % 2 == 0:
                print("Valores aceitos")
else:
    print("valores não aceitosS")