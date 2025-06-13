import pytest

from PytestDemo.conftest import datasetLoad


@pytest.mark.usefixtures("datasetLoad")
class TestExample2:

    def test_editProfile(self, datasetLoad):
        print(datasetLoad)
        print(datasetLoad[2])


