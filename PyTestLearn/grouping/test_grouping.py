
'''
grouping tests:
--------------
every test can be grouped with markers @pytest.mark.'some_custom_name'
while grouping tests a pytest.ini file must be created with the markers
so that warning won't show in the results
'''

import pytest


@pytest.mark.testing_sanity
@pytest.mark.testing_regression
def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1

@pytest.mark.e2e_testing
def test_loginbyfacebook():
    print("this is login by facebook")
    assert 1 == 1

@pytest.mark.phone
def test_loginbyphone(setup):
    print("this is login by phone")
    assert 1 == 1


@pytest.mark.testing_sanity
@pytest.mark.testing_regression
def test_signupbyemail():
    print("This is signup by email test")
    assert True == True


@pytest.mark.e2e_testing
def test_signupbyfacebook():
    print("This is signup by facebook test")
    assert True == True

@pytest.mark.phone
def test_signupbyphone(setup):
    print("This is signup by phone test")
    assert True == True


@pytest.mark.testing_regression
def test_paymentindollars():
    print("this is payment in dollars test")
    assert 1==1

@pytest.mark.e2e_testing
def test_paymentineuros():
    print("this is payment in euros test")
    assert 1==1



'''
1) run sanity tests
     pytest PyTestLearn/grouping/test_grouping.py -v -s -m "testing_sanity"
     
2) run only regression tests 
    pytest PyTestLearn/grouping/test_grouping.py -v -s -m "testing_regression"

3) run tests which belong to both sanity and regression
    pytest PyTestLearn/grouping/test_grouping.py -v -s -m "testing_sanity and testing_regression" -m "not e2e_testing and phone"
    
4) run only sanity tests which don't belong to regression
    pytest PyTestLearn/grouping/test_grouping.py -v -s -m "testing_sanity" -m "not testing_regression"

5) run only regression which don't belongs to sanity
    pytest PyTestLearn/grouping/test_grouping.py -v -s -m "testing_regression and e2e_testing and phone" -m "not testing_sanity"

'''
