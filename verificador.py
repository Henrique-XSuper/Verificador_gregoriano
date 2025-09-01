ano=int(input("Digite o ano:  "))

if ano<1582:
  print("não faz parte do calendario gregoriano")
else:
  if ano % 4 != 0:
    print("ano comum")
  elif ano % 100 != 0:
    print("ano Bissexto")
  elif ano % 400 != 0:
    print("ano comum")
  else:
    print("ano bissexto")
