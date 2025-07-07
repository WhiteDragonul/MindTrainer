from score_memory import load_scores,save_scores
from games import memory_game,speed_game,math_game

def main():
    scores=load_scores()
    while True:
        print("\n🎮Mind Trainer🎮")
        print("1. Joc de memorie.")
        print("2. Joc de reactie.")
        print("3. Joc de calcule.")
        print("4. Vezi scorul.")
        print("0. Iesire")
        alegere=input("Alege un joc: ")

        if alegere == "1":
            scores["memorie"] += memory_game.play()
        elif alegere == "2":
            scores["viteza"] += speed_game.play()
        elif alegere == "3":
            scores["matematica"] += math_game.play()
        elif alegere == "4":
            print("\n📊 Scoruri curente:")
            for k, v in scores.items():
                print(f"{k.capitalize()}: {v}")
        elif alegere == "0":
            break
        else:
            print("❗ Opțiune invalidă!")

        save_scores(scores)

    if __name__ == "__main__":
        main()