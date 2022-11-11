#Faça um programa de agenda telefônica, com as classes Agenda e Contato.

from agenda import agenda

agenda = agenda()
listAgenda = []

menu = 1
while (menu !=4):
  print("1 -- Cadastrar contato.")
  print("2 -- Listar todos os contatos.")
  print("3 -- Apagar contato.")
  print("4 -- Sair.")

  menu = int(input("Digite a opção: "))

  if menu == 1:
    nome = input("Digite o nome: ")
    tel = int(input("Digite o telefone: "))
    listAgenda.append(agenda.inserir(nome, tel))

  elif menu == 2:
    agenda.listarTodos(listAgenda)

  elif menu == 3:
    nome = input("Digite o nome para a pesquisa: ")
    print(agenda.deletarNome(listAgenda, nome))

  elif menu == 4:
    break
  else:
    print("Digite uma opção válida! ")

