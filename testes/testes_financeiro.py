from main import calcular_sobra
import requests

def test_sobra_correta():
    sobra = calcular_sobra(1000, 200, 200, 100, 100)
    assert sobra == 400

def test_sobra_negativa():
    sobra = calcular_sobra(500, 300, 300, 100, 100)
    assert sobra < 0


def test_api_dolar():
    resposta = requests.get(
        "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    )

    dado = resposta.json()

    assert resposta.status_code == 200
    assert 'USDBRL' in dado