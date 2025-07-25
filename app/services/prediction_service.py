from app.ml_model.load_model import ml_model

import pandas as pd


def predict_rechute(features: dict) -> float:
    """
    Prédit le score de rechute à partir des features d’un enfant.
    :param features: dictionnaire des variables nécessaires
    :return: score de rechute (float)
    """
    try:
        # Convertir en DataFrame à une ligne
        df = pd.DataFrame([features])
        
        # Faire la prédiction
        score = ml_model.predict(df)[0]  # retourne un float
        return round(float(score),3)

    except Exception as e:
        raise ValueError(f"Erreur de prédiction : {str(e)}")
