import random
import sys
import time
print()
# PIG


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# value = roll()
# print(value)

while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 -4 players!.')

    else:
        print('Invalid, Try Again!!')

# print(players)
max_score = 50
players_scores = [0 for _ in range(players)]

# print(players_scores)

while max(players_scores) < max_score:

    for player_idx in range(players):
        print(f'\nPlayer number, {player_idx + 1}, turn has just started!\n')
        print(f'Your score is: {players_scores[player_idx]}, \n')
        current_score = 0

        while True:

            should_roll = input('Would you like to roll (y):  ')
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print(f'You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a: {value}!')

            print(f'You rolled a: {current_score}!')

        players_scores[player_idx] += current_score
        print(f'Your Total Score is: {players_scores[player_idx]}')

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print(
    f'Player Number, {winning_idx + 1} is the winner with a score of: {max_score}\n')
