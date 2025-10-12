from collections import deque
import random

class Node:
    def __init__(self, my_cards, opponent_cards, my_points, opponent_points, deck, flag, carry):
        self.my_cards = my_cards
        self.opponent_cards = opponent_cards
        self.my_points = my_points
        self.opponent_points = opponent_points
        self.deck = deck
        self.flag = flag
        self.carry = carry

    def draw_middle(self):
        middle = random.choice(self.deck)
        new_deck = [c for c in self.deck if c != middle]
        return new_deck, middle
    
    def expand_random(self, num_samples):
        cards = random.sample(self.deck, min(num_samples, len(self.deck)))
        children = []
        for c in cards:
            new_deck = [x for x in self.deck if x != c]
            children.append((c, Node(
                my_cards=self.my_cards[:],
                opponent_cards=self.opponent_cards[:],
                my_points=self.my_points,
                opponent_points=self.opponent_points,
                deck=new_deck,
                flag=self.flag,
                carry=self.carry
            )))
        return children

    def generate_player_moves(self, middle_card):
        moves = []

        for my_card in self.my_cards:
            new_my_cards = self.my_cards.copy()
            new_my_cards.remove(my_card)

            for opponent_card in self.opponent_cards:
                new_opponent_cards = self.opponent_cards.copy()
                new_opponent_cards.remove(opponent_card)

                new_my_points = self.my_points
                new_opponent_points = self.opponent_points
                new_carry = self.carry
                new_flag = self.flag

                if my_card > opponent_card:
                    new_my_points += middle_card + new_carry
                    new_carry = 0
                    new_flag = False
                elif my_card < opponent_card:
                    new_opponent_points += middle_card + new_carry
                    new_carry = 0
                    new_flag = False
                else:
                    new_carry += middle_card
                    new_flag = True

                new_node = Node(
                    my_cards=new_my_cards,
                    opponent_cards=new_opponent_cards,
                    my_points=new_my_points,
                    opponent_points=new_opponent_points,
                    deck=self.deck.copy(),
                    flag=new_flag,
                    carry=new_carry
                )
                moves.append(new_node)

        return moves


    def evaluate(self):
        if not self.my_cards:
            if self.my_points > self.opponent_points:
                return float('inf')
            elif self.my_points == self.opponent_points:
                return 0
            elif self.my_points < self.opponent_points:
                return float('-inf')
        k = 1
        w1 = 1
        w2 = 1
        return k/sum(self.deck) * (w1*(sum(self.my_cards)-sum(self.opponent_cards)) - w2*(self.my_points - self.opponent_points))




def bfs(start_node, max_depth, num_samples):
    queue = deque([(start_node, 0)])
    best_eval = float('-inf')
    best_node = None

    while queue:
        node, depth = queue.popleft()
        val = node.evaluate()
        print(node.my_cards, node.opponent_cards, node.my_points, node.opponent_points)

        if val > best_eval:
            best_eval = val
            best_node = node
        
        if depth < max_depth and node.deck:
            for middle_card, chance_node in node.expand_random(num_samples):
                for move_node in chance_node.generate_player_moves(middle_card):
                    queue.append((move_node, depth+1))
    
    return best_eval, best_node

n = 5
root = Node(list(range(1, n)), list(range(1, n)), 0, 0, list(range(1, n)), False, 0)
final_choice = bfs(root, 4, 15)
print(final_choice[0], final_choice[1].my_cards, final_choice[1].opponent_cards, final_choice[1].my_points, final_choice[1].opponent_points, final_choice[1].deck)