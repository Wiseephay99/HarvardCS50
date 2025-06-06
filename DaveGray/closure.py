print()

# Closure is a function having access to the parent scope, even after the parent function has closed.
# function after the parent function has finished executing.

def parent_function(person, coins):
    # coins = 3
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print(f'{person} has {coins} coins left.')
        elif coins == 1:
            print(f'{person} has {coins} coin left.')
        else:
            print(f'{person} has no coins left.')
    return play_game

Tommy = parent_function('Tommy', 3)    
# Tommy = parent_function('Tommy')    
Tommy()

Jenny = parent_function('Jenny', 5)
Jenny()