from linux_commands import ls,pip
from pytest import raises

def test_ls():
    result=ls('tests')
    assert result==('__pycache__','tests.py') or result=='tests.py'

def test_ll():
    result=ls('tests',l=True)
    assert len(result)==3
    assert isinstance(result[1][1],int)
    assert result[1][-1]=='tests.py' or result[1][-1]=='__pycache__'

def test_composition():
    assert len(pip.freeze())>0

def test_error():
    with raises(OSError):
        pip.lol()
