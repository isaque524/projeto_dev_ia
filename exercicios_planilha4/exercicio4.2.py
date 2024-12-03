def main():
    maiorValor = None
    posicaoMaior = 0
    print("Digite 11 numeros")
    for i in range (1,11):
        valor = int(input())
        if maiorValor is None or valor > maiorValor:
            maiorValor = valor
            posicaoMaior = i

    print(f"O maior valor é {maiorValor}")
    print(f"Ele se encontra na {posicaoMaior}° posição")

main()
        