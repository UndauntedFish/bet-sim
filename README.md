# bet-sim
This Python program simulates the results of different betting techniques commonly used in games such as blackjack, baccarat, sports betting, and roulette.

## Usage
Clone the script and use the command "pip install -r requirements.txt" to install the required libraries to run the code.

## Betting Systems Included
### Reverse Labouchere
Reverse Labouchere is a betting technique used in a vast array of betting games. It works by first creating a "labby line" like so:
5-5-5-5-5
The first bet's amount will be the sum of the first and last number. In this case it is $10. 

If the bet wins, you remove the first and last numbers:
5-5-5

If the bet loses, you add the amount lost ($10) to the end of the line:
5-5-5-5-5-10
So now your next bet will be $5 + $10 = $15

You repeat this until the line is exhausted. Then you create another line and keep this pattern going.

#### Example
Say I wanted to test out whether the Reverse Labouchere betting system turns out a profit, assuming a 48.8% win chance at 1:1 odds.

I can call reverse_labouchere() with the following arguments:
  starting bankroll: $5,000
  labby-line: [5, 5, 5, 5, 5] (for a 5-5-5-5-5 labby line)
  labby_line_unit: $ (since the numbers in the labby line represent $5 not 5% of the bankroll)
  win_rate: 0.488 (for 48.8% win chance)
  odds: 1 (for even 1:1 odds)
  number_of_bets: 200

![image](https://github.com/UndauntedFish/bet-sim/assets/58181651/b135fd52-565b-4fdf-9702-8c8340eeaaea)

This gives the following result:

![image](https://github.com/UndauntedFish/bet-sim/assets/58181651/7c63ee52-8b75-4938-9779-549b23760024)

According to the graph, the Reverse Labouchere betting system appears to turn a profit over a large number of bets. However, it's a good idea to increase the number of bets and run multiple simulations to determine whether this betting system won because it was legitimately profitable, or if it just got on a lucky streak.

I'll now run the simulation with 1,000 bets instead of 200:

![image](https://github.com/UndauntedFish/bet-sim/assets/58181651/d8763ec8-2699-46aa-aed6-732740940f92)

Shortly before the 400th bet, all $5,000 of bankroll was lost. This graph shows that even though the Reverse Labouchere betting system may work in the short term, it will most likely end up losing long term. This is because each loss increases the next bet's size by $5, so all it takes are enough unluckily large losing streaks to lose all of your bankroll.

However, if you do happen to find a bet with favorable odds (such as a 51% win chance at 1:1 odds), this betting system works well long term.

![image](https://github.com/UndauntedFish/bet-sim/assets/58181651/09c3c9c6-ff3b-4b80-b469-a53f6fa67bf5)
