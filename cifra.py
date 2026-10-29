#Cifra de Cesar Simples
#I. Introdução: 
for c in range(0,26):# Pega da 1° letra até a 26° letra do alfabeto(0 é a primeira e 25 a última)
    print(ord('A')+c,'->',chr(c+65),# +65 pois o ord('A') = 65
          ord('a')+c,'->',chr(c+97))# +97 pois o ord('a') = 97
#II. Programa(Base dele)
A = input("Insira uma frase: ")#Pede para o usuário inserir uma frase
coded = ""
alfa = len(A)#Tamanho da frase
for theta in range(alfa):#Para uma variável no espaço do tamanho da frase
    if A[theta] == " ":
        print(" ")#Caso o caractere da variável seja espaço, retorne espaço. Sem isso, retorna '#'
        coded += " "#Adiciona o espaço na criptografia final
    else:
        print(A[theta], '->' ,ord(A[theta]), f'-> Adicionando 3 ->', ord(A[theta]) + 3, '->', chr(ord(A[theta]) + 3))#Caso contrário, Letra da posição -> Número em Unicode -> letra em Unicode + 3
        coded += chr(ord(A[theta]) + 3)#Adiciona na criptografia final o caractere
print(f"Cifrado! A criptografia é \033[32m{coded}\033[m")#Output é a criptografia final destacada.
