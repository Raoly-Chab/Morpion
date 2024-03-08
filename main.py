import os
import random

# Fonction pour afficher la grille du jeu
def afficher_grille(grille):
    for ligne in grille:
        print("|".join(ligne))
        print("-" * 5)

# Fonction pour créer une grille vide
def creer_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour placer un pion sur la grille
def poser_pion(grille, ligne, colonne, symbole):
    if grille[ligne][colonne] == " ":
        grille[ligne][colonne] = symbole
        return True
    else:
        return False

# Fonctions pour vérifier s'il y a une victoire
def verifier_lignes(grille, symbole):
    for ligne in grille:
        if all(case == symbole for case in ligne):
            return True
    return False

def verifier_colonnes(grille, symbole):
    for j in range(3):
        if all(grille[i][j] == symbole for i in range(3)):
            return True
    return False

def verifier_diagonales(grille, symbole):
    diagonale1 = all(grille[i][i] == symbole for i in range(3))
    diagonale2 = all(grille[i][2 - i] == symbole for i in range(3))
    return diagonale1 or diagonale2

# Fonction principale pour vérifier la victoire
def verifier_victoire(grille, symbole):
    return (verifier_lignes(grille, symbole) or 
            verifier_colonnes(grille, symbole) or 
            verifier_diagonales(grille, symbole))

# Fonction pour gérer le tour de jeu
def tour_de_jeu(grille, joueur):
    afficher_grille(grille)
    if joueur == "X":  # Tour du joueur humain
        while True:
            try:
                print(f"Tour du joueur {joueur}")
                ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
                colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))
                if 0 <= ligne < 3 and 0 <= colonne < 3:
                    if poser_pion(grille, ligne, colonne, joueur):
                        break
                    else:
                        print("Cette case est déjà occupée. Veuillez choisir une autre.")
                else:
                    print("Veuillez entrer des coordonnées valides.")
            except ValueError:
                print("Veuillez entrer des coordonnées valides (entiers).")
    else:  # Tour de l'adversaire (IA)
        ligne, colonne = choix_intelligent(grille, joueur)
        poser_pion(grille, ligne, colonne, joueur)
        print(f"L'adversaire a joué en ({ligne}, {colonne})")

# Fonction pour permettre à l'adversaire de jouer de manière stratégique
def choix_intelligent(grille, joueur):
    symbole_adversaire = "X" if joueur == "O" else "O"

    # Vérification des coups gagnants pour l'adversaire
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole_adversaire
                if verifier_victoire(grille, symbole_adversaire):
                    grille[i][j] = " "
                    return i, j
                grille[i][j] = " "

    # Bloquer les coups gagnants du joueur
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = joueur
                if verifier_victoire(grille, joueur):
                    grille[i][j] = " "
                    return i, j
                grille[i][j] = " "

    # Choisir un coup aléatoire s'il n'y a pas de coups gagnants ou de blocage nécessaires
    coups_disponibles = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(coups_disponibles)

# Fonction principale pour exécuter le jeu de Morpion
def jeu_morpion():
    os.system("cls" if os.name == "nt" else "clear")  # Efface l'écran
    print("Bienvenue dans le jeu de Morpion !")
    while True:
        grille = creer_grille()  # Crée une nouvelle grille
        joueur = "X"  # Définit le premier joueur comme "X"
        while True:
            tour_de_jeu(grille, joueur)  # Gère le tour de jeu
            if verifier_victoire(grille, joueur):  # Vérifie s'il y a une victoire
                afficher_grille(grille)
                print(f"Le joueur {joueur} a gagné !")
                break
            if all(all(case != " " for case in ligne) for ligne in grille):  # Vérifie s'il y a match nul
                afficher_grille(grille)
                print("Match nul !")
                break
            joueur = "O" if joueur == "X" else "X"  # Passe au prochain joueur
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()  # Demande si les joueurs veulent rejouer
        if rejouer != "o":  # Sort de la boucle si les joueurs ne veulent pas rejouer
            break

# Point d'entrée du programme
if __name__ == "__main__":
    jeu_morpion()  # Exécute le jeu de Morpion
