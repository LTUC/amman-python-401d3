from guessing_game import __version__
from guessing_game.game import add2, add5

def test_version():
    assert __version__ == '0.1.0'

def test_add2():
    # Arrange - any setup for running my code
    number = 3
    expected = 5
    # Assign
    actual  =  add2(number)
    # Assert
    assert expected == actual

def test_add5():
    # Arrange - any setup for running my code
    number = 3
    expected = 8
    # Assign
    actual  =  add5(number)
    # Assert
    assert expected == actual