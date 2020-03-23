from FlaskPythonOOP import Main


def test_hello():
    hello = Main.hello.hi()
    assert hello == "Hello world"
