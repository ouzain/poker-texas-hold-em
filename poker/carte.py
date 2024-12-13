


class Carte:
    def __init__(self, valeur, couleur):
        valeurs_valides = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
        if valeur not in valeurs_valides:
            raise ValueError(f"Valeur de carte invalide : {valeur}")
        if couleur not in ['♠', '♥', '♦', '♣']:
            raise ValueError(f"Couleur de carte invalide : {couleur}")
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur}{self.couleur}"
    
    def __repr__(self):
        return f"Carte(valeur={self.valeur}, couleur='{self.couleur}')"

