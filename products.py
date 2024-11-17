class Product:

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Constructor for the Product class
        :param name: str: Name of the product
        :param price: float: Price of the product
        :param quantity: int: Quantity of the product
        """
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non empty string")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if price < 0:
            raise ValueError("Price must be non-negative")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = False if quantity == 0 else True

    def get_quantity(self) -> float: # Not sure why the documentation says it should return float. I think quantity should be an integer
        """ Returns the quantity of the product """
        return float(self.quantity)

    def set_quantity(self, quantity: int) -> None:
        """ Sets the quantity of the product and deactivates it if quantity is 0 """
        if not isinstance(quantity, int):
            raise ValueError("New quantity must be an integer")
        if quantity < 0:
            raise ValueError("New quantity must be non-negative")
        if quantity == 0:
            self.active = False
        self.quantity = quantity

    def is_active(self) -> bool:
        """ Returns whether the product is active or not """
        return self.active

    def activate(self) -> None:
        """ Activates the product """
        self.active = True

    def deactivate(self) -> None:
        """ Deactivates the product """
        self.active = False

    def __str__(self) -> str:
        """ Returns the string representation of the product """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def show(self) -> str:
        """
        Alias for __str__
        Returns the string representation of the product
        """
        return self.__str__()

    def buy(self, quantity: int) -> float:
        """
        Buys the product and returns the total cost
        :param quantity: int: Quantity of the product to buy
        :return: float: Total cost of the product
        """
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show() # As specified in the documentation, this returns a string and doesn't print anything by itself.
    print(bose.show()) # This prints the string representation of the product
    mac.show()
    print(mac) # This also prints the string representation of the product

    bose.set_quantity(1000)
    bose.show()
    print(bose)


if __name__ == "__main__":
    main()