frase = str(input("Digite uma palavra ou frase: ")).lower()
letra = "a"
if letra in frase:
    print(f"O termo digitado contém a letra '{letra}', que aparece {frase.count(letra)} vezes")
else:
    print(f"O termo digitado não contém a letra '{letra}'.")