def evaluer_risque(score: float):
    """
    Évalue le niveau de risque de rechute d'un enfant et fournit une recommandation synthétique pour l'action sociale.
    
    :param score: Score de prédiction de rechute (entre 0 et 1)
    :return: Tuple (niveau_risque, conseil_action)
    """

    if score < 0.15:
        return (
            "Risque Faible",
            "Maintenir la stabilité : suivi léger, continuité scolaire, soutien familial encouragé."
        )
    
    elif score < 0.33:
        return (
            "Risque Moyen",
            "Surveiller et renforcer : améliorer logement, suivre la scolarité, prévenir la violence domestique."
        )

    elif score < 0.5:
        return (
            "Risque Modéré",
            "Mettre en place un accompagnement renforcé : suivi éducatif, soutien parental, logement à améliorer."
        )
    
    elif score < 0.66:
        return (
            "Risque Élevé",
            "Prioriser l’enfant : réduire travail, retour à l’école, accompagnement psychologique nécessaire."
        )

    else:
        return (
            "Risque Très Élevé",
            "Intervention urgente : hébergement sécurisé, soutien alimentaire, prise en charge globale (école, santé mentale)."
        )
