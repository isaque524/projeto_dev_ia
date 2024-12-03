def divisao():
    # A variavel N guarda a quantidade do loop no for
    N = int(input("Digite o numero de pares de valores: "))
    if N < 1:
        raise ValueError("Numero de pares - valores (N) deve ser maior que 0")

    for _ in range(N):
        try:
            X = int(input("Digite o valor de X: "))
            Y = int(input("Digite o valor de Y: "))
            if Y == 0:
                print("Divisão impossivel")
            else:
                resultado = X / Y
                print(f"{resultado:.1f}")
        except ValueError as ve:
            print(f"Erro{ve}")

divisao()