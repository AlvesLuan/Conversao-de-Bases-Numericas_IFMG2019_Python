while True:
    numeroBinario = str(input("\nDigite um número Binario válido: ")).upper()
    numInvertido = numeroBinario[::-1]

    base = 2
    somaDecimal = 0
    tamanho = len(numInvertido)
    temErro = False
    for i in range(0, tamanho):
        caractere = str(numInvertido[i])
        if caractere == str(1) or str(0):
            numero = int(caractere)
        else:
            print("\nTem um caractere inválido: ", caractere)
            temErro = True
            break
        somaDecimal += (numero * (base ** i))
    if not temErro:
        print("\nO número binario", numeroBinario, "convertido para decimal é", somaDecimal)

    if str(input("\nDeseja continuar? (s/n) ")).lower() == "n":
        break