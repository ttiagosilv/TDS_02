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

print('''
Q4 - Qual é o primeiro mês do ano?
a. dezembro
b. janeiro
c. agosto
''')

resposta4 = input().lower() 
     
def perg_4(resposta4):
    score = 0
    if resposta4 == 'a':
        score = 0
    elif resposta4 == 'b':
        score = 1
    elif resposta4 == 'c':
        score = 0
    else:
        score = 0
    
    return score  
    
print('''
Q5 -  o que voê usa para escovar os dentes?
a. colher
b. escova
c. sabão
''')

resposta5 = input().lower() 
    
def perg_5(resposta5):
    score = 0
    if resposta5 == 'a':
        score = 0
    elif resposta5 == 'b':
        score = 1
    elif resposta5 == 'c':
        score = 0
    else:
        score = 0
        
    return score  
    
def mensagem(pontuacao):
    if pontuacao == 5:
        return 'Muito bem!!'
    else:
        return 'tente novamente!!'
    

pontuacao = perg_1(resposta1) + perg_2(resposta2) + perg_3(resposta3) + perg_4(resposta4) + perg_5(resposta5) 
  
print(f'Obrigada por jogar! Seu score foi {pontuacao}, {mensagem(pontuacao)}!! ')