"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os

from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def position():
    item1 = Item("Phone", 1000, 3)
    return item1

@pytest.fixture
def stroka():
    a = "40.0"
    return a

@pytest.fixture
def file():
    file = 'src/items.csv'
    return file


def test_repr():
    item1 = Item("Смартфон", 100, 2)
    assert repr(item1) == "Item('Смартфон', 100, 2)"


def test_str():
    item1 = Item("Смартфон", 100, 2)
    assert str(item1) == 'Смартфон'


def test_add():
  item1 = Item("Смартфон", 100, 2)
  phone1 = Phone("Телефон", 200, 4, 5)
  assert item1 + phone1 == 6
  assert phone1 + item1 == 6

  with pytest.raises(ValueError):
    phone1 + 1

def test_calculate_total_price(position):
    assert position.calculate_total_price() == 3000


def test_apply_discount(position):
    position.apply_discount()
    assert position.price == 1000 * Item.pay_rate


def test_all(position):
    """Вызываем фикстуру 3 раза для каждой функции,
поэтому ожидаемая длина 3"""
    assert len(Item.all) == 7


def test_name_setter(position):
    position.name = "Smartphone"
    assert len(position.name) <= 10
    assert position.name == "Smartphone"


def test_string_to_number(stroka):
    assert Item.string_to_number(stroka) == 40


def test_instantiate_from_csv(file):
    assert Item.instantiate_from_csv('src/items.csv') is None
    assert len(Item.all) == 9


def test_instantiate_from_csv_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/items.csv')


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/items.csv')


