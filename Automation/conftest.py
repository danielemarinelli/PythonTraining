
import pytest
from selenium.webdriver.chrome import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


@pytest.fixture(scope="session")
def browserInstance(request):
    # 'request' in pytest reads the options of global variable passed from
    # command line --> command to launch the framework is:
    # pytest test_e2eTestFramework.py --browser_name firefox
    # I can send 'n' number of options from command line
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver  #till line 25 will be executed BEFORE the test execution
    driver.close() #line 26 will be executed after the execution of the test