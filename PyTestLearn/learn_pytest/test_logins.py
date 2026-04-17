import pytest


def test_LoginEmail(setup):
    print("This is login by email test")
    assert True==True

def test_LoginFacebook(setup):
    print("This is login by facebook test")
    assert True==True

def test_LoginPhone(setup):
    print("This is login by phone test")
    assert True==True

# insert decorator/annotation '@pytest.mark.skip'  .---> to skip the test function
@pytest.mark.skip
def test_LoginIoS(setup):
    print("This is login IoS phone test")
    assert True==True

# insert decorator/annotation '@pytest.mark.skip'  .---> to skip the test function
@pytest.mark.skip
def test_LoginTablet(setup):
    print("This is login tablet test")
    assert True==True