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
    # test d'un gagnant sur les lignes
    for row in range(len(grid) - 3):
        for col in range(int(len(grid[0]))):
            if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col]:
                    if grid[row][col] == 'R':
                        return 1
                    elif grid[row][col] == 'B':
                        return 2
            
    # test d'un gagnant sur les colonnes
    for row in range(len(grid)):
        for col in range(int(len(grid[0]) - 3)):
            if grid[row][col] != 0 and grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3]:
                    if grid[row][col] == 'R':
                        return 1
                    elif grid[row][col] == 'B':
                        return 2
            
    # test d'un gagant sue les diagonal descendantes
    for row in range(len(grid) - 3):
        for col in range(int(len(grid[0]) - 3)):
                if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3]:
                    if grid[row][col] == 'R':
                        return 1
                    elif grid[row][col] == 'B':
                        return 2
                    
    # test d'un gagant sue les diagonal ascendantes
    for row in range(3, len(grid)):
        for col in range(int(len(grid[0])) - 3):
            if grid[row][col] != 0 and grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3]:
                if grid[row][col] == 'R':
                    return 1
                elif grid[row][col] == 'B':
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
                print("\nJoueur ROUGE gagne la partie !!!")
                end_game = 1
            case 2 :
                print("\nJoueur BLEU gagne la partie !!!")
                end_game = 1
    












"""

input_column = input("\nAjout d'un nouveau jeton pour le joueur ROUGE :\nEntrer une posistion (0 - 6) : ")
print("\n INPUT : ", input_column)



row = 2
col = 3
value = grid[row][col]
print(grid)
"""