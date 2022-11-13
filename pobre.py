def juros():
  c = (int(input("Investimento ")))
  if c <= 99:
    print("POBRE!!")
    juros() # Como retornar ao campo pra alterar a variavel C?
  t = (int(input("Tempo ")))
  i = (int(input("Taxa de rendimento ")))
  m = c * (1 + i/100)**t
  lucro = (m - c)
  print ('Seu lucro liquido é:',round((lucro),2))

juros()