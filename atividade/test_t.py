import pytest
from aluno import Aluno
from financeiro import Financeiro

def test_media():
    aluno = Aluno("Wesley")
    aluno.novaNota(9)
    aluno.novaNota(6)
    assert aluno.mediaEnd() == 7.5

def test_media_sem_nota():
    aluno = Aluno("Bruno")
    assert aluno.mediaEnd() == 0.0

def test_modificar_nota():
    aluno = Aluno("Maria")
    aluno.novaNota(5)
    aluno.modificarNota(0, 8)
    assert aluno.mediaEnd() == 8.0

def test_saldo():
    conta = Financeiro()
    conta.regitroDebito(800)
    conta.registroPagamento(300)
    assert conta.saldoPendente() == 500

def test_saldo_sem_pagamento():
    conta = Financeiro()
    conta.regitroDebito(200)
    assert conta.saldoPendente() == 200

def test_fluxo_completo_estudante_e_financeiro():
    aluno = Aluno("João")
    aluno.novaNota(7)
    aluno.novaNota(9)
    aluno.modificarNota(1, 10)

    financeiro = Financeiro()
    financeiro.regitroDebito(1000)
    financeiro.registroPagamento(250)

    assert aluno.mediaEnd() == 8.5
    assert financeiro.saldoPendente() == 750