import json
import os

SCORE_FILE = "scores.json"

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {"memorie": 0, "viteza": 0, "matematica": 0}

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)

def reset_scores():
    scores = {"memorie": 0, "viteza": 0, "matematica": 0}
    save_scores(scores)
    return scores