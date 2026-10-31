#Projeto 1: "App" Relógio, com cronômetro e temporizador embutidos
from limpeza import clean
from time import *
def cronometro():
    A = B = C = 0
    while True:
        sleep(0.01)
        print(f"{A:02d}:{B:02d}:{C:02d}")
        C += 1
        if C == 100:
            B += 1
            C = 0
        if B == 60:
            A += 1
            B = C = 0

def clock():
    while True:
        clean()
        X = strftime('%d/%m/%y - %H:%M:%S')
        print(X)
        sleep(1)

def temporizador():
    print("insira quanto tempo deseja para o temporizador: ")
    H = int(input("Horas: "))
    M = int(input("Minutos: "))
    S = int(input("Segundos: "))
    while True:
        sleep(1)
        if H == 0 and M == 0 and S == 0:
            break
        S -= 1
        if M < 0:
            H -= 1
            M = 59
            S = 59
        if S < 0:
            M -= 1
            S = 59
        print(f"{H:02d}:{M:02d}:{S:02d}")
    print("Time's Up!")

print('='*20,'Relógio','='*20)
print('Configurações de relógio:\nCronômetro\nRelógio Simples\nTemporizador')
zeta = input("Insira configuração de relógio: ")
if zeta == 'Cronômetro':
    print("configuração selecionada: Cronômetro")
    sleep(1)
    clean()
    print("Contagem iniciada")
    cronometro()
if zeta == 'Relógio Simples':
    print("configuração selecionada: Relógio Simples")
    sleep(1)
    clock()
if zeta == 'Temporizador':
    print("configuração selecionada: Temporizador")
    sleep(1)
    clean()
    temporizador()
