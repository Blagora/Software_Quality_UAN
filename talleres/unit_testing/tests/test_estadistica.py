import pytest
from src.estadistica import calcular_promedio

def test_tipo_retorno_float():
    res = calcular_promedio([1, 2, 3])
    assert isinstance(res, float)
    assert res == 2.0

def test_valor_correcto_tres_numeros():
    assert calcular_promedio([1, 2, 3]) == 2.0
    assert calcular_promedio([10, 20, 30]) == 20.0
    assert calcular_promedio([0, 0, 0]) == 0.0

def test_valor_correcto_numeros_negativos():
    assert calcular_promedio([-2, -4]) == -3.0
    assert calcular_promedio([-10, 10]) == 0.0
    assert calcular_promedio([-5, -5, -5]) == -5.0

def test_lista_vacia_retorna_none():
    assert calcular_promedio([]) is None

def test_un_elemento():
    assert calcular_promedio([5]) == 5.0
    assert calcular_promedio([0]) == 0.0
    assert calcular_promedio([-10]) == -10.0

def test_multiples_valores():
    assert calcular_promedio([1, 2, 3, 4, 5]) == 3.0
    assert calcular_promedio([100, 200, 300]) == 200.0

def test_no_lanza_excepcion():
    try:
        calcular_promedio([5])
    except Exception:
        pytest.fail("No debería lanzar excepción")