from dfs import dfs
from actual_node_class import Node
import random
import matplotlib.pyplot as plt

def my_choice_function(root):
    evals = {}
    for i in root.my_cards:
        total_eval = 0
        for j in root.opponent_cards:
            new_my_cards = [a for a in my_cards if a != i]
            new_opponent_cards = [b for b in opponent_cards if b != j]
            new_root = Node(
                my_cards = new_my_cards,
                opponent_cards = new_opponent_cards,
                my_points = root.my_points,
                opponent_points = root.opponent_points,
                deck = root.deck.copy(),
                carry = root.carry,
                current_middle = root.current_middle
            )
            
            total_eval += dfs(new_root, red=True, current_depth = 0, max_depth = min(max_depth, len(my_cards), len(opponent_cards), len(middle_cards)))
        #print(f'{i} has an evaluation of {total_eval}')
        evals[i] = total_eval
    return max(evals, key=evals.get)

def opponent_choice_function(root):
    opponent_choice = random.choice(root.opponent_cards)
    return opponent_choice

def play_round(my_choice, opponent_choice, root):
    if my_choice > opponent_choice:
        root.my_points += root.current_middle + root.carry
        root.carry = 0
    elif my_choice < opponent_choice:
        root.opponent_points += root.current_middle + root.carry
        root.carry = 0
    else:
        root.carry = current_middle
    root.my_cards.remove(my_choice)
    root.opponent_cards.remove(opponent_choice)
    if root.deck:
        root.current_middle = root.deck.pop()


if __name__ == "__main__":
    #Setup Wins Tracker
    no_total_games = 10
    my_scores = []
    opponent_scores = []
    wins = 0
    losses = 0
    draws = 0
    for j in range(no_total_games):
        #Setup Data
        n = 4
        my_cards = [1, 3, 6, 5, 2, 9]
        opponent_cards = [1, 2, 3, 8, 2, 3]
        middle_cards = [3, 6, 8, 2]

        random.shuffle(my_cards)
        random.shuffle(opponent_cards)
        random.shuffle(middle_cards)

        current_middle = middle_cards.pop()
        my_points = 0
        opponent_points = 0
        max_depth = 4

        root = Node(
            my_cards = my_cards,
            opponent_cards = opponent_cards,
            my_points = my_points,
            opponent_points = opponent_points,
            deck = middle_cards,
            carry = 0,
            current_middle = current_middle
            ) #Create starting root
        
        for i in range(n): #replace with while loop later to play the full game
            my_choice = my_choice_function(root)
            opponent_choice = opponent_choice_function(root)
            play_round(root=root, my_choice=my_choice, opponent_choice=opponent_choice)

        my_scores.append(root.my_points)
        opponent_scores.append(root.opponent_points)
        if root.my_points > root.opponent_points:
            wins += 1
        elif root.my_points < root.opponent_points:
            losses += 1
        else:
            draws += 1
    
    print(wins)
    print(losses)
    print(draws)