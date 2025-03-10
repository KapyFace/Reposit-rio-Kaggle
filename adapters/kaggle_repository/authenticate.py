import os
from infrastructure.logger.logger import get_logger

logger = get_logger(__name__)

def authenticate():
    
    try:
        os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser("~/.kaggle")
        logger.info("Autenticado com sucesso no Kaggle API.")
    except Exception as e:
        logger.error(f"Erro na autenticação: {e}")