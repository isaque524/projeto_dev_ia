def calculo():
    # cordenada ponto 1
    print("Entre com o valor do ponto 1")
    x1, y1 = map(float, input().split())

    # cordenada ponto 2
    print("Entre com o valor do ponto 2")
    x2, y2 = map(float, input().split())

    # calculo da formula
    distancia = ((x2 - x1) **2 + (y2 - y1) **2) **0.5

    # exibir a distancia segundo a formula
    print(f"A distancia é = {distancia:.4f}")
calculo()