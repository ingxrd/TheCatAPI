from django.shortcuts import render
import requests  # Para realizar a requisição HTTP
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def inicio(request):
    # Carregar a chave da API a partir do arquivo .env
    api_key = os.getenv('API_KEY')

    # Verificar se a chave foi carregada corretamente
    if api_key is None:
        raise ValueError("API_KEY não encontrada no arquivo .env")

    # URL para pegar uma imagem aleatória de gato
    random_image_url = 'https://api.thecatapi.com/v1/images/search'

    # Requisição GET para a API
    response = requests.get(random_image_url, headers={'x-api-key': api_key})

    if response.status_code == 200:
        # Extraindo a URL da imagem do gato
        data = response.json()
        cat_image = {
            "url": data[0]["url"]
        }
    else:
        cat_image = None

    # Passando a imagem para o template 'inicio.html'
    return render(request, 'inicio.html', {'cat_image': cat_image})
