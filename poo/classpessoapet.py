class Pet:
    def __init__(self, tipo, nome, idade, peso, raca, cor, castrado=False):
        self.__tipo = tipo
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__castrado = castrado
    
    @property
    def nome(self):
        return self.__nome
    
    def __str__(self):
        return f"Pet {self.__tipo}: {self.__nome}, {self.__idade} anos, {self.__raca}, {self.__cor}"

class Pessoa:
    def __init__(self, cpf, nome, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__meus_pets = []
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    def cadastrar_pet(self, pet):
        self.__meus_pets.append(pet)
        print(f"Pet {pet.nome} cadastrado com sucesso para {self.__nome}")
    
    def excluir_pet(self, nome):
        for pet in self.__meus_pets:
            if pet.nome == nome:
                self.__meus_pets.remove(pet)
                print(f"Pet {nome} foi removido da lista de {self.__nome}")
                return
        print(f"Pet {nome} não encontrado na lista de {self.__nome}")
    
    def mostrar_meus_pets(self):
        if not self.__meus_pets:
            print(f"{self.__nome} não possui pets cadastrados")
            return
        
        print(f"\nPets de {self.__nome}:")
        for pet in self.__meus_pets:
            print(f"- {pet}")

if __name__ == "__main__":
    joao = Pessoa("123.456.789-00", "João Silva", "Rua A, 123")
    maria = Pessoa("987.654.321-00", "Maria Santos", "Rua B, 456")
    pedro = Pessoa("111.222.333-44", "Pedro Oliveira", "Rua C, 789")
    
    pet_rua1 = Pet("Cachorro", "Rex", 2, 8.5, "Vira-lata", "Caramelo")
    pet_rua2 = Pet("Gato", "Mia", 1, 3.2, "SRD", "Preto e Branco")
    
    pet_abrigo1 = Pet("Cachorro", "Thor", 3, 15.0, "Pastor Alemão", "Preto", True)
    pet_abrigo2 = Pet("Gato", "Luna", 2, 4.0, "Siamês", "Bege", True)
    
    print("\n=== Realizando adoções ===")
    joao.cadastrar_pet(pet_rua1)
    maria.cadastrar_pet(pet_abrigo1)
    maria.cadastrar_pet(pet_rua2)
    pedro.cadastrar_pet(pet_abrigo2)
    print("\n=== Situação inicial dos pets ===")
    joao.mostrar_meus_pets()
    maria.mostrar_meus_pets()
    pedro.mostrar_meus_pets()
    
    print("\n=== Simulando perda de pet ===")
    maria.excluir_pet("Mia")
    
    print("\n=== Situação final dos pets ===")
    joao.mostrar_meus_pets()
    maria.mostrar_meus_pets()
    pedro.mostrar_meus_pets()