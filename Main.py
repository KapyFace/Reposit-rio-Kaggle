from adapters.kaggle_repository.authenticate import authenticate
from adapters.kaggle_repository.download_data import download_data
from application.use_cases.generate_report import generate_report
from application.ml.ml_pipeline import run_pipeline

if __name__ == "__main__":
    dataset_name = "nazishjaveed/credit-card-application"  
    file_name = "Credit_Card_Applications.csv"  
    download_path = "kaggle_data"

    authenticate()
    download_data(dataset_name, download_path)
    generate_report(download_path, file_name)

    model = run_pipeline(file_path)
