import kaggle
from infrastructure.logger.logger import get_logger

logger = get_logger(__name__)

def download_data(dataset_name, download_path="kaggle_data"):
    try:
        kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
        logger.info(f"Dados baixados para {download_path}.")
    except Exception as e:
        logger.error(f"Erro ao baixar dataset: {e}")
