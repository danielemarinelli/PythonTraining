import pytest

# re-use fixture in all modules. It's a common fixture and available from all
# the test modules. The fix name of file must be conftest.py , now this file
# contains all fixtures that are available for all modules across all package


@pytest.fixture()
def setup():
    print("phone env up and running...")
    yield
    print("tear down phone env after testing...")

