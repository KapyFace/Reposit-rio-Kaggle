import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from infrastructure.logger import get_logger

logger = get_logger(__name__)

def preprocess_data(df):
    logger.info("Iniciando pré-processamento dos dados...")

    df = df.dropna(axis=1, thresh=int(0.8 * len(df)))

    df = df.fillna(df.mean())

    X = df.iloc[:, :-1]  
    y = df.iloc[:, -1]   

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

def train_model(X, y):
    logger.info("Iniciando treinamento do modelo...")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    logger.info(f"Acurácia do modelo: {acc:.4f}")
    return model

def run_pipeline(file_path):
    df = pd.read_csv(file_path)
    X, y = preprocess_data(df)
    model = train_model(X, y)
    return model
