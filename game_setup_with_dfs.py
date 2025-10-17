from dfs import dfs
from dfs_with_random import dfs_with_random
from actual_node_class import Node
import random

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
                my_points = 0,
                opponent_points = 0,
                deck = middle_cards,
                carry = 0,
                current_middle = current_middle
            )
            total_eval += dfs_with_random(new_root, red=True, current_depth=0, 
                              max_depth=min(max_depth, len(my_cards), len(opponent_cards), len(middle_cards)), no_samples = 3)
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
    # Setup Wins Tracker
    no_total_games = 100
    my_scores = []
    opponent_scores = []
    wins = 0

    for j in range(no_total_games):
        # Setup Data
        n = 4
        my_cards = [1, 2, 3, 4, 5, 6, 7]
        opponent_cards = [1, 2, 3, 4, 5, 6, 7]
        middle_cards = [1, 3, 2, 8, 11, 12, 6]

        current_middle = middle_cards.pop()
        my_points = 0
        opponent_points = 0
        max_depth = 2

        root = Node(
            my_cards = my_cards,
            opponent_cards = opponent_cards,
            my_points = my_points,
            opponent_points = opponent_points,
            deck = middle_cards,
            carry = 0,
            current_middle = current_middle
        )

        # Play game
        for i in range(n):
            my_choice = my_choice_function(root)
            opponent_choice = opponent_choice_function(root)
            play_round(root=root, my_choice=my_choice, opponent_choice=opponent_choice)

        my_scores.append(root.my_points)
        opponent_scores.append(root.opponent_points)
        if root.my_points > root.opponent_points:
            wins += 1

    print(wins)
