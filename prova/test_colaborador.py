from colaborador import *
import pytest

@pytest.mark.parametrize("s,t,m,esperado",[
    (3000,4,"123","Junior"),(5000,8,"123","Sênior"),(17000,13,"123","Pleno"),(3000,4,"12h","Matricula invalida")
])
def test_colaborador(s,t,m,esperado):
    assert colaborador(s,t,m) == esperado