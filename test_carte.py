from cmath import pi
from unittest.mock import Mock
from carte_pizzeria import CartePizzeria

def test_isEmpty() :
    carte = CartePizzeria()
    carte.pizza = []
    assert carte.is_empty()

def test_nbPizzas() :
    pizza = Mock()
    pizza2 = Mock()
    carte = CartePizzeria()
    carte.pizza = [pizza, pizza2]
    assert carte.nb_pizzas() == 2

def test_addPizza():
    pizza = Mock()
    carte = CartePizzeria()

    carte.pizza = []
    carte.add_pizza(pizza)

    assert carte.pizza == [pizza]

def test_removePizza():
    pizza1 = Mock()
    pizza2 = Mock()

    carte = CartePizzeria()

    carte.pizza = [pizza1, pizza2]

    carte.remove_pizza(pizza1)

    assert carte.pizza == [pizza2]