from voto import *

def test_voto():
    assert voto(15) == "NÃO PODE VOTAR"
    assert voto(16) == "PODE VOTAR"
    assert voto(24) == "DEVE VOLTAR MAS NÃO PODE SER PRESIDENTE"
    assert voto(58) == "DEVE VOTAR E PODE SER PRESIDENTE"
    assert voto(72) == "PODE VOTAR E PODE SER PRESIDENTE"