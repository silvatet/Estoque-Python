# Estoque-UNIFECAF
=====================

## Visão Geral

Este é um estudo de caso em Python que implementa um sistema de controle de estoque simples. O sistema permite adicionar itens ao estoque, remover itens e exibir o estoque atual.

## Funcionalidades

* **Adicionar itens ao estoque**: permite adicionar novos itens ao estoque com suas respectivas quantidades.
* **Remover itens do estoque**: permite remover itens do estoque com suas respectivas quantidades.
* **Exibir o estoque atual**: permite exibir o estoque atual com os itens e suas quantidades.

## Requisitos

* **Python 3.x**: necessário para executar o sistema.

## Como Usar

### Clone o repositório

## Código de Exemplo

Aqui está um exemplo simples de como o estoque é implementado em Python:
```python
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
