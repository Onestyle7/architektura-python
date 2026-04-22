# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.quantity += amount
        return self.quantity

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        if self.quantity < amount:
            raise ValueError("Not enough stock")
        
        self.quantity -= amount
        return self.quantity


    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity if self.is_available() else 0
    
    def apply_discount(self, percent: float):
        if percent < 0 or percent > 100:
            raise ValueError("Discount cannot be negative or greater than 100%")
        self.price *= (1 - percent / 100)
        return self.price