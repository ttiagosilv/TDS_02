def caractere_inicial(caractere):
    if caractere.isdigit():
        return 'número'
    elif caractere.isalpha():
        if caractere.lower() in 'aeiou':
            return 'vogal'
        if caractere.lower() == 'ç':
            return 'símbolo' 
        else: 
            return 'consoante'
    else:
        return 'símbolo'
    
def main():
    caractere = input("Digite um caractere: ")
    if len(caractere) == 1:
        if caractere.isalnum():
            mensagem = caractere_inicial(caractere)
        else:
            mensagem = "símbolo"
        print(mensagem)
    else:
        print("Por favor, digite apenas um caractere.")
if __name__ == "__main__":
    main()