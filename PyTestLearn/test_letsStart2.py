# Fixture it is a Re-usable function
# Scope of a fixture:
# scope="function" (default) fixture will be called before EVERY test function executes (mostly used)
# scope="module"   fixture will be called ONLY ONCE before test functions executes  (mostly used)
# scope="class"   fixture will be called only once before the CLASS
# scope="session"  fixture will be called only once for session

# def are called Functions if they are not inside a class and
# are called methods if they are inside a class
# module --> class --> methods
# module --> function
# run with cmd line --> pytest PyTestLearn/test_letsStart1.py -s -v

import pytest

@pytest.fixture
def setup_app(scope='module'):
    print("Setting up the app browser")

def test_one(setup_app):
    print("this is my test one")

def test_two(setup_app):
    print("this is my test two")

def test_three(setup_app):
    print("this is my test three")


