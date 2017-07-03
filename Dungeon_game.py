import os
import random

# Draw grid
# Pick random location for player
# Pick random location for exit door
# Pick random location for monster
# Draw player in the grid
# Take input for movement
# move player, unless invalid move (past edges of grid)
# Check for win or loss
# Clear screen and redraw grid

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1,1), (2,1), (3,1), (4,1),
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4),]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_location():
    return random.sample(CELLS, 3)

def move_player(player, move):
    # Get the player's location
    x,y = player
    # If move == LEFT, x-1
    if move == "LEFT":
        x -= 1
    # If move == RIGHT, x+1
    if move == "RIGHT":
        x += 1
    # If move == UP, y-1
    if move == "UP":
        y -= 1
    # If move == DOWN, y+1
    if move == "DOWN":
        y += 1
    return x, y

def get_moves(player):
    moves = ['LEFT','RIGHT','UP','DOWN']
    x,y = player
    # If player's x == 0, can't move left
    if x == 0:
        moves.remove("LEFT")
    # If player's x == 4, can't move right
    if x == 4:
        moves.remove("RIGHT")
    # If player's y == 0, can't move up
    if y == 0:
        moves.remove("UP")
    # If player's y == 4, can't move down
    if y == 4:
        moves.remove("DOWN")
    return moves

def draw_map(player):
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x,y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def game_loop():
    monster, door, player = get_location()
    playing = True
    
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        
        print("You're currently in room {}".format(player)) # Fill with player position
        print("You can move {}".format(",".join(valid_moves))) # Fill with available moves
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player, move)
            
            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! **\n")
                playing = False
                
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()

clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()

