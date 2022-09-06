#Luan Kauan Alves dos Santos / Info1

import os
DesejaContin = "s"
while DesejaContin == "s":
  base = int(input("Qual a base do seu numero ? \n[1]Decimal\n[2]Octal\n[3]Binario\n[4]Hexadecimal\n"))

  if (base == 1): #BASE DECIMAL #COMPLETO#
    num = int(input("\ninforme o seu numero decimal: "))
    esc = int(input("\nDigite pra qual base voce quer converter:\n[1] para Binario \n[2] para Octal \n[3] para Hexadecimal \n\n"))
    if esc == 1: #DECIMAL PRA BINARIO
      junta = ''
      base = 2
      quociente = num
      while (quociente >= base):
        resto = quociente % base
        quociente //= base
        junta = junta + str(resto)
      junta = junta + str(quociente)
      print ("O seu numero em Binario é: " + junta[::-1])
    if esc == 2: #DECIMAL PRA OCTAL
      junta = ''
      base = 8
      quociente = num
      while (quociente >= base):
        resto = quociente % base
        quociente //= base
        junta = junta + str(resto)
      junta = junta + str(quociente)
      print ("O seu numero em Octal é: " + junta[::-1])  
    if esc == 3: #DECIMAL PRA HEXA
      junta = ''
      base = 16
      quociente = num
      while (quociente >= base):
        resto = quociente % base
        if (resto == 10):
          resto = "A"
        elif (resto == 11):
          resto = "B"
        elif (resto == 12):
          resto = "C"
        elif (resto == 13):
          resto = "D"
        elif (resto == 14):
          resto = "E"
        elif (resto == 15):
          resto = "F"
        quociente //= base
        junta = junta + str(resto)
      if(quociente == 10):
        quociente = "A"
      if(quociente == 11):
        quociente = "B"
      if(quociente == 12):
        quociente = "C"
      if(quociente == 13):
        quociente = "D"
      if(quociente == 14):
        quociente = "E"
      if(quociente == 15):
        quociente = "F"
      junta = junta + str(quociente)
      print ("\nO seu numero em Hexadecimal é: " + junta[::-1])
      break




#################################################################




  elif (base == 2): #BASE OCTAL #COMPLETO
    num = str(input("\ninforme o seu numero Octal: "))
    esc = int(input("\nDigite pra qual base voce quer converter:\n[1] para Binario \n[2] para Decimal \n[3] para Hexadecimal \n\n"))
    if esc == 1: #OCTAL PRA BINARIO
      num = num[::-1]
      base = 8
      somaDecimal = 0
      tamanho = len(num)
      for i in range(0, tamanho):
        caractere = str(num[i])
        if caractere == str(1) or str(0):
          numero = int(caractere)
        somaDecimal += (numero * (base ** i))
      numOctEmDec = somaDecimal
      base = 2
      quociente = numOctEmDec
      binario = ""
      while (quociente >= 2):
        resto = quociente % base
        quociente //= base
        binario += str(resto)
      binario += str(quociente)
      binario = binario[::-1]
      print ('O seu numero em binario é:',binario)
    if esc == 2: #OCTAL PRA DECIMAL
      num = num[::-1]
      base = 8
      somaDecimal = 0
      tamanho = len(num)
      for i in range(0, tamanho):
        caractere = str(num[i])
        if caractere == str(1) or str(0):
          numero = int(caractere)
        somaDecimal += (numero * (base ** i))
      numOctEmDec = somaDecimal
      base = 2
      quociente = numOctEmDec
      print('Seu numero em decimal é:',numOctEmDec)
    if esc == 3: #OCTAL PRA HEXA
      num = num[::-1]
      base = 8
      somaDecimal = 0
      tamanho = len(num)
      for i in range(0, tamanho):
        caractere = str(num[i])
        if caractere == str(1) or str(0):
          numero = int(caractere)
        somaDecimal += (numero * (base ** i))
      numOctEmDec = somaDecimal
      base = 16
      HexDec = ''
      quociente = numOctEmDec
      while (quociente >= 2):
        resto = quociente % base
        if (resto == 10):
          resto = str("A")
        elif (resto == 11):
          resto = str("B")
        elif (resto == 12):
          resto = str("C")
        elif (resto == 13):
          resto = str("D")
        elif (resto == 14):
          resto = str("E")
        elif (resto == 15):
          resto = str("F")
        quociente //= base
        HexDec += str(resto)
      HexDec += str(quociente)
      HexDec = HexDec[::-1]
      if (HexDec[0] == "0"):
        HexDec = HexDec[1:]
      print('Seu numero em decimal é:',HexDec)



