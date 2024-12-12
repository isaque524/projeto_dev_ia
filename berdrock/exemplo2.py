import requests
import json

def buscar_produtos(categoria):
  """Busca produtos na Fake Store API com base na categoria.

  Args:
    categoria: A categoria de produtos a ser buscada.

  Returns:
    Uma lista de dicionários, cada um representando um produto.
  """

  url = f"https://fakestoreapi.com/products/category/{categoria}"
  response = requests.get(url)
  data = response.json()
  return data

def mostrar_produtos(produtos):
  """Mostra os detalhes dos produtos encontrados.

  Args:
    produtos: Uma lista de dicionários, cada um representando um produto.
  """

  for produto in produtos:
    print(f"Produto: {produto['title']}")
    print(f"Preço: ${produto['price']}")
    print(f"Descrição: {produto['description']}")
    print("--------------------")

def main():
  while True:
    pergunta = input("O que você procura? (Digite 'sair' para encerrar): ")
    if pergunta.lower() == 'sair':
      break

    produtos = buscar_produtos(pergunta.lower())
    if produtos:
      mostrar_produtos(produtos)
    else:
      print("Não encontramos produtos para essa categoria.")

if __name__ == "__main__":
  main()