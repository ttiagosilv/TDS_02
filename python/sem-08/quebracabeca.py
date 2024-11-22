import urllib.request  # Importa o módulo urllib para lidar com solicitações HTTP
from unicodedata import normalize  # Importa a função normalize do módulo unicodedata

def remover_acentos(texto):
    # Função para remover acentos do texto
    texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto

def horoscopo(signo_desejado):
    # Função para obter o horóscopo de um determinado signo
    signo_formatado = remover_acentos(signo_desejado).lower() 
    # Constrói a URL do horóscopo
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado  
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={"User-Agent": "Mozilla/5.0"}  # Define o cabeçalho do usuário para a requisição HTTP
    )
    resposta = urllib.request.urlopen(requisicao)  # Faz a requisição HTTP
    pagina = resposta.read().decode('utf-8')  # Lê a página e decodifica o conteúdo
    marcador_inicio = '<p class="text-pred">'  # Define o marcador de início do horóscopo
    marcador_final = '</p>'  # Define o marcador de fim do horóscopo
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)  # Encontra a posição do início do horóscopo
    final = pagina.find(marcador_final, inicio)  # Encontra a posição do fim do horóscopo
    return signo_desejado + " " + pagina[inicio:final]  # Retorna o horóscopo

def signo(dia, mes):
    # Função para determinar o signo com base na data de nascimento
    if mes == 3:
        return "Peixes" if dia < 21 else "Áries"
    elif mes == 4:
        return "Áries" if dia < 21 else "Touro"
    elif mes == 5:
        return "Touro" if dia < 21 else "Gêmeos"
    elif mes == 6:
        return "Gêmeos" if dia < 22 else "Câncer"
    elif mes == 7:
        return "Câncer" if dia < 23 else "Leão"
    elif mes == 8:
        return "Leão" if dia < 23 else "Virgem"
    elif mes == 9:
        return "Virgem" if dia < 23 else "Libra"
    elif mes == 10:
        return "Libra" if dia < 23 else "Escorpião"
    elif mes == 11:
        return "Escorpião" if dia < 22 else "Sagitário"
    elif mes == 12:
        return "Sagitário" if dia < 22 else "Capricórnio"
    elif mes == 1:
        return "Capricórnio" if dia < 20 else "Aquário"
    elif mes == 2:
        return "Aquário" if dia < 19 else "Peixes"

def separar_data(dma):
    # Função para separar a data em dia, mês e ano
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //= 100
    d = dma
    return d, m, a

def main():
    # Função principal
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))  # Solicita a data de nascimento ao usuário
    dia, mes, ano = separar_data(nascimento)  # Separa a data em dia, mês e ano
    meu_signo = signo(dia, mes)  # Determina o signo com base na data de nascimento
    horoscopo_de_hoje = horoscopo(meu_signo)  # Obtém o horóscopo do signo determinado
    print(horoscopo_de_hoje)  # Exibe o horóscopo

if __name__ == "__main__":
    main()  # Chama a função principal se o script for executado diretamente