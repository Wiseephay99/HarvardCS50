import random
print()

# rock paper scissors
#
'''
    Ask the user ro make a choice
    if choice is not valid...print an error  
    let the compter to make a choice   
    print choices (emojis)
    determine the winner 
    Ask the user if they want to continue 
    If not .....Terminate
'''

'''
def play():
    user = input(
        "What's your choice...'r' for rock..\n'p' for paper..\n's' for scissors...\n\n ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return f'It\'s a Tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'Player Won!'
    return f'You Lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True
'''


def rps():
    choice = input(
        "choose...\n'r' for rock🪨\n'p' for paper📃\n's' for scissors✂️✂️..\n\n")
    computer = random.choice(['r', 'p', 's'])

    show = display(choice, computer)
    print(show)

    if choice == computer:
        return f'\nIt\'s a Tie'

    if is_winner(choice, computer):
        return f'\nPlayer Won'

    return f'\nYou Lost'


def display(choice, computer):
    return f'\nPlayer chose: {choice}\nCompuer chose: {computer}'


def is_winner(choice, computer):
    if ((choice == 'r' and computer == 'p') or
            (choice == 'p' and computer == 's') or
            (choice == 's' and computer == 'r')):
        return True


result = rps()
print(result)
