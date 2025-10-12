Making the Tree Search

The game works in pairs of two seperate stages:
1. Drawing the card from the middle of the deck
2. You and your opponent each simultaneously playing a card

In this way it works like a game tree, each level alternates "colour" (red and black coding): the red levels are drawing a card from the middle, the black levels are you and your opponent each playing a card.

The game scales very quickly. For instance, if there are 13 cards in both middle and each hand, that state will have 13^3 = 2197 children, only for one "progression" in the game. The state space grows as (n!)^3 which is enormous even for small values of n.

Each position needs an evaluation function, so we don't have to explore the entire state space. The one I have come up with is:



All of this will be put into a Latex doc report at the end of the project.

\section{Rules}
The rules of the card game are quite simple.
\begin{itemize}
\item Each player is dealt a suit of hands (e.g. diamonds or hearts). One suit is shuffled and left in the middle.
\item The top middle card is drawn and shown to both players. 
\item Both players choose a card from their deck, and simultaneously show each other the card. The winner of the round is the player with the higher card. The winner takes the middle card and keeps it stashed away as their points tally.
\item In the case of a draw, the two cards shown by the players are moved aside, and another middle card is drawn \textbf{on top} of the original middle card. The middle card is now the sum of these two.
\item This continues until there are no more cards left to draw. 
\item At the end of the game, the players add the cards that they have won. The player with the higher score wins. In the case of the 13 card game, there are 91 points available, so a draw is not possible.
\end{itemize}

For simplicity, lets move away from the cards framework and into a numbers framework. An Ace can be represented as 1, 2 as 2, and so on, up to a King which is worth 13.

It's assumed that each starting player knows which cards

\subsection*{Game Modifications/Different Rules}
It is possible (although I haven't tried it) to be able to play with 3 or more players, if you have another deck of cards to spare. You could also play, as we will see, with more or less than 13 numbers. 13 is simply a convenient number because of how many cards are in a suit, but at some point that will be ignored for testing reasons. It may be easier to test a simple program with 4 cards only (Ace, 2, 3 and 4), or have some fun and see what a game of 200 cards might look like, or if it's feasible.

You could also play with starting sets of numbers that aren't the same for each player. For instance, start with a [4, 5, 6], and give your opponent [1, 2, 3]. This will be especially useful for testing programs, as this should instantly give you the win.

\section{Commentary/Initial Thoughts}
Initially you could see a certain strategy emerge - try and either "bluff" the opponent, making them waste their best cards while you put down one of your lowest to lose that round on purpose, or simply try and beat them by a little (i.e. put down an 8 if they've put down a 7). So your aim is to either win the round by a little, or lose it by a lot. However it's difficult to do this as while you have knowledge of which cards your opponent has by tracking the ones they have already put down.

\end{document}