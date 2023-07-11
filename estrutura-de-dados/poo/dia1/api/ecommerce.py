import re
import json
from dataclasses import dataclass


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.__email = email
        self.address = address

    def __str__(self) -> str:
        return f"{self.name};{self.__email};{self.address};"

    def show_details(self):
        print(
            f"Nome: {self.name}|Email: {self.__email}|Endereço: {self.address}"
        )

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not re.match(r"[^w]+@[^w]+\.[^w]+", value):
            raise ValueError("Email inválido")
        self.__email = value

    @classmethod
    def load_customers_from_json(cls, file_path: str):
        with open(file_path, "r") as file:
            data = json.load(file)
        return [cls(**customer) for customer in data]


@dataclass
class Product:
    name: str
    unit_price: float
    stock_quantity: int = 0


class ShoppingCart:
    def __init__(self):
        self._items: list[tuple[Product, int]] = []

    def add_item(self, product_quantity: tuple[Product, int]):
        self._items.append(product_quantity)

    def item_quantity(self):
        return sum(item[1] for item in self._items)

    def total_price(self):
        return sum(
            product.unit_price * quantity for product, quantity in self._items
        )


class PremiumCustomer(Customer):
    def __init__(
        self, name: str, email: str, address: str, rewards_points: int = 0
    ):
        super().__init__(name, email, address)
        self.rewards_points = rewards_points

    def add_rewards_points(self, points: int):
        self.rewards_points += points

    def redeem_rewards_points(self, points: int):
        if self.rewards_points >= points:
            self.rewards_points -= points
            return True
        else:
            return False

    def show_details(self):
        super().show_details()
        print(f"Rewards Points: {self.rewards_points}")