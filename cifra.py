#Cifra de Cesar Simples
#I. Introdução: 
for c in range(0,26):# Pega da 1° letra até a 26° letra do alfabeto(0 é a primeira e 25 a última)
    print(ord('A')+c,'->',chr(c+65),# +65 pois o ord('A') = 65
          ord('a')+c,'->',chr(c+97))# +97 pois o ord('a') = 97
#II. Programa(Base dele)
A = input("Insira uma frase: ")#pede para o usuário inserir uma frase
B = int(input("Insira quantas letras quer pular(recomendado apenas 3): "))
alfa = len(A)#Tamanho da frase
for theta in range(alfa):#para uma variável no espaço do tamanho da frase
    if A[theta] == " ":
        print(" ")#Caso o caractere da variável seja espaço, retorne espaço. Sem isso, retorna '#'
    else:
        print(A[theta], '->' ,ord(A[theta]), f'-> Adicionando {B} ->', ord(A[theta]) + B, '->', chr(ord(A[theta]) + B))#Caso contrário, Letra da posição -> Número em Unicode -> letra em Unicode + 3