'''
PyTest
------------
PyTest is a python framework by which we can use certain features in automation..

1) Fixtures
2) Skip the tests
3) ordering the tests
4) Group the tests
5) Parallel testing

install pytest
--------------
pip install pytest
pip uninstall pytest

Naming conventions
-------------------
1) module (.py file) name should start with "test_"
	Ex:  test_example.py   or example_test.py
2) Class name should start with "Test"
	Ex: TestClass
3)  Test function name should start with "test_"
	def test_example()
'''

import pytest

def test_one():
    print("this is my test one")

def test_two():
    print("this is my test two")

def test_three():
    print("this is my test three")


# class TestClass:
#     def test_one(self):
#         print("this is my test one")
#
#     def test_two(self):
#         print("this is my test two")
#
#     def test_three(self):
#         print("this is my test three")


'''
To run all the tests in the module
    pytest test_demos.py
    pytest test_demos.py -s
    pytest test_demos.py -s -v

To run specific test in the module
    pytest test_demos.py::test_one -s -v
    pytest test_demos.py::test_two -s -v
    pytest test_demos.py::test_three -s -v

-s  : you can see all print() outputs live in the console while the test runs.
-v :  Runs pytest in verbose mode. Shows detailed test execution information.

'''

