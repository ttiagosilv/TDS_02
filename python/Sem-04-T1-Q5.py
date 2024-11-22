altura = int(input('Qual a altura da sala:'))
comprimento = int(input('Qual o comprimento da sala:'))
largura = int(input('Qual a largura da sala:'))

Area = largura * comprimento

Volume = largura * comprimento * altura

Area_das_paredes = 2 * altura * largura + 2 * altura * comprimento

print('A área da sala é de:', Area)
print('O volume da sala em metros cúbicos é:', Volume)
print('A área das paredes é de:', Area_das_paredes) 
