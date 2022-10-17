
from cards import Card

def test_falle_iguales():
    c1 = Card('Hecer algo', 'Javier')
    c2 = Card('Hecer algo', 'Javier')

    assert c1 == c2


if __name__ == '__main__':
    test_falle_iguales()