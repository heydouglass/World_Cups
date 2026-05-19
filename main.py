# IMPORTANDO BIBLIOTECAS
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# URL API
url = "https://v3.football.api-sports.io/leagues"

# HEADERS
headers = {
    'x-apisports-key': os.getenv("API_KEY")
}

# REQUISIÇÃO
response = requests.get(url, headers=headers)

# CONVERTE PARA JSON
data = response.json()

# NORMALIZA JSON
df = pd.json_normalize(data["response"])

# FILTRA COPA DO MUNDO
world_cup = df[df["league.name"] == "World Cup"]

# MOSTRA RESULTADO
print(world_cup[[
    "league.id",
    "league.name",
    "country.name"
]])