"""
Instruction:
-----------
Compare two integers if number one bigger than number tow 
return True otherwise return False

Rquirements
-----------
  - If statement
  - Comperassion operators
  - Boolean type
"""

def compare(x, y):
    pass

# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(compare, (2, 3), -1)
    assert_equals(compare, (0, 5), -1)
    assert_equals(compare, (-1, -5), -1)
    assert_equals(compare, (4, 0), 1)
    assert_equals(compare, (0, 0), 0)
