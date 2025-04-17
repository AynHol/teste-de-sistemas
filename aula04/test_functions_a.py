from functions_a import *

def test_person_person():
    assert person_person("Wesley Antunes", "48123450000", 20, "wesley@gmail.com") is True
    assert person_person("WesleyAntunes", "47123450000", 20, "wesley!gmail.com") is False

def test_person_values():
    assert person_values(1700,500,400) == 171700
    assert person_values(1400,500,400) == 141400
    assert person_values(2300,500,400) == 232300
    assert person_values(4000,800,750) == 204000

    assert person_values(1700,500,600) == -168300 