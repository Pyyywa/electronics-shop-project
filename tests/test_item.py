"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def position():
    item1 = Item("Phone", 1000, 3)
    return item1

def test_calculate_total_price(position):
    assert position.calculate_total_price() == 3000

def test_apply_discount(position):
    position.apply_discount()
    assert position.price == 1000 * Item.pay_rate

def test_all(position):
    item2 = Item("Phone2", 2000, 3)
    assert len(Item.all) == 2
