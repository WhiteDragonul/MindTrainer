import time
import random

def play():
    print("\n⚡ Joc de reactie rapida ⚡")
    print("Apasa Enter CAND vezi cuvantul 'GO'...")
    time.sleep(random.uniform(2, 5))
    print("GO!")
    start = time.time()
    input()
    reaction_time = time.time() - start

    print(f"Timpul tau de reactie: {reaction_time:.2f} secunde")

    if reaction_time < 0.5:
        print("🚀 Reflex rapid!")
        return 1
    else:
        print("🧱 Mai încearca!")
        return 0