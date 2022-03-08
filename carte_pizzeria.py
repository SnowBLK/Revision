"""class cartePizzeria
"""


class CartePizzeria:
    """Class docstrings."""

    def __init__(self, pizza=None):
        self.__pizza = pizza

    @property
    def pizza(self):
        """getter"""
        return self.__pizza

    @pizza.setter
    def pizza(self, value):
        """setter"""
        self.__pizza = value

    def is_empty(self):
        """returns if list is empty"""
        return not self.__pizza

    def nb_pizzas(self):
        """returns number of pizza list"""

        return len(self.__pizza)

    def add_pizza(self, pizza):
        """adds a pizza to pizza list"""
        self.__pizza.append(pizza)

    def remove_pizza(self, pizza):
        """remove pizza from pizza list"""
        try:
            self.__pizza.remove(pizza)
            return self.__pizza
        except ValueError:
            return Exception("Pizza not found")


# if __name__ == "__main__":
#     carte_pizz = CartePizzeria()

#     carte_pizz.pizza = [1,3,5]

#     print(carte_pizz.remove_pizza(2))
