def calculaMediaIdades():
    soma_idades = 0
    quantidade = 0

    while True:
        try:
            print("Se quiser encerrar digite um valor negativo")
            idade = int(input("Digite uma idade:  "))
            if idade < 0:
                break
            soma_idades += idade
            quantidade += 1
        except ValueError:
            print("Entrada invalida, insira um numero inteiro.")
    if quantidade > 0:
        media = soma_idades / quantidade
        return round(media, 2)
    else:
        return "Nenhuma idade valida inserida"
        
def main():
    try:
        media_idades = calculaMediaIdades()
        print(f"A media das idades é: {media_idades}")
    except Exception as e:
        print(f"Error: {e}")
main()