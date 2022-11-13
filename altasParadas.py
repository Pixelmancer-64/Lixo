def escolha():
  opt = int(input("Selecione o número correspondente a opção desejada:\n[1] Calculadora Básica \n[2] Equação de segundo grau\n[3] Regra de 3\n[4] Calculo de juros compostos\n[5] Calculo IMC\n"))
  if opt == 1:
      calculadora()
  elif opt == 2:
      quadratica()
  elif opt == 3:
      regra3()
  elif opt == 4:
      juros()
  elif opt == 5:
      imc()
  else:
      print("Selecione uma opção válida") 
def calculadora():
  num1 = float(input("Primeiro número: "))
  op =  (input("Operação(+ ,- , / , ): "))
  num2 = float(input("Segundo número: "))

  if op == "+":
    print(num1 + num2)
  elif op == "-":
    print(num1 - num2)
  elif op == "":
    print(num1 * num2)
  elif op == "/":
    print(num1 / num2)
  elif op == "":
    print(num1  num2)
  else:
    print("Operação inválida")
    escolha()
def regra3():
  valor1 = float(input("Primeiro valor: "))
  print("Está para")
  valor2 = float(input(""))
  print("Assim como")
  valor3 = float(input(""))
  x = valor3 * valor2 / valor1
  print("Está para", (x))
  escolha()

def juros():
  c = (int(input("Investimento ")))
  if c <= 99:
    print("POBRE!!")
    juros() # Como retornar ao campo pra alterar a variavel C?
  t = (int(input("Tempo ")))
  i = (int(input("Taxa de rendimento ")))
  m = c * (1 + i/100)t
  lucro = (m - c)
  print ('Seu lucro liquido é:',round((lucro),2))
  escolha()


def imc():  # terminar esse 
  peso = float(input("Peso: ")) 
  altura = float(input("Altura: ")) 
  imc = peso / altura2 
  print ('Seu IMC é: ',round((imc),2))
  if imc < 18.5 :
    print ("Muito magro")
  elif 24.9> imc > 18.5:
    print("Peso ideal")
    escolha()

def quadratica():
  a = float(input("A ")) 
  b = float(input("B ")) 
  c = float(input("C ")) 
  delta = b2 - 4 * a * c
  x1 = (-b + (delta(1/2))) / (2a)
  x2 = (-b - (delta**1/2)) / (2a)
  print ('Δ = ', delta)
  print ('X1 = ', round(x1, 2))
  print ('X2 = ', round(x2, 2))
  escolha()
escolha()