def calcularAnos(PA, PB, G1, G2):
    anos = 0
    while PA <= PB:
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1

        if anos > 100:
            return "Mais do que 100 anos"
    return anos

def main():
    try:
        T = int(input("Digite o numero de casos de teste: "))
        if 1 <= T > 3000:
            raise ValueError("Numeros de teste deve ser maior que 0 e menor que 3000")
        
        for T in range(T):
            valores = input("Digite o valor de PA, PB, G1, G2 separados por espaço: ").split()
            PA, PB = int(valores[0]), int(valores[1])
            G1, G2 = int(valores[2]), int(valores[3])

            resultado = calcularAnos(PA, PB, G1, G2)
            print(resultado)
    except ValueError as ve:
        print(f"Error: {ve}")
main()