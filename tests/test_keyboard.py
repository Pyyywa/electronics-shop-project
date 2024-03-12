import pytest
import os

from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    keyboard = Keyboard("RedDragon", 1000, 5)
    return keyboard


def test_init(keyboard):
  assert keyboard.name == "RedDragon"
  assert keyboard.price == 1000
  assert keyboard.quantity == 5
  assert keyboard.language == "EN"


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"

    keyboard.change_lang()
    assert str(keyboard.language) == "RU"