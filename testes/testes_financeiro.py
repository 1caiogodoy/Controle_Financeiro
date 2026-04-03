from main import calcular_sobra

def test_sobra_correta():
    sobra = calcular_sobra(1000, 200, 200, 100, 100)
    assert sobra == 400

def test_sobra_negativa():
    sobra = calcular_sobra(500, 300, 300, 100, 100)
    assert sobra < 0