import random
import requests
import boto3
import json

def buscar_pokemon_por_nome(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def buscar_pokemon_por_tipo(tipo):
    url = f"https://pokeapi.co/api/v2/type/{tipo.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        # Escolhe um Pokémon aleatório do tipo
        pokemon = random.choice(response.json()["pokemon"])
        return buscar_pokemon_por_nome(pokemon["pokemon"]["name"])
    else:
        return None
def chamar_bedrock(prompt):
  """Chama a API do Amazon Bedrock e retorna a resposta."""
  client = boto3.client('bedrock-runtime', region_name='us-east-1')
  model_id = "amazon.titan-text-premier-v1:0"  # Substitua pelo ID do seu modelo

  response = client.converse(
      modelId=model_id,
      messages=[
          {
              "role": "user",
              "content": [{"text": prompt}],
          }
      ],
      inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
  )

  return response["output"]["message"]["content"][0]["text"]
def buscar_curiosidade(pokemon):
    prompt = f"Qual é uma curiosidade interessante sobre o Pokémon {pokemon['name']}?"
    curiosidade = chamar_bedrock(prompt)
    return curiosidade

def main():
    while True:
        pergunta = input("Qual Pokémon você procura? (Digite o nome ou o tipo): ")
        if pergunta.lower() == 'sair':
            break

        if pergunta.lower() in ["fogo", "água", "elétrico", ...]:  # Lista de tipos
            pokemon = buscar_pokemon_por_tipo(pergunta)
        else:
            pokemon = buscar_pokemon_por_nome(pergunta)

        if pokemon:
            curiosidade = buscar_curiosidade(pokemon)
            print(f"Pokémon: {pokemon['name']}")
            print(f"Tipo: {pokemon['types'][0]['type']['name']}")
            print(f"Curiosidade: {curiosidade}")
        else:
            print("Pokémon não encontrado.")

if __name__ == "__main__":
    main()