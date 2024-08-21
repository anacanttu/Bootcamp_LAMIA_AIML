total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe o numero ou -1 para sair:'))
    if nota != -1:
        qtde += 1
        total += nota   
print(f'Media = {total/qtde}')