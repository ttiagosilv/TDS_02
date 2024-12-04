class Bicicleta:
    def __init__(self, veloc_atual=0, altura_cela=75, calibragem_pneus=50):
        self.veloc_atual = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus
        self.veloc_max = 100  
        self.veloc_min = 0    
        self.altura_cela_min = 50  
        self.altura_cela_max = 100 
        self.calib_min = 0   
        self.calib_max = 100 

    def mostrar_estado(self):
        return f"Velocidade: {self.veloc_atual} km/h | Altura da cela: {self.altura_cela} cm | Calibragem dos pneus: {self.calibragem_pneus}%"

    def alterar_velocidade(self, nova_velocidade):
        if nova_velocidade < self.veloc_min or nova_velocidade > self.veloc_max:
            print(f"Velocidade inválida! Deve estar entre {self.veloc_min} e {self.veloc_max} km/h.")
        else:
            self.veloc_atual = nova_velocidade
            
    def regular_cela(self, nova_altura):
        if self.veloc_atual == 0:
            if self.altura_cela_min <= nova_altura <= self.altura_cela_max:
                self.altura_cela = nova_altura
            else:
                print(f"Altura inválida! Deve estar entre {self.altura_cela_min} e {self.altura_cela_max} cm.")
        else:
            print("A bicicleta precisa estar parada para ajustar a altura da cela.")
    
    def calibrar_pneus(self, nova_calibragem):
        if self.veloc_atual == 0:
            if self.calib_min <= nova_calibragem <= self.calib_max:
                self.calibragem_pneus = nova_calibragem
            else:
                print(f"Calibragem inválida! Deve estar entre {self.calib_min} e {self.calib_max}.")
        else:
            print("A bicicleta precisa estar parada para calibrar os pneus.")

bicicleta1 = Bicicleta()
bicicleta2 = Bicicleta(veloc_atual=30, altura_cela=80, calibragem_pneus=60)

print("Estado inicial da bicicleta 1:")
print(bicicleta1.mostrar_estado())

print("\nEstado inicial da bicicleta 2:")
print(bicicleta2.mostrar_estado())

bicicleta1.regular_cela(90) 
bicicleta1.calibrar_pneus(70)  
bicicleta2.regular_cela(85)  
bicicleta2.calibrar_pneus(80) 
bicicleta1.alterar_velocidade(50)  
bicicleta2.alterar_velocidade(110)  

print("\nEstado após alterações na bicicleta 1:")
print(bicicleta1.mostrar_estado())

print("\nEstado após alterações na bicicleta 2:")
print(bicicleta2.mostrar_estado())
