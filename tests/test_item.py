"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.get_name == 'Ноутбук'
    assert item1.price == 1000
    assert item1.quantity == 3
    item2 = Item.all[2]
    assert item2.get_name == 'Кабель'
    assert item2.price == 10
    assert item2.quantity == 5

def test_string_to_number():
    assert Item.string_to_number("10") == 10
    assert Item.string_to_number("25") == 25

def test_get_name():
    item = Item("Мышка", 50, 5)
    item.name = "Мышка"
    assert item.name == "Мышка"

    item1 = Item("Клавиатура",75,5)
    item1.name = "Клавиатура"
    assert item1.name == "Клавиатура"



def test__str__(item1):
    assert str(item1) == "Смартфон"


def test__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"