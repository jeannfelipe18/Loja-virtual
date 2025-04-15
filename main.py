from produto import *

def exibir_menu():
    while True:
        print("\n Loja de informatica - MENU")
        print("1 Lista de produtos disponíveis")
        print("2 Adicionar produto ao carrinho")
        print("3 Verificar carrinho")
        print("4 Simulador de pagamento")
        print("5 Finalizar a compra")
        print("6 Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n Produtos Disponíveis:")
            for i, produto in enumerate(estoque):
                print(f"{i + 1}. {produto.nome} - R${produto.preco:.2f} | Estoque: {produto.quantidade}")

        elif escolha == "2":
            try:
                indice = int(input("Digite o número do produto: ")) - 1
                if 0 <= indice < len(estoque):
                    quantidade = int(input("Digite a quantidade desejada: "))
                    carrinho.adicionar_item(estoque[indice], quantidade)
                else:
                    print(" Produto inválido!")
            except ValueError:
                print(" Entrada inválida! Digite um número válido.")

        elif escolha == "3":
            carrinho.mostrar_carrinho()

        elif escolha == "4":
            total = carrinho.calcular_total()
            print(f"\n Valor total atual do carrinho: R${total:.2f}")
            metodo = input("Escolha sua forma de pagamento (pix/dinheiro/cartão): ").strip().lower()
            parcelas = 1
            if metodo == "cartão":
                try:
                    parcelas = int(input("Em quantas vezes deseja parcelar? "))
                except ValueError:
                    print(" Número de parcelas inválido!")
                    continue
            pagamento = Pagamento()
            total_simulado = pagamento.processar_pagamento(total, metodo, parcelas)
            if total_simulado is not None:
                print(f" Valor total do pagamento: R${total_simulado:.2f}")

        elif escolha == "5":
            metodo = input("Escolha a forma de pagamento (pix/dinheiro/cartão): ").strip().lower()
            parcelas = 1
            if metodo == "cartão":
                try:
                    parcelas = int(input("Em quantas vezes deseja parcelar? "))
                except ValueError:
                    print(" Número de parcelas inválido!")
                    continue
            carrinho.finalizar_compra(metodo, parcelas)

        elif escolha == "6":
            print(" Obrigado por visitar a nossa loja")
            break

        else:
            print(" Opção inválida! Tente novamente.")

        time.sleep(1)

exibir_menu()
