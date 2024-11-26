#media de alunos
def main():
    n1,n2,n3,n4 = map(float, input("Digite as notas n1 n2 n3 n4  separados por espaço ").split())

    #calcula a media conforme os pesos
    media = (n1*2 + n2*3 + n3*4 + n4*1)/10 

    print(f"Média é {media:.1f}")

    if media >=7.0:
        print("Aluno Aprovado")
    elif media < 5.0:
        print("Aluno Reprovado")
    else:
        print("Aluno em recuperação")
        notaRecuperacao = float(input("Digite a nota do exame: "))
        print(f"Nota do exame: {notaRecuperacao}")

        mediaFinal = (media + notaRecuperacao) / 2

        if mediaFinal >= 5.0:
            print("Aluno Aprovado!")
        else:
            print("Aluno Reprovado")

        print(f"Media final: {mediaFinal:.1f}")


main()