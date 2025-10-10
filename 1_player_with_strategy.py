import random
import numpy as np
import matplotlib.pyplot as plt

n = 13
repetitions = 10000

my_points_total = []
opponent_points_total = []
my_wins = 0
his_wins = 0

flag = False
carry = 0

for i in range(repetitions):
    my_cards = list(range(1, n+1))
    opponent_cards = list(range(1, n+1))
    deck = list(range(1, n+1))

    random.shuffle(my_cards)
    random.shuffle(opponent_cards)
    random.shuffle(deck)

    my_points = 0
    opponent_points = 0

    for j in range(n):
        middle = deck.pop()
        if flag:
            middle += carry
            flag = False
            carry = 0

        if middle in my_cards:
            mine = middle
            my_cards.remove(middle)
        elif middle + 1 in my_cards:
            mine = middle + 1
            my_cards.remove(middle + 1)
        elif middle + 2 in my_cards:
            mine = middle + 2
            my_cards.remove(middle + 2)
        else:
            mine = max(my_cards)
            my_cards.remove(mine)
        his = opponent_cards.pop()

        if mine > his:
            my_points += middle
        elif his > mine:
            opponent_points += middle
        else:
            flag = True
            carry = middle

    my_points_total.append(my_points)
    opponent_points_total.append(opponent_points)

    if my_points > opponent_points:
        my_wins += 1
    elif opponent_points > my_points:
        his_wins += 1

print("My wins:", my_wins)
print("His wins:", his_wins)
print("My average points:", np.mean(my_points_total))
print("His average points:", np.mean(opponent_points_total))

plt.figure(figsize=(10, 6))
plt.hist(my_points_total, bins=20, alpha=0.6, label='My Points', edgecolor='black')
plt.hist(opponent_points_total, bins=20, alpha=0.6, label='Opponent Points', edgecolor='black')
plt.xlabel("Total Points")
plt.ylabel("Frequency")
plt.title("Distribution of Total Points per Game")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()