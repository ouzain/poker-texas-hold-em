from table import Table
from poker.joueur import Joueur

if __name__ == "__main__":
    table = Table()
    table.melanger_cartes()

    # Ajout des joueurs
    joueur1 = Joueur("Ousmane", 100)
    joueur2 = Joueur("Abdoulaye", 100)
    table.ajouter_joueur(joueur1)
    table.ajouter_joueur(joueur2)

    # Distribution des cartes
    table.distribuer_cartes()
    print(f"Joueurs : {table.joueurs}")

    # Phases de jeu
    print("Phase Flop :")
    table.phase_cartes_communes(3)
    print(f"Cartes communes : {table.cartes_communes}")

    print("Phase Turn :")
    table.phase_cartes_communes(1)
    print(f"Cartes communes : {table.cartes_communes}")

    print("Phase River :")
    table.phase_cartes_communes(1)
    print(f"Cartes communes : {table.cartes_communes}")

    # Déterminer le gagnant
    table.determiner_gagnant()
