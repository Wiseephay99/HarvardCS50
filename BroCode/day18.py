import time
import random
print()
#   python betting game


def spin_row():
    symbols = ['🍈', '🍉', '🍎', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('****************************')
    print(" | ".join(row))
    print('****************************')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍈':
            return bet * 5
        if row[0] == '🍉':
            return bet * 7
        if row[0] == '🍎':
            return bet * 8
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '🌟':
            return bet * 20
    # elif ((row[0] == row[1]) or
    #       (row[0] == row[2]) or
    #       (row[2] == row[1])):
    #     return bet * 5
    else:
        return 0


balance = 100

print('****************************')
print('Python Bet Spin and Win Game')
print('Symbols: 🍈🍉🍎🔔🌟🔔')
print('****************************')

while balance > 0:
    print(f'Current balance is ${balance:.2f}')
    bet = input('Enter bet amount (q to quit): ')

    if bet.lower() == 'q':
        break

    if not bet.isdigit():
        print('Invalid bet amount')
        continue

    bet = int(bet)

    if bet <= 0:
        print('Bet amount must be greater than 0')

    if bet > balance:
        print(f'Insufficient Funds!!\nYour balance is {balance:.2f}')
        continue

    balance -= bet

    row = spin_row()
    # print(row)

    display_row(row)

    payout = get_payout(row, bet)
    if payout > 0:
        balance += payout
        print(f'You won: {payout:.2f}')
    elif payout <= 0:
        print(f'Sorry 😔 😞 You did not win in this round!')

print('************************************')
print(f'Game Over...Your balance is: {balance:.2f}')
print('************************************')
