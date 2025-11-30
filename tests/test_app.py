import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import hello_world, add_numbers

def test_hello_world():
    """Test funkcji hello_world"""
    result = hello_world()
    assert "Hello, World!" in result
    assert True  # Dummy test

def test_add_numbers():
    """Test funkcji add_numbers"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert True  # Dummy test

def test_dummy():
    """Przykładowy test dummy"""
    assert True

# def test_failing_test():
#     """Test który zawsze failuje"""
#     assert False, "Celowy fail do testowania powiadomień"