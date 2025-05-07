class Financeiro:
    def __init__(self):
        self.devido = 0
        self.pago = 0
    
    def regitroDebito(self, valor):
        self.devido += valor
    
    def registroPagamento (self, valor):
        self.pago += valor
    
    def saldoPendente(self):
        return self.devido - self.pago