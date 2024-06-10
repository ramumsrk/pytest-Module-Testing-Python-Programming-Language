#! /usr/bin/python3.12

from typing import Literal

def test_addition() -> Literal[None]:
  assert 1 + 1 == 2
  return None

def test_subtraction() -> Literal[None]:
  assert 2 - 1 == 1
  return None