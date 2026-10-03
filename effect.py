from math import *
from tkinter import *
from random import *
from sys import *
from time import * 
from os import *
def loading(): 
    for epyslon in range (0,5): 
        if 1>0: 
            print("[===       ]") 
            print("Processando.") 
            A = time.sleep(1) 
            system('cls' if name == 'nt' else 'clear') 
        if 2>1:
            print("[======    ]")
            print("Processando..")
            A = time.sleep(1)
            system('cls' if name == 'nt' else 'clear')
        if 3>2:
            print("[========= ]")
            print("Processando...")
            A = time.sleep(1)
            system('cls' if name == 'nt' else 'clear')

def cleaning():
    system('cls' if name == 'nt' else 'clear')

def bond(texto, atraso=0.05):
    for letra in texto:
        stdout.write(letra)
        stdout.flush()  
        sleep(atraso)  
    print()

def gambling(A:int,B:int,C:int):
    chance = randint(A,B)
    if chance == C:
        print("")

def tela():
    sc = Tk()
    sc.geometry("640x480")
    sc.title("Insira título")
    sc.mainloop()