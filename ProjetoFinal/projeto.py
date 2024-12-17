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

def chamar_bedrock(prompt):
  """Chama a API do Amazon Bedrock e retorna a resposta."""
  client = boto3.client('bedrock-runtime', region_name='us-east-1')
  model_id = "amazon.titan-text-premier-v1:0" 

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
        pergunta = input("Qual Pokémon você procura? (Digite o nome ou sair): ")
        if pergunta.lower() == 'sair':
            break
        else:
            pokemon = buscar_pokemon_por_nome(pergunta)

        if pokemon:
            curiosidade = buscar_curiosidade(pokemon)
            print(f"Pokémon: {pokemon['name']}")
            print(f"Tipo: {pokemon['types'][0]['type']['name']}")
            print(f"Curiosidade: {curiosidade}")
            print("-------------------------------------")
        else:
            print("Pokémon não encontrado.")

if __name__ == "__main__":
    main()