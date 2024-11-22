
print('''
Q1 - Qual é a tradução da palavra notebook? 
a. caderno
b. tela maior
c. mini computador
''')
resposta1 = input().lower() 

def perg_1(resposta1):
    score = 0
    if resposta1 == 'a':
        score = 1
    elif resposta1 == 'b':
        score = 0
    elif resposta1 == 'c':
        score = 0
    else:
        score = 0
    
    return score
   
print('''
Q2 - Quantos dedos temos em uma mão? 
a. 10
b. 8
c. 5
''')

resposta2 = input().lower() 
     
def perg_2(resposta2):
    score = 0
    if resposta2 == 'a':
        score = 0
    elif resposta2 == 'b':
        score = 0
    elif resposta2 == 'c':
        score = 1
    else:
        score = 0
    
    return score  

print('''
Q3 - Quantos dias tem uma semana?
a. 7
b. 31
c. 5
''')

resposta3 = input().lower() 
     
def perg_3(resposta3):
    score = 0
    if resposta3 == 'a':
        score = 1
    elif resposta3 == 'b':
        score = 0
    elif resposta3 == 'c':
        score = 0
    else:
        score = 0
    
    return score 

pontuacao = perg_1(resposta1) + perg_2(resposta2) + perg_3(resposta3)
print('Sua pontuação foi de:', pontuacao)
