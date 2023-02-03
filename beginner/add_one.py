"""
Description
-----------
Get integer number and add one to it.

Requirements
------------
  - Variables
  - Arithmetic operators

"""
import tests


def add_one(n):
    return n + 1


if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(add_one, (1,), 2)
    assert_equals(add_one, (0,), 1)
    assert_equals(add_one, (-1,), 0)
