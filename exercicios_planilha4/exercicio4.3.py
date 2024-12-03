def main():
    try:
        N = int(input("Digite o número de casos de teste: "))
        if N < 1:
            raise ValueError("Numero de casos de teste deve ser maior que zero")
        for _ in range(N):
            X, Y = map(int, input("Digite os valores de X e Y: ").split())
            if X > Y:
                X, Y = Y, X
            soma = sum(i for i in range(X + 1, Y) if i % 2 != 0)
            print(soma)
    except ValueError as ve:
        print(f"Erro: {ve}")

main()
