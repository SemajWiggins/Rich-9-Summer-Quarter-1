# Import the Pygame module go start using its functions
import pgzrun

# Define width and height of the game grid & size of each grid tile
GRID_WIDTH = 16 # Defines how many squares wide the game board is
GRID_HEIGHT = 12 # Defines how many squares tall the game board is
GRID_SIZE = 50

# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W   KG      W",
       "W  WWWWWWWWWW  W", 
       "W              W",
       "W       P      W",
       "W  WWWWWWWWWW  W",
       "W       GK     W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]

# This function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

# This function draws the dungeon floor as a background on  screen
def DrawBackground():
    for y in range (GRID_HEIGHT): # loop over each grid row
        for x in range(GRID_WIDTH): # loop over each grid column
            pgzrun.screen.blit("floor1", GetScreenCoords(x, y)) # Draws the named imaged at the given screen
######################

########## 1.7 ##########
# This function creates an actor object from the Actor class to represent the player
def SetupGame():
    global player # Define player as a global var that can be accsessed anywhere in your code
    player = pgzrun.Actor("player", anchor=("left", "top")) #Create a new Anchor & test its new anchor
    for y in range(GRID_HEIGHT): # Loop over each grid position
        for x in range(GRID_WIDTH):
            square = MAP[y, x] # Extracts the character from the MAP variable 
            if square  == "P": # Checks if the grid position id the player 
                player.pos = GetScreenCoords # Set the position of the player
#########################

###########1.6###########
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

########################

# draw() is
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
########################    

######## 2.2 ###########
def MovePlayer(dx, dy):
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        return
    player.pos = GetScreenCoords(x, y)
########################

######### 2.3 ##########
# This Function gets a key from the user and moves the player based on the input
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0) # Player moves left one on the grid
    elif key == keys.UP:
        MovePlayer(0, -1) # Player moves up one on the grid
    elif key == key.RIGHT:
        MovePlayer(1, 0) # Player moves right one on the grid
    elif key == keys.DOWN:
        MovePlayer(0, 1) # Player moves down one on the grid
######################## 

##### 1.7, 3.0 #########
# This function creates an actor object from the Actor class to represent the player & keys
def SetupGame():


# Start the Pygame
SetupGame
pgzrun.go()
