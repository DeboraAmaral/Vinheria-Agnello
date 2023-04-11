# Solicitando os dados ao cliente
print()
print("\033[33m *************************** BEM-VINDO(A) À VINHEIRA AGNELLO *************************** \033[0;0m")
print()
user = input("\033[1m- Digite o seu nome completo: \033[0;0m")
def obter_inteiro(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print()
            print("\033[31m**** Entrada inválida. Digite um número inteiro.****\033[0;0m")
            print()
idade = obter_inteiro("\033[1m- Qual a sua idade? \033[0;0m")

# Conferindo se o cliente é maior de idade
if idade < 18:
    print()
    print("\033[31m* Você ainda é menor de idade, é proibida a venda de bebidas alcoólicas a menores!! :( *\033[0;0m")
    print()
    print("\033[32m---- COMPRA FINALIZADA ----\033[0;0m")

# Solicitando a quantidade de itens     
else:
    endereco_cliente = input("\033[1m- Digite o seu endereço: \033[0;0m")
    endereco_entrega = input("\033[1m- Qual o endereço de entrega? \033[0;0m")
    print()
    print("\033[36m***********************************\033[0;0m\033[32m CATÁLOGO DE PREÇOS \033[0;0m\033[36m*********************************\033[0;0m")
    print("\033[32m1) \033[0;0m\033[36mVinho Argentino Tinto Gran Bodega Bonarda Malbec - \033[1mR$ 39,90\033[0;0m")
    print("\033[32m2) \033[0;0m\033[36mVinho Tinto Português Flor de Penalva Colheita Selecionada - \033[1mR$ 79,90\033[0;0m")
    print("\033[32m3) \033[0;0m\033[36mVinho Orgânico Branco Guardian De Los Vinedos - \033[1mR$ 89,90\033[0;0m")
    print("\033[32m4) \033[0;0m\033[36mVinho Tinto Argentino Reserva de los Andes Gran Roble Cabernet Sauvignon - \033[1mR$ 99,90\033[0;0m")
    print("\033[32m5) \033[0;0m\033[36mVinho Rosé Português Pouca Roupa - \033[1mR$ 119,90\033[0;0m")
    print()
    print("\033[1m- Digite a quantidade que gostaria de cada tipo de vinho (caso não queira continuar a compra, digite TERMINAR): \033[0;0m")
    print()
    opcao1 = obter_inteiro("\033[1m- Quantos gostaria da opção 01? \033[0;0m")
    if opcao1 == "TERMINAR":
        print()
        print("\033[32m---- COMPRA FINALIZADA ----\033[0;0m")
        print()
        print("---- VOLTE SEMPRE :) ----")
        print()
    else:
        opcao2 = obter_inteiro("\033[1m- Quantos gostaria da opção 02? \033[0;0m")
        opcao3 = obter_inteiro("\033[1m- Quantos gostaria da opção 03? \033[0;0m")
        opcao4 = obter_inteiro("\033[1m- Quantos gostaria da opção 04? \033[0;0m")
        opcao5 = obter_inteiro("\033[1m- Quantos gostaria da opção 05? \033[0;0m")
        valor_total_produtos = float(39.90 * int(opcao1) + 79.90 * int(opcao2) + 89.90 * int(opcao3) + 99.90 * int(opcao4) + 119.90 * int(opcao5))

        if valor_total_produtos < 100.00:
            print()
            print("\033[31m**** Compra não autorizada!! Mínimo de compra é R$100,00, por favor adicione mais itens!! ****\033[0;0m")
        else:
            print()
            print("\033[32m---- COMPRA FINALIZADA COM SUCESSO ----\033[0;0m") 
            print()   

            # Conferindo se haverá cobrança de frete             
            if (valor_total_produtos < 200.00):
                print()
                print("- O valor do frete é de: R$15,00")
                valor_frete = 15.00
            else:
                print()
                print("\033[30m---- FRETE GRÁTISSSSSSS!! :) ----\033[0;0m")
                valor_frete = 0
            
        # Conferindo se atingiu o valor mínimo para compra
        while valor_total_produtos < 100:
            print()
            print("\033[36m***********************************\033[0;0m\033[32m CATÁLOGO DE PREÇOS \033[0;0m\033[36m*********************************\033[0;0m")
            print("\033[32m1) \033[0;0m\033[36mVinho Argentino Tinto Gran Bodega Bonarda Malbec - \033[1mR$ 39,90\033[0;0m")
            print("\033[32m2) \033[0;0m\033[36mVinho Tinto Português Flor de Penalva Colheita Selecionada - \033[1mR$ 79,90\033[0;0m")
            print("\033[32m3) \033[0;0m\033[36mVinho Orgânico Branco Guardian De Los Vinedos - \033[1mR$ 89,90\033[0;0m")
            print("\033[32m4) \033[0;0m\033[36mVinho Tinto Argentino Reserva de los Andes Gran Roble Cabernet Sauvignon - \033[1mR$ 99,90\033[0;0m")
            print("\033[32m5) \033[0;0m\033[36mVinho Rosé Português Pouca Roupa - \033[1mR$ 119,90\033[0;0m")
            print("- Digite a quantidade que gostaria de cada tipo de vinho (caso não queira continuar a compra, digite TERMINAR): ")
            print()
            opcao1 = obter_inteiro("\033[1m- Quantos gostaria da opção 01? \033[0;0m")
            if opcao1 == "TERMINAR":
                    print()
                    print("\033[32m---- COMPRA FINALIZADA ----\033[0;0m")
                    print()
                    print("---- VOLTE SEMPRE :) ----")
                    print()
            else:
                opcao2 = obter_inteiro("\033[1m- Quantos gostaria da opção 02? \033[0;0m")
                opcao3 = obter_inteiro("\033[1m- Quantos gostaria da opção 03? \033[0;0m")
                opcao4 = obter_inteiro("\033[1m- Quantos gostaria da opção 04? \033[0;0m")
                opcao5 = obter_inteiro("\033[1m- Quantos gostaria da opção 05? \033[0;0m")   
                valor_total_produtos = float(39.90 * int(opcao1) + 79.90 * int(opcao2) + 89.90 * int(opcao3) + 99.90 * int(opcao4) + 119.90 * int(opcao5))
                if (valor_total_produtos < 200.00):
                    print()
                    print("\033[32m- O valor do frete é de: R$15,00\033[0;0m")
                    valor_frete = 15.00
                else:
                    print()
                    print("\033[32m---- FRETE GRÁTISSSSSSS!! :) ----\033[0;0m")
                    valor_frete = 0

            if valor_total_produtos < 100.00:
                print()
                print("\033[31m**** Compra não autorizada!! Mínimo de compra é R$100,00, por favor adicione mais itens!! ****\033[0;0m")       

        # Calculando tudo e retornando ao cliente as informações finais
        total_produtos = int(int(opcao1) + int(opcao2) + int(opcao3) + int(opcao4) + int(opcao5))
        valor_total = float(valor_total_produtos + valor_frete)
        print()
        print("-> Você comprou \033[33m{}\033[0;0m produtos!".format(total_produtos))
        print("-> O total foi de: \033[33mR${:.2f}\033[0;0m".format(valor_total))
        print("-> Os produtos serão entregues no endereço: \033[33m{}\033[0;0m".format(endereco_entrega))
        print()
        print("\033[34m---- AGRADECEMOS PELA PREFERÊNCIA {}, VOLTE SEMPRE!! :) ----\033[0;0m".format(user.upper()))
        print()