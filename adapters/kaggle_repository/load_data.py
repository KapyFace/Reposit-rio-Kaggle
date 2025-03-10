import os
import pandas as pd
from infrastructure.logger.logger import get_logger

logger = get_logger(__name__)

def load_data(download_path, file_name):
    
    try:
        file_path = os.path.join(download_path, file_name)
        df = pd.read_csv(file_path)
        logger.info(f"Arquivo {file_name} carregado com sucesso.")
        return df
    except Exception as e:
        logger.error(f"Erro ao carregar dataset: {e}")
        return None