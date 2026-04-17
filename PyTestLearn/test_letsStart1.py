# Fixture it is a Re-usable function
#this example has 3 test functions and a fixture (normal function)
# before executing every test function, I want to launch pre-requisite
# -> use annotation @pytest.fixture + pass as argument the fixture to all test functions
# run with cmd line --> pytest PyTestLearn/test_letsStart1.py -s -v

import pytest

@pytest.fixture
def setup_app():
    print("Setting up the app browser")


def test_one(setup_app):
    print("this is my test one")

def test_two(setup_app):
    print("this is my test two")

def test_three(setup_app):
    print("this is my test three")


# Fixture can also return a value

@pytest.fixture
def setup_team():
    print("Setting up the italian QA team....")
    return "Roy and Charlie"

# yield keyword in fixtures
# actions can be done before and after starting the function

@pytest.fixture
def setup_swiss_team():
    print("Setting up the swiss QA team....")
    yield
    print("The swiss team ended the duty ")

def test_one_italian_team(setup_team):  # fixture is passed as argument and as return value
    print("this is my italian team: ",setup_team)

def test_one_swiss_team(setup_swiss_team):
    print("this is my swiss team")

def test_one_french_team():    # this function does not call fixtures
    print("this is my french team")




