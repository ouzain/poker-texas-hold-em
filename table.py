import random
from treys import Evaluator, Card
from poker.carte import Carte

class Table:
    SUIT_MAPPING = {
        '♠': 's',  # Spades
        '♥': 'h',  # Hearts
        '♦': 'd',  # Diamonds
        '♣': 'c',  # Clubs
    }

    def __init__(self):
        self.jeu_de_cartes = [Carte(val, coul) for val in list(range(2, 11)) + ['J', 'Q', 'K', 'A']
                              for coul in ['♠', '♥', '♦', '♣']]
        self.cartes_communes = []
        self.pot = 0
        self.joueurs = []
        self.evaluator = Evaluator()

    def melanger_cartes(self):
        random.shuffle(self.jeu_de_cartes)

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def distribuer_cartes(self):
        for joueur in self.joueurs:
            joueur.recevoir_cartes([self.jeu_de_cartes.pop() for _ in range(2)])

    def phase_cartes_communes(self, nombre):
        self.cartes_communes.extend([self.jeu_de_cartes.pop() for _ in range(nombre)])

    def carte_to_treys(self, carte):
        """Convertit une carte en un format compatible avec Treys."""
        valeurs_mapping = {
            2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'
        }

        # Validation de la valeur
        if carte.valeur not in valeurs_mapping:
            raise ValueError(f"Valeur de carte inconnue : {carte.valeur}")

        valeur = valeurs_mapping[carte.valeur]
        couleur = self.SUIT_MAPPING[carte.couleur]
        return f"{valeur}{couleur}"


    def determiner_gagnant(self):
        scores = {}
        joueurs_actifs = [joueur for joueur in self.joueurs if joueur.actif]
        
        if len(joueurs_actifs) == 1:
            # Si un seul joueur est encore actif, il gagne automatiquement
            gagnant = joueurs_actifs[0]
            print(f"{gagnant.nom} gagne car tous les autres joueurs se sont couchés!")
            gagnant.jetons += self.pot
            self.pot = 0
            return

        if not joueurs_actifs:
            print("Oops !  Aucun joueur actif. Le jeu ne peut pas continuer.")
            return

        # Calcul des scores pour les joueurs actifs
        for joueur in joueurs_actifs:
            try:
                print(f"Main du joueur {joueur.nom}: {joueur.cartes}")
                print(f"Cartes communes : {self.cartes_communes}")
                main = [Card.new(self.carte_to_treys(carte)) for carte in joueur.cartes]
                commune = [Card.new(self.carte_to_treys(carte)) for carte in self.cartes_communes]
                score = self.evaluator.evaluate(commune, main)
                scores[joueur] = score
            except Exception as e:
                print(f"Erreur pour le joueur {joueur.nom}: {e}")
                raise e

        # Déterminer le gagnant parmi les joueurs actifs
        gagnant = min(scores, key=scores.get)
        print(f"Le gagnant est {gagnant.nom} avec un score de {scores[gagnant]}!")
        gagnant.jetons += self.pot
        self.pot = 0


