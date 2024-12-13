from table import Table
from poker.joueur import Joueur

def initialiser_joueurs():
    """Crée et initialise les joueurs pour la partie."""
    joueurs = []
    nombre_joueurs = 0
    
    while nombre_joueurs < 2 or nombre_joueurs > 10:
        try:
            nombre_joueurs = int(input("Combien de joueurs (2 à 10) ? "))
            if nombre_joueurs < 2 or nombre_joueurs > 10:
                print("Le nombre de joueurs doit être compris entre 2 et 10.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(1, nombre_joueurs + 1):
        nom = input(f"Entrez le nom du joueur {i} : ").strip()
        jetons = 100  # Chaque joueur commence avec 100 jetons par défaut
        joueurs.append(Joueur(nom, jetons))

    return joueurs

def tour_de_jeu(table):
    """Gère un tour de jeu interactif."""
    for joueur in table.joueurs:
        if joueur.actif:
            print(f"\nC'est le tour de {joueur.nom} ({joueur.jetons} jetons disponibles).")
            action = input("Voulez-vous miser(m), se coucher(c) ou passer(p) ? ").strip().lower()
            if action == 'm':
                try:
                    montant = int(input("Combien voulez-vous miser? "))
                    table.pot += joueur.miser(montant)
                    print(f"{joueur.nom} a misé {montant}. Le pot est maintenant de {table.pot}.")
                except ValueError as e:
                    print(f"Action invalide : {e}")
                    joueur.se_coucher()
                    print(f"{joueur.nom} s'est couché.")
            elif action == 'c':
                joueur.se_coucher()
                print(f"{joueur.nom} s'est couché.")
            elif action == 'p':
                print(f"{joueur.nom} passe son tour.")
            else:
                print("Action non reconnue, vous passez automatiquement.")

if __name__ == "__main__":
    table = Table()
    table.melanger_cartes()

    # Initialisation des joueurs
    joueurs = initialiser_joueurs()
    for joueur in joueurs:
        table.ajouter_joueur(joueur)

    # Distribution des cartes
    table.distribuer_cartes()
    print(f"Joueurs : {table.joueurs}")

    # Phases de jeu
    print("\nPhase Flop :")
    table.phase_cartes_communes(3)
    print(f"Cartes communes : {table.cartes_communes}")
    tour_de_jeu(table)

    print("\nPhase Turn :")
    table.phase_cartes_communes(1)
    print(f"Cartes communes : {table.cartes_communes}")
    tour_de_jeu(table)

    print("\nPhase River :")
    table.phase_cartes_communes(1)
    print(f"Cartes communes : {table.cartes_communes}")
    tour_de_jeu(table)

    # Déterminer le gagnant
    table.determiner_gagnant()
