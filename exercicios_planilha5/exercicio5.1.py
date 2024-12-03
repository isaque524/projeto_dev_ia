def sequencia(n):
    for i in range (1, n + 1):
        print(f"{i} {i**2} {i**3}")
        print(f"{i} {i**2 + 1} {i**3 + 1}")
def main():
    try:
        N = int(input("Digite o valor para N: "))
        if N < 1 or N > 1000:
            raise ValueError("N deve estar entre 1 e 1000")
        sequencia(N)
    except ValueError as ve:
        print(f"Erro: {ve}")
main()