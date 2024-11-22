def eletra(caractere):
    return 'A' <= caractere.upper() <= 'Z'

def enum(caractere): 
    return caractere in '0123456789'

def econs(caractere):
    return not eletra(caractere) and not enum(caractere)

caractere = input('Digite algo:').strip()

print(f'o que você digitou é:{econs(caractere)}')