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
    with pytest.raises(TypeError):
        addition('a', 1)

def test_abnormal2():
    with pytest.raises(TypeError):
        addition(1, 'b')
