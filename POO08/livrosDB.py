from Livro import livro
from Pessoa import pessoa
from Emprestimo import emprestimo

class livrosDB:
    listPessoa = []
    listEmprestimo = []

    estoqueLivro = []
    def gerarBD(self):
        self.estoqueLivro.append(livro(1, "Harry Potter e as reliquias da morte", "JK Roling", "Fantasia", 2007, 4))
        self.estoqueLivro.append(livro(2, "Crepusculo", "Stephenie Meyer", "Fantasia", 2008, 1))
        self.estoqueLivro.append(livro(3, "Anna Kariênina", " Liev Tolstói", "Romance", 1877, 3))
        self.estoqueLivro.append(livro(4, "A Menina que Roubava Livros", "Markus Zusak", "Drama", 2007, 1))
        self.estoqueLivro.append(livro(5, "Crime e castigo", "Paulo Bezerra", "Romance", 1886, 2))
        self.estoqueLivro.append(livro(6, "Laranja Mecânica", "Anthony Burgess", "Romance", 1986, 8))
        self.estoqueLivro.append(livro(7, "Orgulho e Preconceito", "Jane Austen", "Romance", 1813, 4))
        self.estoqueLivro.append(livro(8, "Moby Dick", "Herman Melville", "Aventura", 1851, 3))
        self.estoqueLivro.append(livro(9, "Alice no País das Maravilhas", "Lewis Carroll", "Aventura", 1856, 2))
        self.estoqueLivro.append(livro(10, "O Iluminado", "Stephen King", "Romance", 1977, 14))
        self.estoqueLivro.append(livro(11, "Medo Clássico", "Edgar Allan Poe", "Terror", 2017, 3))
        self.estoqueLivro.append(livro(12, "Horror em Amityville", "Jay Anson", "Terror", 1977, 20))
        self.estoqueLivro.append(livro(13, "O Desfiladeiro do Medo", "Clive Barker", "Terror", 2003, 21))
        self.estoqueLivro.append(livro(14, "O Chamado de Cthulhu", "H.P Lovecraft", "Terror", 1927, 10))


    def realizarEmp(self, nome, telefone, livro, dataEmprest, dataDevol):
        for item in self.estoqueLivro:
            if(item.codigo == livro):
                self.listPessoa.append(pessoa(nome, telefone))
                self.listEmprestimo.append(emprestimo(livro, nome, dataEmprest, dataDevol))
                print("Empréstimo realizado com sucesso! ")
                return
        print("Código não encontrado!")


    def devolucao (self, nome, codLivro):
        if len(self.listEmprestimo) != 0:
            cont = 0
            for item in self.listEmprestimo:
                if item.codLivro == codLivro and item.nomePessoa == nome:
                    self.listEmprestimo.pop(cont)
                    return "Devolução feita com sucesso!".format(nome)
                else:
                    return "Empréstimo não encontrado!"

    def verificarEstoque(self, codigo):
        for item in self.estoqueLivro:
            if(item.codigo == codigo and item.qtd >= 1):
                return True

        return False



    def retirarEstoque(self, codigo):
        for item in self.estoqueLivro:
            if (item.codigo == codigo):
                item.qtd = item.qtd - 1

    def devolverEstoque(self, codigo):
        for item in self.estoqueLivro:
            if (item.codigo == codigo):
                item.qtd = item.qtd + 1