#o programa vai ler o codigo de um item e a quantidade deste item

def main ():
    codigo, quantidade = map(int, input().split())
    #tabela de preços

    precos = {
        1: 4.00, #Cachorro-quente
        2: 4.50, # X-SALADA
        3: 5.00, # X-BACON
        4: 7.50, # X-EGG
        5: 8.50, #X-TUDO
    }


    if codigo in precos:
        # Calcular valor total a pagar
        total = precos[codigo] * quantidade

        #Imprime o texto na tela no formato especificado
        print(f"Total em compras: R$ {total:.2f}")

main()