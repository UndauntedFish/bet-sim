import pandas as pd
import numpy as np
import random


def reverse_labouchere(starting_bankroll, labby_line, win_rate, odds, number_of_bets, max_bet_size = 0.0):
    """
    Simulates the Reverse Labouchere betting strategy.

    Args:
        starting_bankroll (float): The initial bankroll for betting.
        labby_line (list): List of integers representing the Labouchere sequence. Ex) A labby line of 1-2-3-4-5 would be represented in a list as [1,2,3,4,5]
        win_rate (float): The probability of winning each bet (0.0 to 1.0).
        odds (float): The odds of winning (e.g., 1.0 for even money, 2.0 for 2:1, 0.5 for 0.5:1, etc.).
        number_of_bets (int): The number of bets to simulate.
        max_bet_size (float, optional): Will reset the labby line if bet sizes exceed this amount. Represented as a percentage of your bankroll. Ex) 2% max bet size means that the largest bet size can only risk 2% of your bankroll.

    Returns:
        list: List of bankroll amounts after each simulated bet.

    Description:
        This function simulates the Reverse Labouchere betting strategy, also known as the Cancellation betting system.
        It starts with a Labouchere sequence and modifies the sequence based on wins and losses.
        The strategy continues until the specified number of bets is reached or the Labouchere sequence is empty or the stop-out condition is met.

    Example:
        initial_balance = 1000
        labby_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
        win_probability = 0.48
        betting_odds = 1.0  # Even money
        num_bets = 100
        balances = reverse_labouchere(initial_balance, labby_sequence, win_probability, betting_odds, num_bets)
    """
    equity_curve = [starting_bankroll]
    working_labby_line = labby_line

    for _ in range(number_of_bets):
        # Get the percentage to risk for this bet. If labby line is 1-2-3-4-5, it will be 1+5=6%.
        percent_to_risk = working_labby_line[0] + working_labby_line[-1]

        # Reset the working labby line to the initial labby line if the bet size exceeds the maximum allowed bet size
        if (max_bet_size > 0.0 and percent_to_risk > max_bet_size):
            working_labby_line = labby_line

        # Simulate a bet. Will be true if the bet is a win, false if loss. 
        # random.random() draws a random number between 0.0 and 1.0
        bet_is_win = random.random() < win_rate

        if bet_is_win:
            # Use the last bankroll amount to calculate the amount won/lost.
            equity_curve.append(equity_curve[-1] * odds * percent_to_risk)
            
            # Remove the first and last elements from the working labby line.
            working_labby_line = working_labby_line[1:-1]
        else:
            # Use the last bankroll amount to calculate the amount won/lost.
            equity_curve.append(equity_curve[-1] * -odds * percent_to_risk)
            
            # Adds the amount risked on this bet to the end of the working labby line
            working_labby_line.append(percent_to_risk)
    
    return equity_curve

my_equity_curve = reverse_labouchere(5000, [5, 5, 5, 5, 5], 0.488, 1, 10)
print(my_equity_curve)