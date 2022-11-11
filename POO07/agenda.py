from contato import Contato


class agenda ():
  def inserir(self, nome, telefone):
    return Contato(nome, telefone)

  def listarTodos(self, listaTelefone):
    for tel in listaTelefone:
      print(f"{tel.nome} | {tel.telefone}")


  def deletarNome(self, listaTelefone, nome):
    if len(listaTelefone) != 0:
      cont = 0
      for tel in listaTelefone:
        if tel.nome == nome:
          listaTelefone.pop(cont)
          return "Contado {} removido com sucesso!".format(nome)
        else:
          return "Nome não encontrado!"
    else:
      return "Lista vazia!"