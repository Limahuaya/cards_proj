from pathlib import Path
from re import A
import pytest
from tempfile import TemporaryDirectory
import cards


# ctrl + shif + a: comentar con """"""
#  
#def test_vacio():
#    with TemporaryDirectory() as db_dir:
#        db_path = Path(db_dir)
#        db = cards.CardsDB(db_path)
#        count = db.count()
#        db.close()
#        assert count == 0
#        print("success test_vacio")


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        count = db.count()
        yield db
        db.close()

def test_db_vacio(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    n = 6
    for i in range(n):
        cards_db.add_card(cards.Card(f"Numero {i}"))
    assert cards_db.count() == n


""" 
Ejercicio, elabora un programa que resuelva una ecuacion de primero grado, con TDD
"""

# ax + b = c
# -b/a = x


# Dividento debe ser diferente que cero
def dividendo_diferente_q_cero(a):
    return a != 0

def resolver_ecuacion(a,b):
    return -b/a


def test_ecuacion_dividendo_no_cero():
    a=0
    assert not dividendo_diferente_q_cero(a)

def test_calcula_resultado():
    a = 2
    b = 4
    assert resolver_ecuacion(a,b) == -2

def test_ecuacion_success():
    a = 2
    b = 4
    assert dividendo_diferente_q_cero(a)
    assert resolver_ecuacion(a,b) == -2
