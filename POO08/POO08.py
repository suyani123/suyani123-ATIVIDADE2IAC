#Faça um programa para controle de empréstimo de livros, com as classes Empréstimo, Livro e Pessoa.
from livrosDB import livrosDB


DB = livrosDB()
DB.gerarBD()

menu = 1
while (menu !=4):

  print("1 - Listar todos livros")
  print("2 - Realizar Empréstimo")
  print("3 - Devolver livro.")
  print("4 - Sair.")

  menu = int(input("Digite a opção: "))

  if menu == 1:
      for item in DB.estoqueLivro:
        print(f"Código do item: {item.codigo}. Livro: {item.nome}. Autor: {item.autor}. Gênero: {item.genero}. Ano: {item.ano}. Quantidade: {item.qtd}")

  elif menu == 2:
      nome = input("Digite o nome: ")
      telefone = int(input("Digite o telefone: "))
      codLivro = int(input("Digite o código do livro: "))
      dataEmprest = (input("Digite a data do empréstimo: "))
      dataDevol = (input("Digite a data que você irá devolver o livro: "))

      if (DB.verificarEstoque(codLivro)):
        DB.realizarEmp(nome, telefone, codLivro, dataEmprest, dataDevol)
        DB.retirarEstoque(codLivro)
      else:
          print("Não possui quantidade disponível no estoque.")


  elif menu == 3:
      nome = input("Digite o nome para confirmar a devolução:")
      codLivro = int(input("Digite o código do livro:"))
      print(DB.devolucao(nome, codLivro))
      DB.devolverEstoque(codLivro)

  elif menu == 4:
      break
  else:
      print("Digite uma opção válida!")