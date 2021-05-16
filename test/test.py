import pytest
import sys
sys.path.append('srcs')
from app import addition

def test_addition():
    actual = addition(3, 4)
    exceeded = 7
    assert exceeded == actual

def test_addition2():
    actual = addition(-1, 2)
    exceeded = 1
    assert exceeded == actual

def test_addition3():
    actual = addition(1, -2)
    exceeded = -1
    assert exceeded == actual

def test_addition3():
    actual = addition(0, 0)
    exceeded = 0
    assert exceeded == actual

def test_abnormal():
    actual = addition('a', 1)
    exceeded = 'Invalid input'
    assert exceeded == actual

def test_abnormal2():
    actual = addition(1, 'b')
    exceeded = 'Invalid input'
    assert exceeded == actual