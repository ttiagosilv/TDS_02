class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def __str__(self):
        return f"Conta número: {self.numero}, Saldo: R${self.saldo:.2f}"

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def saldo(self):
        return self.saldo

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.debitar(valor)
            conta_destino.creditar(valor)
        else:
            print("Saldo insuficiente para transferência.")


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo=0, taxa_juros=0):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros

    def __str__(self):
        return f"{super().__str__()}, Taxa de juros: {self.taxa_juros}%"

    def render_juros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)
