
import sys
import random
from enum import Enum
def rps():
    gamecount = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal player_wins
        print()
        print('--------------------------------------------')  
        print('|            Rock Paper Scissors Game       |')
        print('--------------------------------------------')  

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input('Enter ...\n1. for Rock 🪨,\n2. for Paper 📃 , or\n3. for Scissors ✂️:\n\n')
        
        # using recurssive function
        if playerchoice not in ["1", "2", "3"]:
            print('You must enter 1, 2, or 3.')
            return play_rps()
        
        player = int(playerchoice)
        
        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print('-----------------------------------')
        # print(f'You chose: {playerchoice}')
        # print(f'Python chose: {playerchoice}')
        print(f'You chose: {str(RPS(player)).replace('RPS.','')}')
        print(f'Python chose: {str(RPS(computer)).replace('RPS.','')}')
        print('-----------------------------------')

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return '🏆🏆 You Win! 🏆🏆\n'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '🏆🏆 You Win! 🏆🏆\n'
            elif player == 3 and computer == 2:
                player_wins += 1
                return '🏆🏆 You Win! 🏆🏆\n'
            elif player == computer:
                return '😲 Tie Game! 🤓\n'
            else:
                python_wins += 1
                return '🐍 Python Wins!\n'
        game_result = decide_winner(player, computer)
        print(game_result)
        
        nonlocal gamecount
        gamecount += 1
        print(f'\n Game Count: {gamecount}')
        print(f'\n Player Wins: {player_wins}')
        print(f'\n Python Wins: {python_wins}')
        
        print('-----------------------------------')
        print('Play Again?')
        while  True:
            playagain = input('Y for Yes or \nQ to Quit \n\n')
            print('-----------------------------------')
        
            if playagain.lower() not in ["y" , "q"]:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return play_rps()
        else:
            print(f'\n🎉🎉🎉🎉🎉')
            print('Thank You for playing!')
            sys.exit(f'Bye!👋👋 \n')
    return play_rps()

rock_paper_scissors = rps()
if __name__ == '__main':
    rock_paper_scissors()
