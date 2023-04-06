def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas) #como a lista tem 4 objetos o len vale 4, ou seja, sum/4
    return media
notas = [7.5,8.0,6.5,9.0]
media = calcular_media(notas)
print('A média é: ',media)