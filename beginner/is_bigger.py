"""
Description
------------
Compare two integers x and y togeter
if x bigger than y return 1
if x smaller than y return -1
if x and y were equal return 0

Reuirements
-----------
  - if statement
  - comparession operator
"""


def is_bigger(x, y):
    pass


# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(is_bigger, (0, 0), False)
    assert_equals(is_bigger, (-1, -5), True)
    assert_equals(is_bigger, (2, 3), False)
    assert_equals(is_bigger, (2, 1), True)
