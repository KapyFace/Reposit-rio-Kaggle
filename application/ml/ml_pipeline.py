import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from infrastructure.logger.logger import get_logger


logger = get_logger(__name__)

def preprocess_data(file_path):
    logger.info("Carregando o dataset do Credit Card Application...")
    df = pd.read_csv(file_path)
    
    logger.info("Iniciando pré-processamento dos dados...")
    df = df.dropna(axis=1, thresh=int(0.8 * len(df)))  # Remove colunas com muitos valores nulos
    df = df.fillna(df.mean())  # Preenche valores nulos com a média
    
    X = df.iloc[:, :-1]  # Features
    y = df.iloc[:, -1]   # Target
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y

def run_pipeline(file_path):
    X, y = preprocess_data(file_path)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    logger.info("Treinando modelo RandomForest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    logger.info(f"Acurácia do modelo: {accuracy:.2f}")
    
    return model
