# Estoque-UNIFECAF
Esse é um estudo de caso em Python 

Estoque Simples em Python
Este é um projeto simples de um sistema de controle de estoque em Python. O sistema permite adicionar itens ao estoque, remover itens e exibir o estoque atual.

Funcionalidades
Adicionar itens ao estoque.
Remover itens do estoque.
Exibir o estoque atual.
Requisitos
Python 3.x
Como Usar
Clone o repositório:

bash
Copiar código
git clone 
cd estoque-simples
Execute o programa:

bash
Copiar código
python estoque.py
Código de Exemplo
Aqui está um exemplo simples de como o estoque é implementado em Python:

python
Copiar código
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
