# puissance 4 

# des variables globale
rows, cols = 6, 7
grid = [[0 for i in range(cols)] for u in range(rows)]
grid_index = [x for x in range(7)]
count_game = 0


# FCT : affichage de la grille avec l'indexe des colones
def display_grid():
    print("\n")
    for i in range(6):
        print(grid[i])
    print("---------------------")
    print(grid_index)

# FCT : 
def add_token():
    if (count_game % 2) == 0:
        player = 'ROUGE'
    else:
        player = 'BLEU'
    print("\nAjout d'un nouveau jeton pour le joueur %s", player)






# main
# Explication début de partie
print("\n---    DEBUT DE LA PARTIE   ---")
print("\nIl y a 2 joueur ROUGE et BLEU")
print("\nROUGE = 1\nBLEU = 2\nvide = 0")

display_grid()

input_column = input("\nAjout d'un nouveau jeton pour le joueur ROUGE :\nEntrer une posistion (0 - 6) : ")
print("\n INPUT : ", input_column)


"""
row = 2
col = 3
value = grid[row][col]
print(grid)"""