def verifica_caractere(caractere):
    if (caractere.isalpha() or caractere.isdigit()):
        return True
    else:
        return False

caractere = input('Digite algo:').strip()

print(f'O que você digitou é:{(verifica_caractere(caractere))}')