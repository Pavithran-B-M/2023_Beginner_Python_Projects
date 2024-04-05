import pgzrun


GRID_WIDTH = 19 #defines the width of the game grid
GRID_HEIGHT = 15 #defines the height of the game grid
GRID_SIZE = 50 # defines the size of the game grid

GUARD_MOVE_INTERVAL = 0.4

WIDTH = GRID_WIDTH * GRID_SIZE #defines the width of the game window
HEIGHT = GRID_HEIGHT * GRID_SIZE #defines the hieght of the game window

MAP = ["WWWWWWWWWWWWWWWWWWW", #the follwong is the map defined as a list of 11 (y) entries and each entry is 16 (x) characters wide 
       "W       G         W",
       "W   WWWWWW WW     W", 
       "W   W       K     W", 
       "W   WWWWW WWW     W", 
       "W     W   K       W",
       "W     W  WWWWW    W",
       "W     W     W    GW",
       "W      W   W    G W",
       "W       WWW     G W", 
       "W        W        W", 
       "W   WWWWWWW W     W",
       "W   W   K   W     W",
       "W       P         D",
       "WWWWWWWWWWWWWWWWWWW"]


def screen_coords(x, y): #the following function converts grid positions x and y to screen coordinates that are spaced evenly by the grid size (each x and y is multiplied by the grid size)
    return (x * GRID_SIZE, y * GRID_SIZE)

def grid_coords(actor): # the following function is used to get the position of the actor on the map grid ~ converts the pixel position to grid position by dividing by one tile size
    return (round(actor.x/GRID_SIZE), round(actor.y/GRID_SIZE)) # the divison by the grid size is used to convert the pixel position to grid coordinates ex. (3,2) would mean on the third column and the second row

def setup_game():

    global game_over, player, keys_to_collect, guards, guard, player_won 
    global Actor

    player_won = False
    game_over = False # intiaally the variable is set to FALSE

    player = Actor("player", anchor=("left", "top"))
     #creates an actor object for the player (syntax is the Actor("Image file for object", anchor=("x anchor position", "y anchor position") ))
    

    keys_to_collect = [] #initally set the key_to_collect variable to an empty list
    
    guards = [] #sets guards to an empty list intially 

    for y in range(GRID_HEIGHT): #loops through the y coordinate positions
        for x in range(GRID_WIDTH): #loops through the x coordinate positions

            square = MAP [y][x] #extracts the characters from the MAP list representing the grid positions | yth row at xth position is looped over and over until the entire MAP is scanned

            if square =="P": # if the current grid position being looped through is P then set the position to player.pos 

                player.pos = screen_coords(x, y) # sets the position (hence --> pos) of the player to grid position where P is identified on the MAP
            
            elif square =="K": #if current grid position qued is K then the following fucntion will be executed

                key = Actor("key", anchor=("left", "top"), pos=screen_coords(x,y) ) #creates the key actor with image, achor and position depending on the MAP

                keys_to_collect.append(key) #takes the key actor from above and stores into the empty keys_to_collect library every time a grid position with K is identified

            elif square == "G": #if current grid position qued is G then the following set of code is executed

                guard = Actor("guard", anchor=("left", "top"), pos=screen_coords(x,y)) #an actor is set to the variable guard

                guards.append(guard) # adds the guard actor in que with the if statement to the guards dictionary



def draw_background():
    global screen
    for y in range(GRID_HEIGHT): # loops through 0 - 10
        for x in range(GRID_WIDTH): # loops through 0 - 15
            screen.blit("floor1", screen_coords(x, y)) # adds the "floor 1" image every iteration or loop

def draw_scenary(): 
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH): #this line and the line above loops over each grid position in the x and y 

            square = MAP[y][x] #extracts the characters from the map represented by the grid position | ex. MAP[1][4] --> is the 1st row with the 4th entry being qued

            if square == "W" : #draws at wall tile at the screen position represented by W on the MAP 
                screen.blit("wall", screen_coords(x,y))

            elif square == "D": #draws a door at the screen position represented by D on the MAP 
                screen.blit("door", screen_coords(x,y))

def draw_actors():
    global player
    player.draw() #draws the player actor on screen on its current position according to the MAP

    for key in keys_to_collect:
        key.draw()

    for guard in guards:
        guard.draw()

def draw_game_over():
    
    screen_middle = (WIDTH / 2, HEIGHT / 2)
    
    screen.draw.text("GAME OVER", midbottom=screen_middle, fontsize=GRID_SIZE, color="cyan", owidth=1) # creates the text on screen when the game is over
    
    if player_won:
        screen.draw.text("You won!", midtop=screen_middle, fontsize = GRID_SIZE, color = "green", owidth=1)

    else:
        screen.draw.text("You lost :(", midtop=screen_middle, fontsize = GRID_SIZE, color = "red", owidth=1)
    
    screen.draw.text("Press SPACE to play again", midtop=(WIDTH/2, HEIGHT/2 + GRID_SIZE), fontsize = GRID_SIZE/2, color="cyan", owidth=1)

