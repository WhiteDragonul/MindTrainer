import random
import time

def play():
    print("\n🧮 Joc de calcule mentale 🧮")
    a = random.randint(10, 50)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])
    expr = f"{a} {op} {b}"
    correct = eval(expr)

    print(f"Cat face: {expr}? (ai 5 secunde)")
    start = time.time()
    try:
        answer = input("Raspuns: ")
        duration = time.time() - start
        if duration > 5:
            print("⌛ Timpul a expirat!")
            return 0
        if int(answer) == correct:
            print("✅ Corect!")
            return 1
        else:
            print(f"❌ Gresit! Raspunsul era {correct}")
            return 0
    except:
        print("❌ Raspuns invalid!")
        return 0