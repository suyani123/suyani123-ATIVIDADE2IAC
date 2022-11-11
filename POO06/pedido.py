class pedido:
    def __init__(self):
        self.listaItens = []
        self.formapagamento = " "

    def adicionarLista(self, selecionado, quantidade):
        self.listaItens.append(compra(selecionado, quantidade))
    def selecionarformaDpagamento(self, tipoPagamento):
        self.formapagamento = tipoPagamento

class compra:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade