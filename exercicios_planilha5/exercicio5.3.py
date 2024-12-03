def calcularFatorial(n):
    #Calculo de fatorial de um numero inteiro
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial
def main():
    try:
        N = int(input("Digite um numero inteiro entre 1 e 20: "))
        if N < 1 or N > 20:
            raise ValueError("O numero deve estar entre 1 e 20.")
        resultado = calcularFatorial(N)
        print(f"O fatorial de {N} é {resultado}")
    except ValueError as ve:
        print(f"Error, {ve}")
main()