class RadioFM:
    def __init__(self, vol_max, estações):
        self.__volume_min = 0
        self.__volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estações = estações
        self.__volume = None
        self.__ligado = False
        self.__estação_atual = None
        self.__frequencia_atual = None
        self.__antena_habilitada = False

    def ligar(self):
        self.__ligado = True
        self.__volume = self.__volume_min
        print(f"Rádio ligado. Volume inicial: {self.__volume}")
        
        if self.__antena_habilitada:
            self.__frequencia_atual = list(self.__estações.keys())[0]
            self.__estação_atual = self.__estações[self.__frequencia_atual]
            print(f"Antena habilitada. Estação sintonizada: {self.__estação_atual} ({self.__frequencia_atual} MHz)")
        else:
            print("Antena não habilitada. Não é possível sintonizar uma estação.")

    def desligar(self):
        self.__ligado = False
        self.__volume = None
        self.__frequencia_atual = None
        self.__estação_atual = None
        print("Rádio desligado. Atributos resetados.")

    def aumentar_volume(self, incremento=1):
        if not self.__ligado:
            print("Rádio desligado. Ligue o rádio antes de ajustar o volume.")
            return

        if incremento < 1:
            print("Incremento deve ser maior que 0.")
            return
        
        if self.__volume + incremento <= self.__volume_max:
            self.__volume += incremento
            print(f"Volume aumentado para {self.__volume}")
        else:
            print(f"Volume máximo alcançado. O volume máximo é {self.__volume_max}.")

    def diminuir_volume(self, decremento=1):
        if not self.__ligado:
            print("Rádio desligado. Ligue o rádio antes de ajustar o volume.")
            return

        if decremento < 1:
            print("Decremento deve ser maior que 0.")
            return

        if self.__volume - decremento >= self.__volume_min:
            self.__volume -= decremento
            print(f"Volume diminuído para {self.__volume}")
        else:
            print(f"Volume mínimo alcançado. O volume mínimo é {self.__volume_min}.")

    def mudar_frequencia(self, nova_frequencia=0):
        if not self.__ligado:
            print("Rádio desligado. Ligue o rádio antes de mudar a frequência.")
            return
        
        if nova_frequencia != 0:
            if nova_frequencia in self.__estações:
                self.__frequencia_atual = nova_frequencia
                self.__estação_atual = self.__estações[nova_frequencia]
                print(f"Frequência alterada para: {self.__estação_atual} ({self.__frequencia_atual} MHz)")
            else:
                print("Frequência inválida. Não existe esta estação.")
        else:
            frequencias = list(self.__estações.keys())
            indice = frequencias.index(self.__frequencia_atual) if self.__frequencia_atual else -1
            if indice == len(frequencias) - 1:
                self.__frequencia_atual = frequencias[0]
                self.__estação_atual = self.__estações[self.__frequencia_atual]
            else:
                self.__frequencia_atual = frequencias[indice + 1]
                self.__estação_atual = self.__estações[self.__frequencia_atual]
            print(f"Frequência alterada para: {self.__estação_atual} ({self.__frequencia_atual} MHz)")

    @property
    def volume(self):
        return self.__volume

    @property
    def frequencia_atual(self):
        return self.__frequencia_atual
    
    @property
    def estacao_atual(self):
        return self.__estação_atual

    def habilitar_antena(self):
        self.__antena_habilitada = True
        print("Antena habilitada.")

    def desabilitar_antena(self):
        self.__antena_habilitada = False
        print("Antena desabilitada.")
        

estações = {
    89.5: 'Cocais',
    91.5: 'Mix',
    94.1: 'Boa',
    99.1: 'Clube'
}

def main():
    meu_radio = RadioFM(vol_max=10, estações=estações)
    meu_radio.habilitar_antena()
    meu_radio.ligar()
    meu_radio.aumentar_volume(3)
    meu_radio.mudar_frequencia(91.5)
    meu_radio.mudar_frequencia()
    meu_radio.diminuir_volume(2)
    meu_radio.desligar()
    meu_radio.aumentar_volume(1)

    print(f"Volume atual: {meu_radio.volume}")
    print(f"Frequência atual: {meu_radio.frequencia_atual} MHz")
    print(f"Estação atual: {meu_radio.estacao_atual}")

if __name__ == '__main__':
    main()
