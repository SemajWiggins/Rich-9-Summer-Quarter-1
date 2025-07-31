import pgzrun
import random

# === Game Constants ===
GRID_WIDTH = 20
GRID_HEIGHT = 12
GRID_SIZE = 60
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
GUARDMOVEINTERVAL = 0.5
BACKGROUNDSEED = 12345

# === Game Map ===
MAP = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W G      KG      G W",
    "W    WWWWWWWWWWW   W",
    "W    W         W   W",
    "W    W    W    W   W",
    "W       W P W      W",
    "W    W         W   W",
    "W    W         W   W",
    "W    WWWWWWWWWWW   W",
    "W        GK        W",
    "W                  D",
    "WWWWWWWWWWWWWWWWWWWW"
]

# === Game State ===
player = None
guards = []
keysToCollect = []
gameOver = False

# === Coordinate Conversion ===
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

# === Setup Game ===
def SetupGame():
    global player, keysToCollect, guards, gameOver
    gameOver = False
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)

# === Drawing ===
def DrawBackground():
    random.seed(BACKGROUNDSEED)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if x % 2 == y % 2:
                screen.blit("floor1", GetScreenCoords(x, y))
            else:
                screen.blit("floor2", GetScreenCoords(x, y))
            n = random.randint(0, 99)
            if n < 5:
                screen.blit("crack1", GetScreenCoords(x, y))
            elif n < 10:
                screen.blit("crack2", GetScreenCoords(x, y))

def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        screen.draw.text(
            "Game Over! Press Space to try again",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60, color="yellow"
        )

# === Player Movement ===
def MovePlayer(dx, dy):
    global gameOver
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    newX = x + dx
    newY = y + dy

    # Check bounds
    if not (0 <= newX < GRID_WIDTH and 0 <= newY < GRID_HEIGHT):
        return

    square = MAP[newY][newX]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) == 0:
            gameOver = True
        return

    player.pos = GetScreenCoords(newX, newY)

    # Check for key collection
    for key in keysToCollect[:]:  # iterate over a copy
        (keyX, keyY) = GetActorGridPos(key)
        if newX == keyX and newY == keyY:
            keysToCollect.remove(key)
            break

def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

def on_key_up(key):
    global gameOver
    if key == keys.SPACE and gameOver:
        SetupGame()

# === Guard Movement ===
def MoveGuard(guard):
    global gameOver
    if gameOver:
        return

    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)

    newX, newY = guardX, guardY

    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        newX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        newX -= 1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        newY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        newY -= 1

    # Immediate collision check (before moving)
    if (newX, newY) == (playerX, playerY):
        gameOver = True
        return

    def check_collision():
        if GetActorGridPos(player) == (newX, newY):
            global gameOver
            gameOver = True

    animate(guard, pos=GetScreenCoords(newX, newY), duration=GUARDMOVEINTERVAL, on_finished=check_collision)

def MoveGuards():
    for guard in guards:
        MoveGuard(guard)

# === Run Game ===
SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()
