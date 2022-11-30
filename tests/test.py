import pytest

from app.calc import Calculator as c

class TestCalc():
    def setup(self):
        self.calc = c()

    def test_adding_success(self):
        assert self.calc.adding(4, 4) == 8

    def test_division_success(self):
        assert self.calc.division(8, 4) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(24, 16) == 8

    def test_multiply_success(self):
        assert self.calc.multiply(34, 2) == 68

    def teardown(self):
        print('Выполнение метода Teardown')
