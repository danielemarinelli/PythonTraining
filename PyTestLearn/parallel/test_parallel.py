'''
Pre-requisite:  Install a pytest plugin "pytest-xdist" to run tests parallel
pip install pytest-xdist
'''

def test_one():
    print("running test one")
    assert True

def test_two():
    print("Running test two")
    assert True

def test_three():
    print("Running test three")
    assert True

def test_four():
    print("Running test four")
    assert True

def test_five():
    print("Running test 5")
    assert True

def test_six():
    print("Running test 6")
    assert True


'''
To run the tests parallely:
specify the number of workers!
in serial execution one worker receives the tests and execute them all one by one
in parallel execution (increasing the workers n=2) the execution is faster , 
in this example (tot 6 tests) one worker
executes the first 3 tests and the other workers executes the other 3 
but more workers are there and SLOW PERFORMANCE will have the framework because workers get memory
maximum 5 workers are ok for 100-200 tests


    pytest PyTestLearn/parallel/test_parallel.py -v -s -n=2 
    pytest PyTestLearn/parallel/test_parallel.py -v -s -n 3 

'''