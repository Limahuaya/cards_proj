from cards import Card

def test_field_access():
    c = Card("alguna tarea", "Jaime", "todo", 123)
    print(c.summary)
    assert c.summary == 'alguna tarea'
    assert c.owner == 'Jaime'
    assert c.state == 'todo'
    assert c.id == 123

def test_defult_value():
    c = Card()
    print(c.summary)
    assert c.summary is None
    assert c.owner is None
    assert c.state is 'todo'
    assert c.id is None

# Compare dos tarjetas, teniendo en cuenta 
# que tiene la misma asijnacion

def test_compare_value_card():
    a = Card("alguna tarea", "Hector", "todo", 123)
    b = Card("alguna tarea", "Hector", "todo", 123)
    assert a == b


"""
que valide la diferencia id en dos tareas iguales
"""

def test_compare_id_equals_value_card():
    a = Card("alguna tarea", "Hector", "todo", 1)
    b = Card("alguna tarea", "Hector", "todo", 2)
    assert a.id != b.id

"""
validar la diferencias de dos tareas
"""

def test_compare_diferent_value_card():
    a = Card("alguna tarea", "Hector", "todo", 1)
    b = Card("alguna tarea xd", "Hector Javier", "done", 2)
    assert a.summary != b.summary
    assert a.owner != b.owner
    assert a.state != b.state
    assert a.id != b.id
    assert a != b

"""
validar dos tareas, una de forma redicional
y otra eb formato dict
"""

def test_create_dic_dard_and_traditional_card():
    dicionario = {
        "id": 1,
        "summary": "Alguna tarea 1",
        "owner": "Hector Javier",
        "state": "done",
    }
    a = Card(**dicionario)
    assert a.to_dict() == dicionario


def test_create_dic_dard_and_traditional_card2():
    dicionario = {
        "id": 1,
        "summary": "Alguna tarea 1",
        "owner": "Hector Javier",
        "state": "done",
    }
    a = Card().from_dict(dicionario)

    b = Card("Alguna tarea 1", "Hector Javier", "done", 1)

    assert a == b


"""
construir diciconarios a partir de objetos
"""


def test_compare_to_dict_compare_dict_obj():
    dicionario = {
        "id": 1,
        "summary": "Alguna tarea 1",
        "owner": "Hector Javier",
        "state": "done",
    }
    a = Card('Alguna tarea 1', "Hector Javier", "done", 1)
    assert dicionario == a.to_dict()
   