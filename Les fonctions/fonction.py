def elever_au_carre(nombre):
    """
    Retourne le carré du nombre passé en argument. Si le nombre n'est pas un entier, la fonction retourne -1
    """
    try:
        resultat = nombre ** 2
    except TypeError:
        resultat = -1
    return resultat
