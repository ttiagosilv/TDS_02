import random
from datetime import datetime

class CartaoEmbarque:
    ASSENTOS_DISPONIVEIS = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C"]
    ASSENTOS_OCUPADOS = set()

    def __init__(self, nome, numero_voo, codigo_reserva, data_embarque):
        self.nome = nome
        self.numero_voo = numero_voo
        self.codigo_reserva = codigo_reserva
        self.data_embarque = self.validar_data_embarque(data_embarque)
        self.status_checkin = False
        self.assento = None

    def validar_codigo_reserva(self):
        return len(self.codigo_reserva) == 6 and self.codigo_reserva.isalnum()

    def validar_data_embarque(self, data_embarque):
        if data_embarque < datetime.now():
            raise ValueError("Data de embarque não pode ser retroativa.")
        return data_embarque

    def realizar_checkin(self):
        if self.status_checkin:
            raise ValueError("Check-in já realizado.")
        if not self.validar_codigo_reserva():
            raise ValueError("Código de reserva inválido.")
        
        assento = self.obter_assento_disponivel()
        if assento:
            self.assento = assento
            self.status_checkin = True
            CartaoEmbarque.ASSENTOS_OCUPADOS.add(assento)
            print(f"Check-in realizado. Assento: {assento}")
        else:
            raise ValueError("Sem assentos disponíveis.")

    def obter_assento_disponivel(self):
        disponíveis = list(set(CartaoEmbarque.ASSENTOS_DISPONIVEIS) - CartaoEmbarque.ASSENTOS_OCUPADOS)
        return random.choice(disponíveis) if disponíveis else None

    def alterar_assento(self, novo_assento):
        if not self.status_checkin:
            raise ValueError("Check-in necessário antes de alterar o assento.")
        if novo_assento in CartaoEmbarque.ASSENTOS_OCUPADOS:
            raise ValueError(f"Assento {novo_assento} ocupado.")
        CartaoEmbarque.ASSENTOS_OCUPADOS.remove(self.assento)
        self.assento = novo_assento
        CartaoEmbarque.ASSENTOS_OCUPADOS.add(novo_assento)
        print(f"Assento alterado para: {novo_assento}")

    def __str__(self):
        return (f"Passageiro: {self.nome}\nVoo: {self.numero_voo}\nCódigo: {self.codigo_reserva}\n"
                f"Embarque: {self.data_embarque.strftime('%d/%m/%Y %H:%M')}\nCheck-in: {'Realizado' if self.status_checkin else 'Não realizado'}\n"
                f"Assento: {self.assento if self.assento else 'Não atribuído'}")

# Função main para interação com o usuário
def main():
    print("Bem-vindo ao sistema de Cartão de Embarque!")
    
    nome = input("Digite o nome do passageiro: ")
    numero_voo = input("Digite o número do voo: ")
    codigo_reserva = input("Digite o código da reserva (6 caracteres alfanuméricos): ")
    
    data_embarque_str = input("Digite a data e hora do embarque (formato: dd/mm/yyyy HH:MM): ")
    
    try:
        # Convertendo a string para o formato datetime
        data_embarque = datetime.strptime(data_embarque_str, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Data e hora do embarque estão no formato incorreto.")
        return
    
    # Verificando se o código da reserva é válido
    cartao = CartaoEmbarque(nome, numero_voo, codigo_reserva, data_embarque)
    if not cartao.validar_codigo_reserva():
        print("Código de reserva inválido. O código deve ter 6 caracteres alfanuméricos.")
        return
    
    print("\nCartão de embarque criado com sucesso!\n")
    print(str(cartao))
    
    while True:
        print("\nO que você deseja fazer?")
        print("1. Realizar check-in")
        print("2. Alterar assento")
        print("3. Exibir informações do cartão de embarque")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            try:
                cartao.realizar_checkin()
            except ValueError as e:
                print(f"Erro: {e}")
        
        elif opcao == "2":
            if not cartao.status_checkin:
                print("Você precisa realizar o check-in primeiro.")
            else:
                novo_assento = input("Digite o novo assento (ex: 2A): ")
                try:
                    cartao.alterar_assento(novo_assento)
                except ValueError as e:
                    print(f"Erro: {e}")
        
        elif opcao == "3":
            print("\nInformações do Cartão de Embarque:")
            print(str(cartao))
        
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executando a função main
if __name__ == "__main__":
    main()
