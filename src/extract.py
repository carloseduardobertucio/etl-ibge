import requests
import json
from datetime import datetime
import os
import csv

def create_data_directories():
    """Cria os diretórios necessários para armazenar os dados"""
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)

def get_estados():
    """Extrai lista de estados brasileiros"""
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_municipios(estado_id):
    """Extrai lista de municípios de um estado específico"""
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado_id}/municipios"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_data(data, filename):
    """Salva os dados em CSV"""
    if not data:
        return
    
    # Pega as chaves do primeiro item para usar como cabeçalho
    headers = data[0].keys()
    
    # Cria o nome do arquivo com a data atual
    filepath = f"data/raw/{filename}_{datetime.now().strftime('%Y%m%d')}.csv"
    
    # Salva os dados em CSV
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Dados salvos em {filepath}")

def main():
    """Função principal de extração"""
    print("Iniciando extração de dados...")
    
    # Cria diretórios necessários
    create_data_directories()
    
    # Extrai estados
    print("Extraindo dados dos estados...")
    estados = get_estados()
    save_data(estados, 'estados')
    
    # Extrai municípios para cada estado
    print("Extraindo dados dos municípios...")
    for estado in estados:
        print(f"Extraindo municípios de {estado['nome']}...")
        municipios = get_municipios(estado['id'])
        save_data(municipios, f'municipios_{estado["sigla"]}')
    
    print("Extração concluída!")

if __name__ == "__main__":
    main() 