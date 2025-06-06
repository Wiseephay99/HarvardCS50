import random
import time


print()


def spin_row():
    symbols = ['🍇', '🍉', '🥭', '🔔', '⭐']
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result


def display_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍇':
            return bet * 5
        elif row[0] == '🍉':
            return bet * 10
        elif row[0] == '🥭':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 10
    return 0


balance = 100
print("***************************")
print('Symbols:       🍇🍉🥭🔔⭐')
print("***************************")

while balance > 0:
    print(f'Current balance is ${balance:.2f}')
    bet = input('Place your bet amount:   ')
    if bet.lower() == 'q':
        break

    if not bet.isdigit():
        print('Enter a valid amount')
        continue

    bet = int(bet)

    if bet > balance:
        print('Insufficient Funds..')
        continue

    if bet <= 0:
        print('Bet must be greater than 0')
        continue

    balance -= bet

    time.sleep(1)
    print(f'Spinning ♻️ ♻️ ')
    time.sleep(2)

    row = spin_row()
    # print(row)

    display_row(row)

    payout = get_payout(row, bet)
    if payout > 0:
        print(f'You won: ${payout:.2f}')
    else:
        print(f'Sorry, you lost this round...')

    play_again = input('Continue Playing? (Y/N): ')
    if play_again.lower() == "y":
        continue
    else:
        break

print(f'Game over ..your current balance is ${balance:.2f}\n')
