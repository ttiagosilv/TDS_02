def data_recente(data1, data2):
    if data1[2] > data2[2]:
        return data1
    elif data1[2] < data2[2]:
        return data2
    elif data1[1] > data2[1]:
        return data1
    elif data1[1] < data2[1]:
        return data2
    elif data1[0] > data2[0]:
        return data1
    elif data1[0] < data2[0]:
        return data2
    else:
        return data1  # Se as datas forem iguais, retorna qualquer uma delas

def main():
    print("Digite a primeira data:")
    dia1 = int(input("Dia: "))
    mes1 = int(input("Mês: "))
    ano1 = int(input("Ano: "))
    
    print("\nDigite a segunda data:")
    dia2 = int(input("Dia: "))
    mes2 = int(input("Mês: "))
    ano2 = int(input("Ano: "))

    data1 = (dia1, mes1, ano1)
    data2 = (dia2, mes2, ano2)
    
    # Comparando as datas
    resultado = data_recente(data1, data2)

    # Exibindo a data mais recente
    print("\nA data mais recente é: {}/{}/{}".format(resultado[0], resultado[1], resultado[2]))

if __name__ == "__main__":
    main()

