import pytest


#instead of passing fixture 'setup' in all methods arguments, let's create a class
#that contains all methods and fixture is passed only once with class
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will be executing test_fixtureDemo, but first gotta launch commands under setup()")

    def test_fixtureDemo2(self):
        print("I will be executing test_fixtureDemo2, but first gotta launch commands under setup()")

    def test_fixtureDemo3(self):
        print("I will be executing test_fixtureDemo3, but first gotta launch commands under setup()")

    def test_fixtureDemo4(self):
        print("I will be executing test_fixtureDemo4, but first gotta launch commands under setup()")


#def test_fixtureDemo(setup):
#    print("I will be executing test_fixtureDemo, but first gotta launch commands under setup()")


#def test_fixtureDemo2(setup):
#    print("I will be executing test_fixtureDemo2, but first gotta launch commands under setup()")


#def test_fixtureDemo3(setup):
#    print("I will be executing test_fixtureDemo3, but first gotta launch commands under setup()")


#def test_fixtureDemo4(setup):
#    print("I will be executing test_fixtureDemo4, but first gotta launch commands under setup()")

