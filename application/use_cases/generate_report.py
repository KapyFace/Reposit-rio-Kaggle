from domain.entities.dataset import Dataset
from infrastructure.logger.logger import get_logger
from adapters.kaggle_repository.load_data import load_data

logger = get_logger(__name__)

def generate_report(download_path, file_name):
    
    df = load_data(download_path, file_name)
    if df is not None:
        dataset = Dataset(file_name, df)
        summary = dataset.get_summary()
        logger.info(f"Resumo dos dados:\n{summary}")
    else:
        logger.warning("Não foi possível gerar o relatório.")