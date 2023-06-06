import pytest
from function import f

def test():
    # Prueba 
    assert f(["casa","carro","perro"]) == ["CASA", "CARRO"]
    assert f(["casa","carro","perro","persona","caminar","ingenieria"]) == ["CASA", "CARRO", "CAMINAR"]
    assert f(["persona","perro","ingenieria"]) == []
    