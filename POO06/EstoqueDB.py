from produto import produto


class EstoqueDB:

    estoqueProd = []
    def gerarEstoque(self):
        self.estoqueProd.append(produto(1, "Batata Frita", 24, 5))
        self.estoqueProd.append(produto(2, "Arroz", 21.50, 1))
        self.estoqueProd.append(produto(3, "Chocolate", 6.75, 30))
        self.estoqueProd.append(produto(4, "Sorvete", 27.80, 2))
        self.estoqueProd.append(produto(5, "Feijão", 5.50, 5))
        self.estoqueProd.append(produto(6, "Filé de Frango", 6.75, 9))
        self.estoqueProd.append(produto(7, "Desodorante", 17.40, 2))
        self.estoqueProd.append(produto(8, "Banana", 3.99, 1))
        self.estoqueProd.append(produto(9, "Miojo", 3.99, 45))
        self.estoqueProd.append(produto(10, "Detergente", 7.50, 9))
        self.estoqueProd.append(produto(11, "Shampoo", 3.50, 6))
        self.estoqueProd.append(produto(12, "Espetos", 6.85, 4))
        self.estoqueProd.append(produto(13, "Cadeira de praia", 30, 3))
        self.estoqueProd.append(produto(14, "Toamte", 1.99, 6))
        self.estoqueProd.append(produto(15, "Condimentos", 1.50, 18))
        self.estoqueProd.append(produto(16, "Pente de cabelo", 4.80, 1))
        self.estoqueProd.append(produto(17, "Carneiro", 44.50, 1))
        self.estoqueProd.append(produto(18, "Creme Dental", 7.15, 4))


    def verificarEstoque(self, codigo, quantidade):
        for item in self.estoqueProd:
            if(item.codigo == codigo and item.quantidade >= quantidade):
                return True

        return False

    def retirarEstoque(self, codigo, quantidade):
        for item in self.estoqueProd:
            if (item.codigo == codigo):
                item.quantidade = item.quantidade - quantidade
