# combos.py
COMBOS = {
    ("Ne", "Tora", "Inu"):   "KATON - FIREBALL JUTSU 🔥",
    ("Ushi", "Ne", "Tora"):  "SHADOW CLONE JUTSU 👥",
    ("Tori", "Inu", "Ushi"): "CHIDORI ⚡",
}

def match_combo(sequence):
    return COMBOS.get(tuple(sequence), None)