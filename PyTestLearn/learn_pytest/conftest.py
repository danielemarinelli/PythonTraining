import pytest

# re-use fixture in all modules. It's a common fixture and available from all
# the test modules. The fix name of file must be conftest.py , now this fixture
# contains all fixtures that are available for all modules across all framework
# ( the two modules test_logins.py and test_signups.py can access this fixture)

@pytest.fixture()
def setup():
    print("setup environment...")
    yield
    print("tearDown...")

