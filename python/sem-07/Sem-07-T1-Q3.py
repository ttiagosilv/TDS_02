def sinal(cor):
    if cor == "V":
        return "Siga"
    elif cor == "A":
        return "Atenção"
    elif cor == "E":
        return "Pare"
    
def main():
    letra = input ("Digite a cor do sinal de trânsito (V para verde, A para amarelo, E para vermelho): ").upper()
    result = sinal(letra)
    print(result)

if __name__ == "__main__":
    main()