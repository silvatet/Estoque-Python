class Produto:
    def __init__(self, codigo, nome, preco, quantidade, cor, tipo):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.cor = cor
        self.tipo = tipo

    def __str__(self):
        return f"Produto {self.nome} (Código: {self.codigo}) - Preço: R$ {self.preco:.2f} - Quantidade: {self.quantidade} unidade(s) - Cor: {self.cor} - Tipo: {self.tipo}"


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print(f"Produto {produto.nome} removido com sucesso!")
                return
        print("Produto não encontrado!")

    def consultar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(produto)
                return
        print("Produto não encontrado!")

    def consultar_estoque(self):
        print("Estoque atual:")
        for produto in self.produtos:
            print(produto)

    def atualizar_quantidade(self, codigo, quantidade):
        for produto in self.produtos:
            if produto.codigo == codigo:
                produto.quantidade = quantidade
                print(f"Quantidade do produto {produto.nome} atualizada para {quantidade} unidade(s)!")
                return
        print("Produto não encontrado!")

    def vender_produto(self, codigo, quantidade):
        for produto in self.produtos:
            if produto.codigo == codigo:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    print(f"Venda de {quantidade} unidade(s) do produto {produto.nome} realizada com sucesso!")
                    return
                print("Quantidade insuficiente em estoque!")
                return
        print("Produto não encontrado!")


def main():
    estoque = Estoque()

    # Adicionando produtos iniciais
    estoque.adicionar_produto(Produto(1, "Tinta Azul", 10.99, 50, "Azul", "Acrylic"))
    estoque.adicionar_produto(Produto(2, "Tinta Vermelha", 12.99, 30, "Vermelho", "Óleo"))
    estoque.adicionar_produto(Produto(3, "Tinta Amarela", 9.99, 20, "Amarelo", "Acrylic"))
    estoque.adicionar_produto(Produto(4, "Tinta Verde", 11.99, 40, "Verde", "Óleo"))
    estoque.adicionar_produto(Produto(5, "Tinta Preta", 8.99, 60, "Preto", "Acrylic"))

    while True:
        print("\nOpções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Consultar produto")
        print("4. Consultar estoque")
        print("5. Atualizar quantidade")
        print("6. Vender produto")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = int(input("Digite o código do produto: "))
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            cor = input("Digite a cor do produto: ")
            tipo = input("Digite o tipo do produto (Acrylic ou Óleo): ")
            produto = Produto(codigo, nome, preco, quantidade, cor, tipo)
            estoque.adicionar_produto(produto)
        elif opcao == "2":
            codigo = int(input("Digite o código do produto a remover: "))
            estoque.remover_produto(codigo)
        elif opcao == "3":
            codigo = int(input("Digite o código do produto a consultar: "))
            estoque.consultar_produto(codigo)
        elif opcao == "4":
            estoque.consultar_estoque()
        elif opcao == "5":
            codigo = int(input("Digite o código do produto a atualizar: "))
            quantidade = int(input("Digite a nova quantidade do produto: "))
            estoque.atualizar_quantidade(codigo, quantidade)
        elif opcao == "6":
            codigo = int(input("Digite o código do produto a vender: "))
           
        elif opcao == "6":
            codigo = int(input("Digite o código do produto a vender: "))
            quantidade = int(input("Digite a quantidade do produto a vender: "))
            estoque.vender_produto(codigo, quantidade)
        elif opcao == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente!")


if __name__ == "__main__":
    main()