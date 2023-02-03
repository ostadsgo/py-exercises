"""
Calculate area of a rectangle if width or height of the rectangle
were less than zero return 0

Requirements:
  - if statement
  - Operators
"""


def area(w, h):
    pass
# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(area, (2, 3), 6)
    assert_equals(area, (0, 0), 0)
    assert_equals(area, (-1, 3), 0)
    assert_equals(area, (-1, -1), 0)
    assert_equals(area, (2, -1), 0)
