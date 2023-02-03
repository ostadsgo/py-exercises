""" 
Description:
============
Is x in range between 0 and n noninclusivly; 

Reuirements
-----------
  - If stetments
  - Compression operators
"""


def in_range(x, n):
    pass


# -----------------------------------
# Test area (Do not touch this area)
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(in_range, (2, 10), True)
    assert_equals(in_range, (0, 3), True)
    assert_equals(in_range, (-1, -5), False)
    assert_equals(in_range, (4, 3), False)
    assert_equals(in_range, (0, 3), True)
    assert_equals(in_range, (-1, 3), False)
    assert_equals(in_range, (1, 3), True)
