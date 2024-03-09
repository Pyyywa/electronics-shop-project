import pytest
import os

from src.item import Item
from src.phone import Phone

@pytest.fixture
def phone():
  phone = Phone("Телефон", 200, 4, 5)
  return phone


def test_init(phone):
  assert phone.name == "Телефон"
  assert phone.price == 200
  assert phone.quantity == 4
  assert phone.number_of_sim == 5


def test_repr(phone):
  assert repr(phone) == "Phone('Телефон', 200, 4, 5)"

