from actual_node_class import Node
import numpy as np

def chunk_average(lst, m):
    return [np.mean(lst[i:i+m]) for i in range(0, len(lst), m)]

def dfs(node, red, current_depth, max_depth):
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
            value = dfs(child, red = False, current_depth = current_depth, max_depth = max_depth)
            eval_values.append(value)
        return np.mean(eval_values) #Average child evaluation

    if not red:
        eval_values = []
        children = []
        #generate children - remember child states have already "played out" the hand drawn so points should be updated, draw mechanics, etc.

        for i in node.my_cards:
            for j in node.opponent_cards: #Loop through both sets of cards
                new_my_cards = [a for a in node.my_cards if a != i]
                new_opponent_cards = [b for b in node.opponent_cards if b != j]

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
            value = dfs(child, red = True, current_depth = current_depth + 1, max_depth = max_depth)
            eval_values.append(value)
        return np.mean(eval_values)
        



# ----------------------- try a quick setup to test it ----------------------- #

n = 4
my_cards = [1, 2, 3, 4, 5]
opponent_cards = [1, 2, 3, 4, 5]
middle_cards = [1, 3, 2, 8, 9]
current_middle = middle_cards.pop()
max_depth = 4




print(f'With a middle card of {current_middle}')
for i in my_cards:
    total_eval = 0
    for j in opponent_cards:
        new_my_cards = [a for a in my_cards if a != i]
        new_opponent_cards = [b for b in opponent_cards if b != j]
        root = Node(
            my_cards = new_my_cards,
            opponent_cards = new_opponent_cards,
            my_points = 0,
            opponent_points = 0,
            deck = middle_cards,
            carry = 0,
            current_middle = current_middle
            )
        
        total_eval += dfs(root, red=True, current_depth = 0, max_depth = min(max_depth, len(my_cards), len(opponent_cards), len(middle_cards)))
    print(f'{i} has an evaluation of {total_eval}')