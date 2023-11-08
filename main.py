# puissance 4 

# Variables globale
rows, cols = 6, 7   # Taille de la grille de jeu
grid = [[' ' for i in range(cols)] for u in range(rows)]  # Création de la grille de jeu
count_round = 0  # Conteur de tour pour la gestion rouge / bleu
end_game = 0    # représente la fin de partie


# FCT : affichage de la grille avec l'indexe des colones
def display_grid():
    grid_index = [str(x) for x in range(7)]  # Création de la liste servant d'index pour l'affichage sur le moniteur série
    print("\n")
    for i in range(6):
        print(grid[i])
    print("---------------------")
    print(grid_index)

# FCT : ajouter un jeton dans la grille 
def new_token():
    indice_rows = 5
    if (count_round % 2) == 0:  # Si le numéro du round es paire = ROUGE qui joue
        player = 'ROUGE'
    else:                       # Sinon Bleu qui joue
        player = 'BLEU'

    print("\nAjout d'un nouveau jeton pour le joueur", player)
    input_column = int(input("Entrer la position (ligne) du jeton (0 - 6) : "))

    while 1:
        if grid[indice_rows][input_column] == ' ':
            if player == 'ROUGE':
                grid[indice_rows][input_column] = 'R'
                #count_round += 1
                return 0
            elif player == 'BLEU':
                grid[indice_rows][input_column] = 'B'
                #count_round += 1
                return 0
        elif indice_rows  == 0: 
            return 1       
        elif grid[indice_rows][input_column]  != ' ':
            indice_rows -= 1

        


# FCT : test si il y a un gagnant
def test_winner():
    indice_rows, indice_columns = 0, 0
    red_winner, blue_winner = 0, 0

    # test d'un gagnant sur les lignes

    for i in range(6): # pour chaque lignes
        for u in range(7):  # pour chaque colonnes
            if grid[i][u] == 'R':
                red_winner += 1
                blue_winner = 0
            elif grid[i][u] == 'B':
                red_winner = 0
                blue_winner += 1
            else:
                red_winner = 0
                blue_winner = 0
            
            # return si gaganant trouvé (1 = rouge 2 = bleu)
            if red_winner == 4:
                return 1
            elif blue_winner == 4:
                return 2

        
    # return 0 si aucun gagant n'est trouvé  
    return 0




# Code principale

# Explication début de partie
print("\n---    DEBUT DE LA PARTIE   ---")
print("\nIl y a 2 joueur ROUGE et BLEU")
print("\nROUGE = R\nBLEU = B\nvide =  ")

display_grid()

# Lancement de la partie

while end_game == 0:
    if new_token() != 0:
        print("colonne complète, impossible de remètre un jeton")
    else:
        count_round += 1
        display_grid()
    
    winner = test_winner()

    if winner != 0:
        match winner :
            case 1:
                print("Joueur ROUGE gagne la partie")
                break
            case 2 :
                print("Joueur BLEU gagne la partie")
                break
    












"""

input_column = input("\nAjout d'un nouveau jeton pour le joueur ROUGE :\nEntrer une posistion (0 - 6) : ")
print("\n INPUT : ", input_column)



row = 2
col = 3
value = grid[row][col]
print(grid)
"""