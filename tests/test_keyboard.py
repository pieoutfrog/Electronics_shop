import pytest
from src.item import Item
from src.keyboard import Keyboard

@pytest.fixture
def keyboard1():
    return Keyboard('Dell Inspiron 5570', 50000, 10)


def test_init(keyboard1):
    assert keyboard1.get_name == 'Dell Inspiron 5570'
    assert keyboard1.price == 50000
    assert keyboard1.quantity == 10


def test_language(keyboard1):
    assert str(keyboard1.language) == "EN"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "EN"



