"""Module doctring"""
from unittest.mock import Mock
from carte_pizzeria import CartePizzeria


def test_is_empty():
    """is_empty docstring"""
    carte = CartePizzeria()
    carte.pizza = []
    assert carte.is_empty()


def test_nb_pizzas():
    """nb_pizza docstring"""
    pizza = Mock()
    pizza2 = Mock()
    carte = CartePizzeria()
    carte.pizza = [pizza, pizza2]
    assert carte.nb_pizzas() == 2


def test_add_pizza():
    """add_pizza docstring"""
    pizza = Mock()
    carte = CartePizzeria()

    carte.pizza = []
    carte.add_pizza(pizza)

    assert carte.pizza == [pizza]


def test_remove_pizza():
    """remove_pizza docstring"""
    pizza1 = Mock()
    pizza2 = Mock()

    carte = CartePizzeria()

    carte.pizza = [pizza1, pizza2]

    carte.remove_pizza(pizza1)

    assert carte.pizza == [pizza2]
