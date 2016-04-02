Again, you must be casually looking through my github.

Since March Madness is a hot time for teens, and I'm a lazy one of those, I wrote a program to generate brackets for me.

The main algorithm I used for probabilities was inherently simple. 

The probability of a team winning was determined by the formula:

1 - ((seed of team)/((seed of team) + (seed of opponent)))

Ex. No 1 seed v No 16 seed, the chances of the 1 seed winning are:

1 - 1/(1 + 16) = 16/17

To then pick the winning team, I generated a random float between 0 and 1.

If that float was below the probability of the first team winning, they won, else the other team wins.

As for input and output, the input is a bracket file in the format provided. Order matters or else divisions will be messed up.

Output will be the matchups for every round past the round of 64.

A sample output is provided. As you can see, some upsets do happen, but due to the probability, mostly high seeds move on.

Enjoy!
