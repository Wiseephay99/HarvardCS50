import random

# ======================================================================
# ======================================================================
# ======================================================================

# Madlibs.py
youtuber = ''
youtuber = 'Wise Ephay'
print('subscribe to ' + youtuber)
print('subscribe to {}'.format(youtuber))
print(f'subscribe to {youtuber}')


# ======================================================================
# ======================================================================
# ======================================================================

print()
# Guess Number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:   '))
        if guess < random_number:
            print(f'Sorry...Guess again.....Too Low...\n')
        elif guess > random_number:
            print(f'Sorry...Guess again....Too high....\n')
    print(f'Yay, congrats. You have guess correctly the number')
guess(10)

# ======================================================================
# ======================================================================
# ======================================================================

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low(L), or correct(C)...\n\n')
        feedback = feedback.lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print('Yay..The computer guesses your number {guess} correctly...')

computer_guess(1000)

# ======================================================================
# ======================================================================
# ======================================================================

# rock paper scissors

def play():
    user = input("What's your choice...'r' for rock..\n, 'p' for paper..\n, 's' for scissors...\n\n ")
    computer = random.choice(['r','p','s'])
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

# ======================================================================
# ======================================================================
# ======================================================================