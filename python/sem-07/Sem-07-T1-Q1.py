def saudacoes(nome, sexo):
    if sexo == 1 or sexo == 2:
        if sexo == 1:
            return "Ilmo Sr. " + nome
        else:
            return "Ilma Sra. " + nome
    else:
        return "Erro, defina o sexo apenas com a digitalização do número 1 para masculino ou 2 para feminino"

def main():
    nome = input('Digite o nome da pessoa:')
    sexo = int(input('Digite o código(1 para masculino e 2 para feminino):'))

    mensagem = saudacoes(nome, sexo)
    print (mensagem)

if __name__ == "__main__":
    main()
