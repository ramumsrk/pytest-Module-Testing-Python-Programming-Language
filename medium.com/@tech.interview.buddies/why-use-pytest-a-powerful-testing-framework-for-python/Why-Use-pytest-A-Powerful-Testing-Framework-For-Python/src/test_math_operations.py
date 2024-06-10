#! /usr/bin/python3.12

from typing import Literal

import pytest

@pytest.fixture
def input_data() -> Literal[tuple[int]]:
  return 2, 3

def test_add(input_data) -> Literal[None]:
  a, b = input_data
  assert a + b == 5
  return None

def test_subtraction() -> Literal[None]:
  a, b = input_data
  assert a - b == -1

@pytest.mark.parametrize(
  "a, b, expected",
  [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9),
  ]
)
def test_another_add(
  a: Literal[int],
  b: Literal[int],
  expected: Literal[int]
) -> Literal[None]:
  assert a + b == expected
  return None

def test_failure() -> Literal[None]:
  assert 1 == 2