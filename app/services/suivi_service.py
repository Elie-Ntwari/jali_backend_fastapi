


from app.repository.agent_repository import get_agent_by_id
from app.repository.enfant_repository import get_enfant_by_id
from app.repository.suivi_repository import create_suivi
from app.schemas.suivi_schema import SuiviCreate
from app.models.suivi_model import Suivi
from app.database import SessionLocal
from app.services.prediction_service import predict_rechute
from app.services.risque_service import evaluer_risque

def traiter_suivi(db, suivi_data: SuiviCreate) -> Suivi:
    enfant = get_enfant_by_id(db, suivi_data.enfant_id)
    if not enfant:
        raise ValueError("Enfant introuvable.")

    agent = get_agent_by_id(db, suivi_data.agent_id)
    if not agent:
        raise ValueError("Agent introuvable. Vérifiez l'identifiant.")

    foyer = enfant.foyer

    # Étape 1 – Données dynamiques (venant du suivi)
    dyn = suivi_data.dict()

    # Étape 2 – Données statiques fusionnées
    features = {
        "Sexe": enfant.sexe,
        "age_enfant": enfant.age_enfant,
        "heures_total_travail": dyn["heures_total_travail"],
        "scol_actuelle": dyn["scol_actuelle"],
        "difficulte_fonctionnelle": dyn["difficulte_fonctionnelle"],
        "nb_pieces_cat": foyer.nb_pieces_cat,
        "quintile_bien_etre_x": dyn["quintile_bien_etre_x"],  # par défaut 3.0
        "age_chef": foyer.age_chef,
        "sexe_chef": foyer.sexe_chef,
        "niveau_education_mere_recod": foyer.niveau_education_mere_recod,
        "souffre_punition_physique": dyn["souffre_punition_physique"],
        "travail_enfant_global":  dyn["travail_enfant_global"],
        "etat_logement": foyer.etat_logement,
        "niveau_scol_regroupe": enfant.niveau_scol_regroupe,
        "favorable_correction_physique": dyn["favorable_correction_physique"]
    }

    # Étape 3 – Prédiction
    score = predict_rechute(features)

    # Étape 4 – Évaluation
    niveau_risque, conseil = evaluer_risque(score)

    # Étape 5 – Construction objet Suivi
    suivi_obj = Suivi(
        enfant_id=enfant.id,
        agent_id=suivi_data.agent_id,
        heures_total_travail=suivi_data.heures_total_travail,
        scol_actuelle=suivi_data.scol_actuelle,
        difficulte_fonctionnelle=suivi_data.difficulte_fonctionnelle,
        souffre_punition_physique=suivi_data.souffre_punition_physique,
        travail_enfant_global=suivi_data.travail_enfant_global,
        niveau_scol_regroupe=suivi_data.niveau_scol_regroupe,
        quintile_bien_etre_x=suivi_data.quintile_bien_etre_x,
        favorable_correction_physique=suivi_data.favorable_correction_physique,
        score_suivi=score,
        statut_risque=niveau_risque,
        commentaire_agent=suivi_data.commentaire_agent,
        conseil_personnalise=conseil
    )

    return create_suivi(db, suivi_obj)
