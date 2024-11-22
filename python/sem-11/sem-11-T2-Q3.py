def main():
    while True:
        
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")
        
        try:
            opcao = int(input())
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue
        
        if opcao == 1:
            print("1 - Olá. Como vai?")
        elif opcao == 2:
            print("2 - Vamos estudar mais.")
        elif opcao == 3:
            print("3 - Meus Parabéns!")
        elif opcao == 0:
            print("0 - Fim de serviço.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
