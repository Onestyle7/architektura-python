# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 2999.99, 10)

# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available()

def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    assert product.total_value() == 2999.99 * 10

# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    # TODO: Dodaj przypadki testowe jako krotki, np.:
    # (5, 15),   # dodanie 5 do poczatkowych 10 = 15
    # (0, 10),   # dodanie 0 = bez zmian
    # (100, 110),  # dodanie 100
    (5,15),
    (0,10),
    (100,110)
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(15)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    with pytest.raises(ValueError):
        product.add_stock(-5)

@pytest.mark.parametrize("percent, expected_price", [
    (0, 2999.99),
    (50, 1499.995),
    (100, 0.0),
])
def test_apply_discount_parametrized(product, percent, expected_price):
    """Testuje apply_discount z roznymi wartosciami."""
    product.apply_discount(percent)
    assert product.price == expected_price

#test dla nieprawidłowych wartości
@pytest.mark.parametrize("invalid_percent",[
    -1,101,150
])
def test_apply_discount_raises_error(product, invalid_percent):
    with pytest.raises(ValueError):
        product.apply_discount(invalid_percent)