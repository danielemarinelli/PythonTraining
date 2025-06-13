import pytest

# with this the prints will execute after every test case (at test case/method level)
#@pytest.fixture()
#def setup():
#    print("@@@@@@@@@@@@@@@@@  I will be executing first.... setup!!")
#    yield
#    print("@@@@@@@@@@@@@@@@@  I will be executed last.... tear_down!!")

# if want to insert the execution before and after class (at class level) insert 'scope=class' in annotation

@pytest.fixture(scope="class")
def setup():
    print("@@@@@@@@@@@@@@@@@  I will be executing first.... setup!!")
    yield
    print("@@@@@@@@@@@@@@@@@  I will be executed last.... tear_down!!")


@pytest.fixture()
def datasetLoad():
    print("user dataset profile is being loaded")
    return ["Daniele","Marinelli","rahulshettyaccademy.com"]  #return tuple

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param






