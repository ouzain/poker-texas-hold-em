class Joueur:
    def __init__(self, nom, jetons):
        self.nom = nom
        self.jetons = jetons
        self.cartes = []
        self.actif = True

    def miser(self, montant):
        if montant > self.jetons:
            raise ValueError(f"{self.nom} n'a pas assez de jetons.")
        self.jetons -= montant
        return montant

    def se_coucher(self):
        self.actif = False

    def recevoir_cartes(self, cartes):
        self.cartes = cartes

    def __repr__(self):
        return f"Joueur({self.nom}, {self.jetons} jetons, Cartes: {self.cartes})"
