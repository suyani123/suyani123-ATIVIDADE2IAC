#POO_06 - Identifique as classes e implemente um programa para a seguinte
#especificação: “O supermercado vende diferentes tipos de produtos. Cada produto
#tem um preço e uma quantidade em estoque. Um pedido de um cliente é composto
#de itens, onde cada item especifica o produto que o cliente deseja e a respectiva
#quantidade. Esse pedido pode ser pago em dinheiro, cheque ou cartão

from POO06.formapagamento import formapagamento
from POO06.pedido import pedido
from POO06.EstoqueDB import EstoqueDB



DB = EstoqueDB()
DB.gerarEstoque()
pedido = pedido()
formapagamento = formapagamento()
formapagamento.gerarPagamento()


opcao = 3
while (opcao !=2):

    for item in DB.estoqueProd:
        if (item.quantidade > 0):
            print(f"Código do item: {item.codigo}. Produto: {item.nome}. Valor unitário: R${item.preco:.2f}. Quantidade em estoque: {item.quantidade}")

    selecionado = int(input("Digite o código do produto: "))
    Quantidade = int(input("Digite a quantidade do produto: "))

    if (DB.verificarEstoque(selecionado, Quantidade)):
        pedido.adicionarLista(selecionado, Quantidade)
        DB.retirarEstoque(selecionado, Quantidade)

    else:
        print("Não possui quantidade disponível no estoque.")

    print("1. Continuar comprando? ")
    print("2. Finalizar Compra? ")
    opcao = int(input("Digite a opção: "))

for item in formapagamento.formaDpagamento:
    print(f"{item.codigo}. {item.nome}. ")

pagSelecionado = int(input("Seleciona a forma de pagamento: "))

if (pagSelecionado == 1 or pagSelecionado == 2 or pagSelecionado == 3):
    print("Pagamento realizado com sucesso!")
else:
    print("Pagamento não aprovado!")
