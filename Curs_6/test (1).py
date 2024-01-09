import new_fizz

def test_unu():
    assert new_fizz.fizzbuzz(1) == 1
    
def test_trei():
    assert new_fizz.fizzbuzz(3) == "fizz"
    
def test_cinci():
    assert new_fizz.fizzbuzz(5) == "buzz"