import fonction
import pytest

def test_elever_au_carre_retourne_la_valeur_attendu():
    """
    description du test.
    """

    valeur = fonction.elever_au_carre(nombre=3)
    assert valeur == 9

def test_elever_au_carre_supporte_zero():
    valeur = fonction.elever_au_carre(0)
    assert valeur == 0

def test_elever_au_carre_retourne_code_correct_si_nombre_est_une_chaine():
    with pytest.raises(TypeError):
        valeur = fonction.elever_au_carre("bonjour")