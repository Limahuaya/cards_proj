
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
    print("Sin solución")

def test_calcula_resultado():
    a = 2
    b = 4
    assert resolver_ecuacion(a,b) == -2

def test_ecuacion_success():
    a = 2
    b = 4
    assert dividendo_diferente_q_cero(a)
    assert resolver_ecuacion(a,b) == -2
