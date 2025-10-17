# Making the Tree Search

## Rules
The rules of the card game are quite simple.

1. Each player is dealt a suit of hands (e.g. diamonds or hearts). One suit is shuffled and left in the middle.
2. The top middle card is drawn and shown to both players. 
3. Both players choose a card from their deck, and simultaneously show each other the card. The winner of the round is the player with the higher card. The winner takes the middle card and keeps it stashed away as their points tally.
4. In the case of a draw, the two cards shown by the players are moved aside, and another middle card is drawn \textbf{on top} of the original middle card. The middle card is now the sum of these two.
5. This continues until there are no more cards left to draw. 
6. At the end of the game, the players add the cards that they have won. The player with the higher score wins. In the case of the 13 card game, there are 91 points available, so a draw is not possible.


For simplicity, lets move away from the cards framework and into a numbers framework. An Ace can be represented as 1, 2 as 2, and so on, up to a King which is worth 13.

It's assumed that each starting player knows which cards

## Game Modifications/Different Rules
It is possible (although I haven't tried it) to be able to play with 3 or more players, if you have another deck of cards to spare. You could also play, as we will see, with more or less than 13 numbers. 13 is simply a convenient number because of how many cards are in a suit, but at some point that will be ignored for testing reasons. It may be easier to test a simple program with 4 cards only (Ace, 2, 3 and 4), or have some fun and see what a game of 200 cards might look like, or if it's feasible.

You could also play with starting sets of numbers that aren't the same for each player. For instance, start with a [4, 5, 6], and give your opponent [1, 2, 3]. This will be especially useful for testing programs, as this should instantly give you the win.

## Commentary/Initial Thoughts
Initially you could see a certain strategy emerge - try and either "bluff" the opponent, making them waste their best cards while you put down one of your lowest to lose that round on purpose, or simply try and beat them by a little (i.e. put down an 8 if they've put down a 7). So your aim is to either win the round by a little, or lose it by a lot. However it's difficult to do this as while you have knowledge of which cards your opponent has by tracking the ones they have already put down, you don't know the upcoming middle cards or what your opponent will play next.

I started by playing two random players against each other just to get a feel for the distribution of points that I would see, and get a baseline control player to test better strategies against. I then played one with a rudimentary strategy - play either the value of the middle card, 1 above or 2 above it. If none of those are available, then play your highest card. The histogram of this against a random players is also available.

# Tree Search

My approach that I wanted to implement was a tree search. Essentially, the tree has alternating layers - the first layer involves flipping the middle card over, and the second layer is both players simultaneously making a move. I could not use minimax because that assumes one player plays before the other, or there are alternating turns.

However, it's obvious the state space grows drastically. A single move will have n middle card options, n of your cards remaining and n opponent cards, giving any given node $(n!)^3$ children, which is enormous. For n larger than 5 or 6 we will need a Monte Carlo method.


### BFS or DFS

BFS covers every node to a certain max depth, so it may not be a bad idea. But given that we'll be calculating the average of a bunch of children nodes, it makes it likely more difficult. One implementation may involve using BFS but picking a bunch of random nodes from each level (to limit the search space) and see how good your position actually is.

## Evaluation
We will need an evaluation function. The one I have come up with is:

Number of points left = i

My points = $x$

Opponents points = $y$ 

Sum of my remaining cards = $\alpha$ 

Sum of opponents remaining cards = $\beta$ 

$f(N) = \frac{k}{i}(w_1(\alpha - \beta) + w_2(x-y))$


$k$ is some normalising factor - not actually needed to compare positions within a game, but might be useful if I would like to compare positions from between games. My reasoning for dividing by $i$ is I would like when there are still lots of cards left, the positions are more neutral (closer to 0) while when there aren't many more cards left the positions should be more weighted towards one way or another. I may increase $i$ (change it to $i^2$ or some other power in the future) to accentuate this. $w_1$ and $w_2$ are nice that incraesing $w_2$ makes an algorithm more "agressive" (wants to win quickly) while increasing $w_1$ means it doesn't mind losing a few provided it has the power to win later. These parameters and this evaluation can be tuned later once the framework is set up.


# Post-Implementation Thoughts

The bot works successfully, and wins around 70-80% of games against a random opponent (in a simple, small game). It is important to remember that it's based of expected value, so it can't be asked to win 100% of games (although the game is inherently random, so no bot should win 100% of games unless you have a dominating hand). 

It performs slightly worse than my initial bot with rudimentary strategy playing against a random opponent, which surprised me. However it makes some sense given that (again) it's going off expected value. I suspect that against not a random opponent but a player with some actual strategy, the rudimentary strategic bot's win rate would decline faster than the tree search bot.

## Performance

The performance speed is quite poor, even for small, simpla games. The rudimentary strategy bot's time efficiency is far quicker. Even after implementing it to be a Monte Carlo Tree Search (choosing only a random selection of states assuming the opponent's next moves are equally likely), I only put it up to a 7 card game with a depth of 3 taking 4 samples per round. It's stll a lot of operations, but it took over 10 seconds to play a single game. I hate to think that for the traditional game it would take far longer.

## Areas for Potential Improvement

I believe that a significant portion of the time taken comes down overhead, which is at least a nice learning experience for me. A problem for me is that I kept creating copies of lists and then looping through them, which is costing me a lot of time and space. In the future I could refactor my code to include backtracking so that I'm only working with one master list and I'm just continually updating it based on where I'm at, although I'm not sure how well that would work in this tree search (although I think it's possible to make it work). Passing information through to be updated rather than recalculated would be great too.

Not performance related - it could be interesting to experiment with assuming that the opponent's choices are not equally weighted i.e. they tend to play cards closer to the actual value itself. Could also be interesting to play the tree search opponent against the rudimentary strategy bot opponent and see who wins.
