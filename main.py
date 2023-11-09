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
    global count_round
    indice_rows = 5

    # quelle joueur doit jouer, en fonction du nombre de tour (paire / inpaire)
    if (count_round % 2) == 0:  # Si le numéro du round es paire = ROUGE qui joue
        player = 'ROUGE'
    else:                       # Sinon Bleu qui joue
        player = 'BLEU'
    print("\nAjout d'un nouveau jeton pour le joueur", player)


    # demande puis ajout du je ton dans la grille de jeu
    while True:
        user_input = input("Entrer la position (ligne) du jeton (0 -> 6) : ")

        if '0' <= user_input <= '6':
            column_input = int(user_input)
            if 0 <= column_input <= 6:
                while True:
                    if grid[indice_rows][column_input] == ' ':
                        if player == 'ROUGE':
                            grid[indice_rows][column_input] = 'R'
                            count_round += 1
                            return 0
                        elif player == 'BLEU':
                            grid[indice_rows][column_input] = 'B'
                            count_round += 1
                            return 0
                    else:
                        if indice_rows == 0:
                            print("colonnes remplie, choisir une autre")
                            indice_rows = 5
                            break
                        else:
                            indice_rows -= 1

        print("Erreure Saisie, valeure accépcté : nombre (0 1 2 3 4 5 6)")


# FCT : test si il y a un gagnant
def test_winner():
    red_win = 0
    blue_win = 0

    # test d'un gagnant sur les lignes
    for row in range(len(grid) - 3):
        for col in range(int(len(grid[0]))):
            if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col]:
                    if grid[row][col] == 'R':
                        red_win = 1
                        blue_win = 0
                    elif grid[row][col] == 'B':
                        red_win = 0
                        blue_win = 1
            
    # test d'un gagnant sur les colonnes
    for row in range(len(grid)):
        for col in range(int(len(grid[0]) - 3)):
            if grid[row][col] != 0 and grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3]:
                    if grid[row][col] == 'R':
                        red_win = 1
                        blue_win = 0
                    elif grid[row][col] == 'B':
                        red_win = 0
                        blue_win = 1
            
    # test d'un gagant sue les diagonales descendantes
    for row in range(len(grid) - 3):
        for col in range(int(len(grid[0]) - 3)):
                if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3]:
                    if grid[row][col] == 'R':
                        red_win = 1
                        blue_win = 0
                    elif grid[row][col] == 'B':
                        red_win = 0
                        blue_win = 1
                    
    # test d'un gagant sue les diagonal ascendantes
    for row in range(3, len(grid)):
        for col in range(int(len(grid[0])) - 3):
            if grid[row][col] != 0 and grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3]:
                if grid[row][col] == 'R':
                    red_win = 1
                    blue_win = 0
                elif grid[row][col] == 'B':
                    red_win = 0
                    blue_win = 1

    #gestion d'un gagnant
    if red_win == 1 and blue_win == 0:
        print("\nJoueur ROUGE gagne la partie !!!")
        return 0
    
    elif red_win == 0 and blue_win == 1:
        print("\nJoueur BLEU gagne la partie !!!")
        return 0
        

    return 1




######          CODE PRINCIPAL          ######

# Explication début de partie
print("\n---    DEBUT DE LA PARTIE   ---")
print("\nIl y a 2 joueur ROUGE et BLEU")
print("\nROUGE = R\nBLEU = B\nvide =  ")
display_grid()

# Lancement de la partie
while test_winner():
    new_token()
    display_grid()
    