def obter_nota_e_conceito():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
            
            if 0 <= nota <= 10:
                if nota >= 8.5:
                    conceito = 'A'
                elif nota >= 7.0:
                    conceito = 'B'
                elif nota >= 5.0:
                    conceito = 'C'
                elif nota >= 4.0:
                    conceito = 'D'
                else:
                    conceito = 'E'
                
                print(f"o conceito para a nota é:{conceito}")
                return 
            else:
                print("Nota inválida.")
        
        except ValueError:
            print("Entrada inválida, por favor digite apenas numeros")

def main():
    obter_nota_e_conceito()

if __name__ == "__main__":
    main()
