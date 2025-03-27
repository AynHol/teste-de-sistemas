def grande(letra):
    return "A" in letra

def test_grande():
    assert grande("A") is True
    assert grande("a") is False

# tristeza não funcional