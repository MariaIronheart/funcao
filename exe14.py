#palindromo palavra ou chave que se pode ler
#indiferentemente, da esuqerda para a 
#direita ou vice-versa
def verificar_palindromo(texto):
    texto = texto.lower().replace(' ','')
    return texto == texto[::-1]
    
#texto == texto[::-1] inverte o texto

texto = 'Socorram-me, subi no ônibus em Marrocos'
if verificar_palindromo(texto):
    print(texto, 'é um palíndromo')
else:
    print(texto, 'não é um palindromo')