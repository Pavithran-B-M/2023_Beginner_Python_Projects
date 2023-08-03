import random 

# the while loop is there because it must run the entire program (enables the last branch statement)
while True:

# double \n\n closes the string and skips one line to start the following string
    print("Welcome to team selector!\n")

    players = [

        "Martin", 'Craig', 'Sue', 'Claire', 'Dave', 
        'Alice', 'Luciana', 'Harry', 'Jack', 'Rose', 
        'Lexi', 'Maria', 'Thomas', 'James', 'William',
        "Ada", 'Grace', 'Jean', 'Marissa', 'Alan' 
                
                ]
    
    random.shuffle(players)

    # divide the above list into two seperate lists then, randonly choose one player from- 
    # each list to be team captain
    # from random module use the shuffle function to randomize the List


    team1_players = players[:len(players)//2] 

    team2_players = players[len(players)//2:] 

    team1_captain = random.choice(team1_players)

    team2_captain = random.choice(team2_players)

    print('Team One Captain: ' + team1_captain + '\n')

# line 37 - 41 is a for loop to print each article from the divided list , repeated from line 41 - 45

    for player in team1_players:
        
        print(player)

        
    print('\nTeam Two Captain: ' + team2_captain)

    for player in team2_players:
        
        print(player)

#  the following is tied to the while loop
    answer = str(input('Pick teams again? (Type y or n)'))

    if answer == "n":
            
            break
    
print('Best of Luck')