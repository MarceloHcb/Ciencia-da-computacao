def mdcR(a, b):
    if b == 0:
        return a
    return mdcR(b, a % b)

#iterativa 
def mdcI(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def test_mdc():
    assert mdcR(2,4) == 2
    assert mdcI(2,4) == 2

if __name__ == "__main__":
    print(mdcR(2,4))
    print(mdcI(2,4))