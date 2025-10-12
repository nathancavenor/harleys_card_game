class Node:
    def __init__(self, my_cards, opponent_cards, my_points, opponent_points, deck, carry, current_middle):
        self.my_cards = my_cards
        self.opponent_cards = opponent_cards
        self.my_points = my_points
        self.opponent_points = opponent_points
        self.deck = deck
        self.carry = carry
        self.current_middle = current_middle
    
    def evaluate(self):
        w1 = 1
        w2 = 1
        return w1*(sum(self.my_cards)-sum(self.opponent_cards)) - w2*(self.my_points - self.opponent_points)
