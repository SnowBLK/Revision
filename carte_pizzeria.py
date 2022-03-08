class CartePizzeria:

    def __init__(self, pizza = []):
        self.__pizaa = pizza


    @property
    def pizza(self):
        return self.__pizza
    
    @pizza.setter
    def pizza(self, value):
        self.__pizza = value

    def is_empty(self):
        return not self.__pizza

    def nb_pizzas(self):
        return len(self.__pizza)

    def add_pizza(self, pizza) :
        self.__pizza.append(pizza)

    def remove_pizza(self, pizza) :
        try:
            self.__pizza.remove(pizza)
        except ValueError :
            return Exception("Pizza not found")


if __name__ == "__main__":
    carte_pizz = CartePizzeria()

    carte_pizz.pizza = [1,3,5]

    print(carte_pizz.remove_pizza(2))