def draw():
# the below functions are in chronological order layering the backgorund then the scenary and finally the actors
    draw_background()
    draw_scenary()
    draw_actors()

    if game_over: # if the game over variable is set to TRUE then the draw_game_over function begins
        draw_game_over()

def on_key_up(key): #this function allows the player to retry the game
    if key == keys.SPACE and game_over: #checks to see if the space bar is pressed and the game over variable is set to true
        setup_game()

def on_key_down(key): #this function will be used to create the movement from the USER (reacts according to arrow keys being pressed)
# the grid is going horizontally left to right (0->16), and vertically going down (0->11) | hence moving up would mean (0,-1) and moving down is (0, 1)
    if key == keys.LEFT:
        move_player(-1,0) 

    elif key == keys.UP:
        move_player(0, -1)

    elif key == keys.RIGHT:
        move_player(1,0)

    elif key == keys.DOWN:
        move_player(0,1)

def move_player(dx,dy): # dx and dy are pre-set in the on_key_down function and will be used to calculate the screen position after each key is pressed
    
    global game_over, player_won

    if game_over: #checks if game_over variable is set to TRUE ~ hence the game will terminate
        return
    
    (x,y) = grid_coords(player) #obtains current grid position of the player and stores the values into x and y respectively

    x += dx # AKA x = x + dx will provide the new x position

    y += dy # AKA y = y + dy will provide the new y position 

    square = MAP[y][x]

    if square == "W": # if the grid tile is a wall then the move_player function will terminate
        return 
    
    elif square == "D": # if the grid tile is a door then the move_player function will terminate
        
        if len(keys_to_collect) > 0: #checks the size of the key_to_collect list ~ if empty then the remaining code will execute
            return # returns if the list is not empty AKA not all keys have been collected 
        else:
            game_over = True # the variable game over will be set to True once all the keys are collected 
            player_won = True


    for key in keys_to_collect: #loops over each key actor in the keys_to_collect dictionary
        (key_x, key_y) = grid_coords(key) # stores the grid coordinates of each key actor to variables key_x and key_y respectively
        
        if x == key_x and y == key_y : # ensures the player actor and key actor posititon are matched up
            keys_to_collect.remove(key) # removes the qued key actor from the keys to collect list
            break #breaks out of the loop because there is one key for each tile
    player.pos = screen_coords(x,y) # updates the position and stores the new grid position of the player after the moving


def move_guard(guard): # a function with mutliple to conditions used to make the guards close in on the player actor

    global game_over

    if game_over: #the following condition is set to leave this function if the game_over variable is set to true
        return  
    
    (player_x, player_y) = grid_coords(player) #collects the grid position of the player and stores each value respectively to player_x and player_y

    (guard_x, guard_y) = grid_coords(guard) #collects the grid positions of the guard actors and stores each value respecively to guard_x and guard_y

    if player_x > guard_x and MAP[guard_y][guard_x+1] != "W": #if the player actor is farther to the right than the guard and the grid position + 1 to the right of the guard is not a wall then
        guard_x += 1 #moves the guard ~ new position is 1 more to the right

    elif player_x < guard_x and MAP[guard_y][guard_x-1] != "W": #check if the player is to the left of the guard and the wall condition again
        guard_x -= 1 #new guard position is one less than before, moves one tile left

    elif player_y > guard_y and MAP[guard_y+1][guard_x] != "W": #checks if player is higher than the guard 
        guard_y += 1 #add one tile unit to the guard

    elif player_y < guard_y and MAP[guard_y-1][guard_x] != "W": # checks if the player lower than the guard
        guard_y -= 1 #subtracts one tile unit to the guard

    
    animate(guard, pos=screen_coords(guard_x, guard_y), duration = GUARD_MOVE_INTERVAL, tween="bounce_start_end") # animates the movement of the guards
    
    if guard_x == player_x and guard_y == player_y : #if the guard and player positions are aligned
        game_over = True #game_over is set to true

def move_guards():# this following function is used to run the move guard function on each guard actor in the guards list
    for guard in guards: # loops through each guard character in the guards list
        move_guard(guard)


    

    print("Rendering Area Dimensions:", WIDTH, HEIGHT)
    print("Position of the Last Row:", screen_coords(0, GRID_HEIGHT - 1))

setup_game()
clock.schedule_interval(move_guards, GUARD_MOVE_INTERVAL)
pgzrun.go() #starts the game 
