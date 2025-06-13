# Any pytest file should start with KEYWORD -> test_
#                           or end with _test
# Pytest method names should start with KEYWORD -> test
import pytest


def test_thirdProgram():
    msg = "Hello!!"
    assert msg == "Hi", "Test failed because strings do not match"


@pytest.mark.smoke
@pytest.mark.skip
def test_addition():
    a = 4
    b = 5
    assert a + b == 9, "Test failed because a + b == 10"

