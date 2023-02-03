""" Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

For example, if n = 111, then nearest_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.
"""


def nearest_sq(n):
    return round(n ** .5) *  round(n ** .5)


if __name__ == "__main__":
    from tests import assert_equals
    assert_equals(nearest_sq, (1,), 1)
    assert_equals(nearest_sq, (2,), 1)
    assert_equals(nearest_sq, (10,), 9)
    assert_equals(nearest_sq, (111,), 121)
    assert_equals(nearest_sq, (9999,), 10000)