#################################################################




  elif (base==3): #BASE BINARIA #COMPLETO#
    num = str(input("\ninforme o seu numero Binario: "))
    esc = int(input("\nDigite pra qual base voce quer converter:\n[1] para octal \n[2] para Decimal \n[3] para Hexadecimal \n\n")) 
    if esc == 1: #BINARIO PARA OCTAL
      caractere = ''
      tamanho = len(num)
      resto = int(tamanho % 3)
      sub = int(3 - resto)
      zeros = '0' * sub
      num = zeros = num
      numerodecimal = ''
      for i in range (0,tamanho,3):
        bloco = num[i:i+3:1]
        if (bloco == '000'):
          caractere = '0'
        if (bloco == '001'):
          caractere = '1'
        if (bloco == '010'):
          caractere = '2'
        if (bloco == '011'):
          caractere = '3'
        if (bloco == '100'):
          caractere = '4'
        if (bloco == '101'):
          caractere = '5'
        if (bloco == '110'):
          caractere = '6'
        if (bloco == '111'):
          caractere = '7'
        numerodecimal += caractere
      print('Seu numero em octal é:',numerodecimal)
    if esc == 2: #BINARIO PRA DECIMAL
      caractere = ''
      tamanho = len(num)
      resto = int(tamanho % 4)
      sub = int(4 - resto)
      zeros = '0' * sub
      num = zeros = num
      numerodecimal = ''
      for i in range (0,tamanho,4):
        bloco = num[i:i+4:1]
        if (bloco == '0000'):
          caractere = '0'
        if (bloco == '0001'):
          caractere = '1'
        if (bloco == '0010'):
          caractere = '2'
        if (bloco == '0011'):
          caractere = '3'
        if (bloco == '0100'):
          caractere = '4'
        if (bloco == '0101'):
          caractere = '5'
        if (bloco == '0110'):
          caractere = '6'
        if (bloco == '0111'):
          caractere = '7'
        if (bloco == '1000' ):
          caractere = '8'
        if (bloco == '1001'):
          caractere = '9'
        numerodecimal += caractere
      print('Seu numero em decimal é:',numerodecimal)
    if esc == 3: #DECIMAL PRA HEXA
      caractere = ''
      tamanho = len(num)
      resto = int(tamanho % 4)
      sub = int(4 - resto)
      zeros = '0' * sub
      num = zeros = num
      numerodecimal = ''
      for i in range (0,tamanho,4):
        bloco = num[i:i+4:1]
        if (bloco == '0000'):
          caractere = '0'
        if (bloco == '0001'):
          caractere = '1'
        if (bloco == '0010'):
          caractere = '2'
        if (bloco == '0011'):
          caractere = '3'
        if (bloco == '0100'):
          caractere = '4'
        if (bloco == '0101'):
          caractere = '5'
        if (bloco == '0110'):
          caractere = '6'
        if (bloco == '0111'):
          caractere = '7'
        if (bloco == '1000' ):
          caractere = '8'
        if (bloco == '1001'):
          caractere = '9'
        numerodecimal += caractere
      junta = ''
      base = 16
      quociente = int(numerodecimal)
      while (quociente >= base):
        resto = quociente % base
        if (resto == 10):
          resto = "A"
        elif (resto == 11):
          resto = "B"
        elif (resto == 12):
          resto = "C"
        elif (resto == 13):
          resto = "D"
        elif (resto == 14):
          resto = "E"
        elif (resto == 15):
          resto = "F"
        quociente //= base
        junta = junta + str(resto)
      if(quociente == 10):
        quociente = "A"
      if(quociente == 11):
        quociente = "B"
      if(quociente == 12):
        quociente = "C"
      if(quociente == 13):
        quociente = "D"
      if(quociente == 14):
        quociente = "E"
      if(quociente == 15):
        quociente = "F"
      junta = junta + str(quociente)
      print ("\nO seu numero em Hexadecimal é: " + junta[::-1])
      



