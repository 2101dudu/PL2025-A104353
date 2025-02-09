import sys

total = 0
calcula = True
for linha in sys.stdin:
    i = 0
    while i < len(linha):
        valor = 0
        if calcula and linha[i] in "0123456789":
            while linha[i] in "0123456789":
                valor = valor * 10 + int(linha[i])
                i += 1
            total += valor
        elif linha[i] in "oO":
            if i+2 <= len(linha) and linha[i+1] in "Ff" and linha[i+2] in "fF":
                calcula = False
                i += 3
            elif i+1 <= len(linha) and linha[i+1] in "nN":
                calcula = True
                i += 2
            else:
                i += 1
        elif linha[i] in "=":
            i += 1
            print(total)
        else:
            i += 1
