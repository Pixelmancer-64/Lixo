# tentativas = 0
# tentativas_limite = 3

# def recomeco():
#   global tentativas
#   resposta1 = "Pneu"
#   tentativa = ""
#   sem_tentativas = False
#   print(tentativas)
#   while tentativa != resposta1 and not(sem_tentativas):
#         if tentativas < tentativas_limite:
#           tentativa = input("Oque é, oque é: Quanto mais rugas, mais novo ")
#           tentativas += 1
#         else:
#           sem_tentativas = True
#   if sem_tentativas:
#       print("Tentativas esgotadas.")
#       recomeco()
#   else:
#       print("Você acertou!")
#       recomeco()

# recomeco()

nTentativas = 0
nTentativas_limite = 3
def recomeço():
  global nTentativas
  global nTentativas_limite
  resposta1 = "Pneu"
  tentativa = ""
  sem_tentativas = False
  while tentativa != resposta1 and not(sem_tentativas):
        if nTentativas < nTentativas_limite:
          tentativa = input("Oque é, oque é: Quanto mais rugas, mais novo ")
          nTentativas += 1
        else:
          sem_tentativas = True
  if sem_tentativas:
      print("Tentativas esgotadas.")
      recomeço()
  else:
      print("Você acertou!")
      recomeço()
recomeço()