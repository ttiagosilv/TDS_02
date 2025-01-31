import pytest
from contas import ContaCorrente, ContaPoupanca

@pytest.fixture
def conta_corrente():
    return ContaCorrente(123, 500)

@pytest.fixture
def conta_poupanca():
    return ContaPoupanca(456, 1000, 5)

def test_creditar(conta_corrente):
    conta_corrente.creditar(200)
    assert conta_corrente.saldo() == 700

def test_debitar(conta_corrente):
    conta_corrente.debitar(100)
    assert conta_corrente.saldo() == 400
    conta_corrente.debitar(500)
    assert conta_corrente.saldo() == 400

def test_transferir(conta_corrente, conta_poupanca):
    conta_corrente.transferir(200, conta_poupanca)
    assert conta_corrente.saldo() == 300
    assert conta_poupanca.saldo() == 1200
    conta_corrente.transferir(500, conta_poupanca)
    assert conta_corrente.saldo() == 300

def test_render_juros(conta_poupanca):
    conta_poupanca.render_juros()
    assert conta_poupanca.saldo() == 1050
