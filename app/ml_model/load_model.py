import pickle
import os

# Charger le modèle au démarrage (pour éviter de le charger à chaque requête)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_rf_pipeline_jali.pkl")

def load_ml_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

ml_model = load_ml_model()  # importable partout
