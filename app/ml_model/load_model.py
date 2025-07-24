# app/utils/ml_model_loader.py

import joblib
import os

# Définir le chemin absolu du modèle
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_rf_pipeline_jali.pkl")

def load_ml_model():
    """
    Charge le modèle ML entraîné (Pipeline sklearn) depuis le fichier .pkl.
    """
    return joblib.load(MODEL_PATH)

# Chargement unique du modèle au démarrage (évite rechargements multiples)
ml_model = load_ml_model()
