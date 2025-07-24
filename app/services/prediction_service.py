from app.ml_model.load_model import ml_model

def predict_rechute(features: dict) -> float:
    """
    Prend un dictionnaire de features, retourne le score prédit (float).
    """
    import pandas as pd
    input_df = pd.DataFrame([features])
    score = ml_model.predict_proba(input_df)[0][1]  # probabilité classe 1
    return round(score, 3)
