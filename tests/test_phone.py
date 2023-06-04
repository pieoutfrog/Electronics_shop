import pytest

from src.item import Item
from src.phone import Phone


# class New:
#     """Класс не связанный с Item, для теста add"""
#
#     def __init__(self, name: str, price: float, quantity: int, sim_cards_num: int):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.sim_cards_num = sim_cards_num


@pytest.fixture
def phone1():
    """Описание фикстуры для тестов"""
    return Phone("Смартфон", 70000, 10, 1)


def test_init(phone1):
    """Тест для init"""
    assert phone1.price == 70000
    assert phone1.name == 'Смартфон'
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 1


def test_number_of_sim():
    """Тест переменой количества симок"""
    date = Phone("Смартфон", 70000, 10, 2)
    assert date.number_of_sim == 2
    with pytest.raises(ValueError):
        date.number_of_sim = 0


def test_repr(phone1):
    """Тест для метода repr"""
    assert repr(phone1) == "Phone('Смартфон', 70000, 10, 1)"