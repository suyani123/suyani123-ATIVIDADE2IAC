class formapagamento:
    formaDpagamento = []

    def gerarPagamento(self):

        self.formaDpagamento.append(pagamento(1, "Dinheiro "))
        self.formaDpagamento.append(pagamento(2, "Cheque "))
        self.formaDpagamento.append(pagamento(3, "Cartão "))

class pagamento:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome