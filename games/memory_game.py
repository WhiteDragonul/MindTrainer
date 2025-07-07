import random
import os
import time

def play():
    print("\n🔁Joc de memorie 🔁")
    symbols = ["🔴", "😤", "🔵", "🖖", "🧟‍♂️", "☂️"]
    level=3

    sequence=[random.choice(symbols) for i in range(level)]
    print("Memoreaza aceasta secventa:")
    print(" ".join(sequence))
    time.sleep(3)

    os.system("cls" if os.name=="nt" else "clear") #stergem ecranul consolei Windows=nt Linux/Mac=posix daca e windows
    #ruleaza comanda cls, daca e alt sistem ruleaza clear
    #os.system ruleaza acea comanda in consola sistemului de operare
    #os.system("cls") - windows
    #os.system("clear")- linux,macos

    raspuns=input("Repeta secventa(cu spatiu intre simboluri): ").split()

    if raspuns== sequence:
        print("✅Corect!")
        level+=1
        return 1
    else:
        print("❌Gresit! Secventa era: "," ".join(sequence))
        return 0;

