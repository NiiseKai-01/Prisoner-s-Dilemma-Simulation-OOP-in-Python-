print("Starting Simulation")
import random
from player_classes import *

#### 1=Cooperate 0=Defect
### reward system
# |a\b|-1-|-0-| <br>
# |-1-|3,3|0,5| <br>
# |-0-|5,0|1,1|

payoff_matrix={
    (1,1):(3,3),
    (1,0):(0,5),
    (0,1):(5,0),
    (0,0):(1,1)
}

def payoff(a,b):
    winner = "None"
    a_act=a.act()
    b_act=b.act()
    a.opponent_last_moves.append(b_act)
    b.opponent_last_moves.append(a_act)
    a_reward,b_reward = payoff_matrix[(a_act,b_act)]
    a.rewards+=a_reward
    b.rewards+=b_reward
    if a_reward > b_reward:
        winner=a.name
    elif b_reward > a_reward:
        winner=b.name
    print(f"""Player 1 action = {a_act} and reward = {a_reward}, Player 2 action = {b_act} and reward = {b_reward} ==> Winner = {winner}""")

#Function to quit game
def quit_game(*args):
    print("Thank you for Playing")

#Function to print all players till now in a run
def print_players(*args):
    for i in player.all_players:
        print(i)

#Function to select a random strategy from switch
#also a soution for getting 5th strategy in switch ultimately avoiding infinite input
#after entering 5 in input then getting Invalid input printed
def random_choice(name):
    strategy = random.choice([always_cooperate,
                              always_defect,
                              titfortat,
                              Grim_trigger,
                              Random])
    return strategy(name)

# strategies = [always_cooperate,always_defect,titfortat,Grim_trigger,Random]
# switch = {1:always_cooperate,
#           2:always_defect,
#           3:titfortat,
#           4:Grim_trigger,
#           5:lambda :random.choice(strategies),
#           6:Random,
#           7:quit}

#below is a switch for selecting any type of strategy in runtime
switch = {1:always_cooperate,
          2:always_defect,
          3:titfortat,
          4:Grim_trigger,
          5:random_choice,
          6:Random,
          7:quit_game}

#main game loop which executes the program
while True:
    
    print("""
    All strategies with their respective index:
        (1) Always Cooperate
        (2) Always Defect
        (3) Tit-for-Tat    
        (4) Grim Trigger    
        (5) Random Strategy    
        (6) Rando    
        (7) Quit                
    """)
    
    #prompting the user to input strategy 1
    while True:
        try:
            select1=int(input("Select Strategy for Player 1: "))
            if select1 in switch:
                break
            else:
                print("Invalid input. Please try again")
        except ValueError:
            print("Invalid input. Please try again")
    if select1 == 7:
        quit_game()
        break

    #selecting a strategy class according to the switch
    p1=switch.get(select1,quit_game)(input("Enter name for player 1: "))
    
    #prompting the user to input strategy 2
    while True:
        try:
            select2=int(input("Select Strategy for Player 2: "))
            if select2 in switch:
                break
            else:
                print("Invalid input. Please try again")
        except ValueError:
            print("Invalid input. Please try again")
    if select2 == 7:
        quit_game()
        break

    #selecting a strategy class according to the switch
    p2=switch.get(select2,quit_game)(input("Enter name of player 2: "))
    
    #prompting the user to input no of matches
    no_of_matches=int(input("Enter no of rounds to play: "))
    
    while no_of_matches:
        payoff(p1,p2)
        p1_op_moves=p1.opponent_last_moves
        p2_op_moves=p2.opponent_last_moves
        no_of_matches-=1
    
    print(f"Total rewards of {p1.name} = {p1.rewards},OP moves = {p1_op_moves}")
    print(f"Total rewards of {p2.name} = {p2.rewards},OP moves = {p2_op_moves}")
    
    if p1.rewards > p2.rewards:
        end_winner = p1.name
    elif p2.rewards > p1.rewards:
        end_winner = p2.name
    else:
        end_winner = None
    
    print(f"The winner is {end_winner}")
    print("-"*50)
    contin_ue = int(input("Enter 1 to continue and 0 to end and print all players till now: "))
    if contin_ue !=1:
        print_players(contin_ue)
        quit_game(contin_ue)
        break