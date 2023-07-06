import pytest
from cod1 import divide

def test_divide():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
        divide(2, 0)
        