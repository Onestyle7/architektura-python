# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancje Product do testow."""
        self.prod = Product("Laptop", 2999.99, 10)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        """Sprawdz, czy dodanie towaru zwieksza quantity."""
        result = self.prod.add_stock(5)
        self.assertEqual(result, 15)

    def test_add_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.prod.add_stock(-5)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
        result = self.prod.remove_stock(5)
        self.assertEqual(result, 5)

    def test_remove_stock_too_much_raises(self):
        """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.prod.remove_stock(15)


    def test_remove_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.prod.remove_stock(-5)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        """Sprawdz, czy produkt z quantity > 0 jest dostepny."""
        result = self.prod.is_available()
        self.assertTrue(result)


    def test_is_not_available_when_empty(self):
        """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""
        self.prod = Product("Laptop", 2999.99, 0)
        result = self.prod.is_available()
        self.assertFalse(result)


    # --- Testy total_value ---

    def test_total_value(self):
        """Sprawdz, czy total_value zwraca price * quantity."""
        result = self.prod.total_value()
        self.assertEqual(result, 2999.99 * 10)


if __name__ == "__main__":
    unittest.main()
