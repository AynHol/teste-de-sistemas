def positivo(numero):
    return numero>0

def test_positivo():
    assert positivo(5) is True
    assert positivo(-5) is False