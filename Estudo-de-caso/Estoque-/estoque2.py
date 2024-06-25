class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, quantidade):
        if nome in self.itens:
            self.itens[nome] += quantidade
        else:
            self.itens[nome] = quantidade

    def remover_item(self, nome, quantidade):
        if nome in self.itens and self.itens[nome] >= quantidade:
            self.itens[nome] -= quantidade
            if self.itens[nome] == 0:
                del self.itens[nome]

    def exibir_estoque(self):
        for nome, quantidade in self.itens.items():
            print(f"{nome}: {quantidade}")

if __name__ == "__main__":
    estoque = Estoque()
    estoque.adicionar_item("Maçã", 10)
    estoque.adicionar_item("Banana", 20)
    estoque.remover_item("Maçã", 5)
    print("Estoque atual:")
    estoque.exibir_estoque()