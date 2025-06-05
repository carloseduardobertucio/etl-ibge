import requests
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IBGEExtractor:
    def __init__(self):
        self.base_url = "https://servicodados.ibge.gov.br/api/v1"
        
        
    def get_estados(self):
        try:
            url = f"{self.base_url}/localidades/estados"
            response = requests.get(url)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except Exception as e:
            logger.error(f"Erro ao extrair estados: {str(e)}")
            raise


    def get_municipios(self, estado_id):
        try:
            url = f"{self.base_url}/localidades/estados/{estado_id}/municipios"
            response = requests.get(url)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except Exception as e:
            logger.error(f"Erro ao extrair municípios: {str(e)}")
            raise


    def get_populacao(self, municipio_id):
        try:
            url = f"{self.base_url}/populacao/{municipio_id}"
            response = requests.get(url)
            response.raise_for_status()
            return pd.DataFrame(response.json())
        except Exception as e:
            logger.error(f"Erro ao extrair população: {str(e)}")
            raise


    def save_to_csv(self, df, filename):
        try:
            df.to_csv(f"data/raw/{filename}_{datetime.now().strftime('%Y%m%d')}.csv", 
                     index=False, encoding='utf-8')
            logger.info(f"Dados salvos em {filename}")
        except Exception as e:
            logger.error(f"Erro ao salvar dados: {str(e)}")
            raise 