#################################################################




  elif (base==4): #BASE HEXADECIMAL #COMPLETO#
    num = str(input("\ninforme o seu numero Hexadecimal: "))
    esc = int(input("\nDigite pra qual base voce quer converter:\n[1] para Binario \n[2] para Octal \n[3] para Decimal \n\n"))
    if esc == 1: #HEXADECIMAL PRA BINARIO
      numInvertido = num[::-1]
      base = 16
      somaDecimal = 0
      tamanho = len(numInvertido)
      temErro = False
      for i in range(0, tamanho):
        caractere = str(numInvertido[i])
        if caractere.isdigit():
          numero = int(caractere)
        elif caractere == 'A':
          numero = 10
        elif caractere == 'B':
          numero = 11
        elif caractere == 'C':
          numero = 12
        elif caractere == 'D':
          numero = 13
        elif caractere == 'E':
          numero = 14
        elif caractere == 'F':
          numero = 15
        else:
          print("\nTem um caractere inválido: ", caractere)
          temErro = True
          break
        somaDecimal += (numero * (base ** i))
      if not temErro:
        junta = ''
        base = 2
        quociente = somaDecimal
        while (quociente >= base):
          resto = quociente % base
          quociente //= base
          junta = junta + str(resto)
        junta = junta + str(quociente)
        print ("O seu numero em Binario é: " + junta[::-1])

    if esc == 2: #HEXADECIMAL PRA OCTAL
      while True:
        numInvertido = num[::-1]
        base = 16
        somaDecimal = 0
        tamanho = len(numInvertido)
        temErro = False
        for i in range(0, tamanho):
          caractere = str(numInvertido[i])
          if caractere.isdigit():
            numero = int(caractere)
          elif caractere == 'A':
            numero = 10
          elif caractere == 'B':
            numero = 11
          elif caractere == 'C':
            numero = 12
          elif caractere == 'D':
            numero = 13
          elif caractere == 'E':
            numero = 14
          elif caractere == 'F':
            numero = 15
          else:
            print("\nTem um caractere inválido: ", caractere)
            temErro = True
            break
          somaDecimal += (numero * (base ** i))
        if not temErro:
          junta = ''
          base = 8
          quociente = somaDecimal
          while (quociente >= base):
            resto = quociente % base
            quociente //= base
            junta = junta + str(resto)
          junta = junta + str(quociente)
          print ("O seu numero em Octal é: " + junta[::-1])
          break
            
            
    if esc == 3: #HEXADECIMAL PRA DECIMAL
      while True:
        numInvertido = num[::-1]
        base = 16
        somaDecimal = 0
        tamanho = len(numInvertido)
        temErro = False
        for i in range(0, tamanho):
          caractere = str(numInvertido[i])
          if caractere.isdigit():
            numero = int(caractere)
          elif caractere == 'A':
            numero = 10
          elif caractere == 'B':
            numero = 11
          elif caractere == 'C':
            numero = 12
          elif caractere == 'D':
            numero = 13
          elif caractere == 'E':
            numero = 14
          elif caractere == 'F':
            numero = 15
          else:
            print("\nTem um caractere inválido: ", caractere)
            temErro = True
            break
          somaDecimal += (numero * (base ** i))
        if not temErro:
            print("\nO seu número em decimal é", somaDecimal)
            break
        





  DesejaContin = str(input("\nDeseja continuar e trocar a base ? (s/n)")).lower()
  if DesejaContin == 'n':
    break
  else :
    os.system('cls' if os.name == 'nt' else 'clear')