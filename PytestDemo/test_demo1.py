# Any pytest file should start with KEYWORD -> test_
#                           or end with _test
# Pytest method names should start with KEYWORD -> test
# these are Test Cases

def test_firstProgram(setup):
    print("Hello World")


def test_secondProgram():
    print("Good morning World!!!")


def test_multiBrowser(crossBrowser):
    print(crossBrowser)

