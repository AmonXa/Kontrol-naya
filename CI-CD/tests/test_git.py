from app import greeting, add, sub, mult

def test_greet():
    assert greeting("HM") == "Hola HM!"

def test_add():
    assert add(22, 16) == 38

def test_sub():
    assert sub(50, 45) == 5

def test_mult():
    assert mult(20, 10) == 200