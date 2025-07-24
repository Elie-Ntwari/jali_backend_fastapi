def evaluer_risque(score: float):
    """
    Évalue le niveau de risque de rechute d'un enfant et fournit un message de recommandations adapté.
    :param score: Score de prédiction de rechute (entre 0 et 1)
    :return: Tuple (niveau_libelle, message)
    """

    if score < 0.15:
        return (
            "🟢 Faible",
            "Profil stable : bon bien-être, logement correct, encadrement protecteur.\n"
            "Maintenir l'encadrement actuel, valoriser les bonnes pratiques, et encourager la poursuite scolaire."
        )

    elif score < 0.33:
        return (
            "🟠 Moyen-Élevé",
            "Profil avec pauvreté structurelle et logement précaire.\n"
            "Maintenir la scolarisation, améliorer les conditions de vie, réduire l'exposition à la violence."
        )

    elif score < 0.5:
        return (
            "🟡 Modéré",
            "Enfants scolarisés partiellement, souvent punis physiquement et vivant en surpopulation.\n"
            "Renforcer le suivi scolaire, agir sur les conditions de logement, sensibiliser sur les violences."
        )

    elif score < 0.66:
        return (
            "🔴 Très Élevé",
            "Adolescents, surtout filles, très exposés : travail massif, violences, déscolarisation.\n"
            "Intervention prioritaire : soutien psychologique, réduction du travail, retour à l’école."
        )

    else:
        return (
            "🔴 Élevé",
            "Jeunes enfants en situation de grande précarité, souvent victimes de violences.\n"
            "Suivi intensif recommandé : hébergement sécurisé, soutien alimentaire, accompagnement scolaire et santé mentale."
        )
