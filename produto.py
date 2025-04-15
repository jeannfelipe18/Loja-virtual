import time

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def reduzir_estoque(self, quantidade):
        if 0 < quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print(" Estoque insuficiente!")

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto: Produto, quantidade: int):
        if produto.quantidade >= quantidade:
            valor_total = produto.preco * quantidade
            self.itens.append((produto, quantidade, valor_total))
            print(f" {quantidade}x {produto.nome} adicionado(s) ao seu carrinho. Total: R${valor_total:.2f}")
        else:
            print(" Estoque insuficiente!")

    def mostrar_carrinho(self):
        if not self.itens:
            print(" Carrinho vazio!")
        else:
            print("\n Seu Carrinho:")
            for produto, quantidade, preco in self.itens:
                print(f"{quantidade}x {produto.nome} - Total: R${preco:.2f}")

    def calcular_total(self):
        return sum(preco for _, _, preco in self.itens)

    def finalizar_compra(self, metodo_pagamento: str, parcelas: int = 1):
        if not self.itens:
            print(" Carrinho vazio! Adicione itens antes de finalizar a compra.")
            return

        total = self.calcular_total()
        pagamento = Pagamento()
        valor_total = pagamento.processar_pagamento(total, metodo_pagamento, parcelas)

        if valor_total is not None:
            for produto, quantidade, _ in self.itens:
                produto.reduzir_estoque(quantidade)
            print(f" Compra finalizada! Total: R${valor_total:.2f}")
            self.itens.clear()

class Pagamento:
    def processar_pagamento(self, total: float, metodo: str, parcelas: int = 1):
        if metodo.lower() in ["pix", "dinheiro"]:
            total *= 0.90
            print(" Pagamento à vista: 10% de desconto aplicado!")

        elif metodo.lower() == "cartão":
            if parcelas > 1:
                juros = 0.05 * (parcelas - 1)
                total *= (1 + juros)
                print(f" Pagamento parcelado em {parcelas}x. Acréscimo de {juros * 100:.1f}%.")
            else:
                print(" Pagamento no cartão à vista, sem acréscimo.")
        else:
            print(" Método de pagamento inválido!")
            return None
        valor_pago = input("Digite o valor pago: ")
        try:
            valor_pago = float(valor_pago)
            if valor_pago < total:
                print(f"Valor insuficiente! Faltam R${total - valor_pago:.2f}")
                return None
            troco = valor_pago - total
            print(f"Pagamento recebido. Troco: R${troco:.2f}")
        except ValueError:
            print("Valor inválido!")
            return None

        return total

estoque = [
    Produto("Notebook", 3300.00, 10),
    Produto("Teclado", 200.00, 15),
    Produto("Mouse", 100.00, 20),
    Produto("Monitor", 1200.00, 5)
]

carrinho = CarrinhoDeCompras()
