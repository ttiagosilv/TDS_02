from datetime import datetime
class Certidão_Nascimento:

  def __init__(self,nome,data,hora,cidade,estado,mae):
    self.nome = nome
    if not self.validar_data(data):
      raise ValueError("Data inválida")
    self.data = data
    if not self.validar_hora(hora):
      raise ValueError("Hora inválida")

    self.hora = hora
    self.cidade = cidade
    self.estado = estado
    self.mae = mae
    self.pai = input("Nome do pai:")


  def validar_data(self,data_str):
    try:
        # Tenta converter a string para um objeto datetime com o formato DD/MM/AAAA
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data
    except ValueError:
        # Se houver um erro de valor, a data não é válida
        return False

  def validar_hora(self,hora_str):

    try:
        # Tenta converter a string para um objeto datetime com o formato HH:MM
        hora = datetime.strptime(hora_str, "%H:%M")
        return hora
    except ValueError:
        # Se houver um erro de valor, a hora não é válida
        return False

  def __str__(self): #imprimir o estado atual do objeto
   s1 = f'Nome: {self.nome}\nData de Nascimento: {self.data}'
   s2 = f'\nHora de Nascimento: {self.hora}\nCidade: {self.cidade}'
   s3 = f'\nEstado: {self.estado}\nNome da Mãe: {self.mae}'
   return s1+s2+s3