from time import sleep
from limpeza import clean
candidato1 = 0
candidato2 = 0
candidato3 = 0
invalido = 0
def introdução():
    print("-"*60)
    print("Simulador de Urna Eletrônica".center(60))
    print("-"*60)
introdução()
print("Números dos candidatos: 01,02,03(Coloque o 0 para funcionar)")
sleep(5)
clean()
introdução()
zeta = "Candidato: __" 
print(zeta)
A = (input(""))
print(f"Candidato : {A}")
print("Confirmar voto?",end = "")
alfa = input("")
if A == "01":
    candidato1 += 1
if A == "02":
    candidato2 += 1
if A == "03":
    candidato3 += 1
else:
    invalido += 1
clean()
while A != 00:
    introdução()
    zeta = "Candidato: __" 
    print(zeta)
    A = (input(""))
    print(f"Candidato : {A}")
    print("Confirmar voto?",end = "")
    alfa = input("")
    if A == "01":
        candidato1 += 1
    if A == "02":
        candidato2 += 1
    if A == "03":
        candidato3 += 1
    else:
        invalido += 1
    if A == "00":
        break
    clean()
clean()
tot = candidato1+candidato2+candidato3+invalido
resA = candidato1 / tot
resB = candidato2 / tot
resC = candidato3 / tot
resI = invalido / tot
clean()
sleep(3)
print("Apuração das Urnas:")
"""sleep(1)
print(f"Total de Votos:{tot}")
sleep(1)
print(f"Candidato 01: {resA*100:.2f}%")
sleep(1)
print(f"Candidato 02: {resB*100:.2f}%")
sleep(1)
print(f"Candidato 03: {resC*100:.2f}%")
sleep(1)
print(f"Votos Brancos/Nulos:{resI*100:.2f}%")
sleep(1)"""
def vencedor():
    if resA > resB and resA > resC:
        print("Vencedor:") 
        sleep(3)
        print(f"Candidato 01({resA*100:.2f}%)")
    if resB > resA and resB > resC:
        print("Vencedor:") 
        sleep(3)
        print(f"Candidato 02({resB*100:.2f}%)")
    if resC > resB and resC > resA:
        print("Vencedor:") 
        sleep(3)
        print(f"Candidato 03({resC*100:.2f}%)")
clean()
vencedor()
