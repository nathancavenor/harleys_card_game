from actual_node_class import Node
import numpy as np
import random

def chunk_average(lst, m):
    return [np.mean(lst[i:i+m]) for i in range(0, len(lst), m)]

def dfs_with_random(node, red, current_depth, max_depth, no_samples):
    if red:
        if current_depth == max_depth:
            return node.evaluate()
        
        eval_values = []
        children = []

        #generate red children

        for i in node.deck:
            new_deck = [j for j in node.deck if j != i]
            new_node = Node(
                my_cards = node.my_cards,
                opponent_cards = node.opponent_cards,
                my_points = node.my_points,
                opponent_points = node.opponent_points,
                deck = new_deck,
                carry = node.carry,
                current_middle = i
            )
            children.append(new_node)

        for child in children:
            value = dfs_with_random(child, red = False, current_depth = current_depth, max_depth = max_depth, no_samples=no_samples)
            eval_values.append(value)
        return np.mean(eval_values) #Average child evaluation

    if not red:
        eval_values = []
        children = []
        #generate children - remember child states have already "played out" the hand drawn so points should be updated, draw mechanics, etc.

        random_my_choices = random.sample(node.my_cards, min(no_samples, len(node.my_cards)))
        random_opponent_choices = random.sample(node.opponent_cards, min(no_samples, len(node.opponent_cards)))

        for i in random_my_choices:
            for j in random_opponent_choices: #Loop through both sets of cards
                new_my_cards = [a for a in random_my_choices if a != i]
                new_opponent_cards = [b for b in random_opponent_choices if b != j]

                if i > j:
                    new_my_points = node.my_points + node.current_middle + node.carry
                    new_opponent_points = node.opponent_points
                    new_carry = 0
                elif i < j:
                    new_my_points = node.my_points
                    new_opponent_points = node.opponent_points + node.current_middle + node.carry
                    new_carry = 0
                else:
                    new_my_points = node.my_points
                    new_opponent_points = node.opponent_points
                    new_carry = node.carry + node.current_middle
                
                child = Node(
                    my_cards = new_my_cards,
                    opponent_cards = new_opponent_cards,
                    my_points = new_my_points,
                    opponent_points = new_opponent_points,
                    deck = node.deck,
                    carry = new_carry,
                    current_middle = node.current_middle
                )
                children.append(child)
        
        for child in children:
            value = dfs_with_random(child, red = True, current_depth = current_depth + 1, max_depth = max_depth, no_samples = no_samples)
            eval_values.append(value)
        return np.mean(eval_values)
