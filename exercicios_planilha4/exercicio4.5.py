def resto():
    try:
        X = int(input("Digite o valor de X: "))
        Y = int(input("Digite o valor de Y: "))

        if X > Y:
            X, Y = Y, X

        for i in range (X + 1, Y):
            if i % 5 == 2 or i% 5 == 3:
                print(i)
    except ValueError:
        print("Error, tente um numero inteiro!")
resto()