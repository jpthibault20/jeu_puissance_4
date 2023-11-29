import pygame
import sys


# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 0) * SQUARE_SIZE  # +1 for an additional row to display the selected column
grid = [[0 for i in range(COLUMN_COUNT)] for u in range(ROW_COUNT)]  # Creat board
ROUND = 1

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
RED_move = (134, 34, 0)
YELLOW = (255, 255, 0)
YELLOW_move = (134, 124, 0)
BLACK = (0, 0, 0)


# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")


# FCT : draw grid
def draw_grid():
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(screen,BLUE,(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),)


            match grid[row][col]:
                case 0:
                    pygame.draw.circle(screen,BLACK,(col * SQUARE_SIZE + SQUARE_SIZE // 2,row * SQUARE_SIZE + SQUARE_SIZE // 2,),int(SQUARE_SIZE * 0.4),)
                case 1:
                    pygame.draw.circle(screen,RED,(col * SQUARE_SIZE + SQUARE_SIZE // 2,row * SQUARE_SIZE + SQUARE_SIZE // 2,),int(SQUARE_SIZE * 0.4),)  
                case 2:
                    pygame.draw.circle(screen,YELLOW,(col * SQUARE_SIZE + SQUARE_SIZE // 2,row * SQUARE_SIZE + SQUARE_SIZE // 2,),int(SQUARE_SIZE * 0.4),)
                case 10:
                    pygame.draw.circle(screen,RED_move,(col * SQUARE_SIZE + SQUARE_SIZE // 2,row * SQUARE_SIZE + SQUARE_SIZE // 2,),int(SQUARE_SIZE * 0.4),)
                case 20:
                    pygame.draw.circle(screen,YELLOW_move,(col * SQUARE_SIZE + SQUARE_SIZE // 2,row * SQUARE_SIZE + SQUARE_SIZE // 2,),int(SQUARE_SIZE * 0.4),)


# FCT : pre drop piece
def pre_drop_piece(col):
    col_past = 10


    if col != col_past:
        col_past = col

        for row in range(ROW_COUNT):
            for col_ in range(COLUMN_COUNT):
                if grid[row][col_] > 2:
                    grid[row][col_] = 0

        invalide = True
        i = ROW_COUNT-1
                
        while invalide == True:
            if grid[i] [col] == 0:
                invalide = False
            elif i >= 0:
                i -= 1
                
        match ROUND:
            case 1:
                grid[i][col] = 10
            case 2:
                grid[i][col] = 20


#FCT : drop piece
def drop_piece(col):
    invalide = True
    i = ROW_COUNT-1
    while invalide == True:
        if grid[i] [col] == 0 or grid[i] [col] > 2:
            invalide = False
        elif i >= 0:
            i -= 1
        else :
            return 1

    if ROUND == 1:
        grid[i][col] = 1
        
    elif ROUND == 2:
        grid[i][col] = 2


# FCT : test si il y a un gagnant
def test_winner():
    red_win = 0
    yellow_win = 0

    # test d'un gagnant sur les lignes
    for row in range(len(grid) - 3):
        for col in range(int(len(grid[0]))):
            if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col]:
                    if grid[row][col] == 1:
                        red_win = 1
                        yellow_win = 0
                    elif grid[row][col] == 2:
                        red_win = 0
                        yellow_win = 1
            
    # test d'un gagnant sur les colonnes
    for row in range(len(grid)):
        for col in range(int(len(grid[0]) - 3)):
            if grid[row][col] != 0 and grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3]:
                    if grid[row][col] == 1:
                        red_win = 1
                        yellow_win = 0
                    elif grid[row][col] == 2:
                        red_win = 0
                        yellow_win = 1
            
    # test d'un gagant sue les diagonales descendantes
    for row in range(len(grid) - 3):
        for col in range(int(len(grid[0]) - 3)):
                if grid[row][col] != 0 and grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3]:
                    if grid[row][col] == 1:
                        red_win = 1
                        yellow_win = 0
                    elif grid[row][col] == 2:
                        red_win = 0
                        yellow_win = 1
                    
    # test d'un gagant sue les diagonal ascendantes
    for row in range(3, len(grid)):
        for col in range(int(len(grid[0])) - 3):
            if grid[row][col] != 0 and grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3]:
                if grid[row][col] == 1:
                    red_win = 1
                    yellow_win = 0
                elif grid[row][col] == 2:
                    red_win = 0
                    yellow_win = 1

    #gestion d'un gagnant
    if red_win == 1 and yellow_win == 0:
        return 1
    
    elif red_win == 0 and yellow_win == 1:
        return 2
        

    return 0



### MAIN
end_game = False

while end_game == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (drop_piece(event.pos[0] // 100) == 1):
                print("saisie invalide")
            else:
                for i in range(6):
                    print(grid[i])
                print("---------------------")

                winner = test_winner()

                match winner:
                    case 1:
                        print("Player Red win this game !!!")
                        end_game = True
                    case 2:
                        print("Player Yellow win this game !!!")
                        end_game = True

                ROUND = 3 - ROUND

        elif event.type == pygame.MOUSEMOTION:
            col = event.pos[0] //100
            pre_drop_piece(col)
                      
    draw_grid()
    pygame.display.update()