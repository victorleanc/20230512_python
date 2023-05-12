import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "7": 4,
    "K": 6,
    "Q": 8,
    "J": 9
}

symbol_value = {
    "7": 10,
    "K": 6,
    "Q": 4,
    "J": 3,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="\033[1;34m | \033[m")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("\033[3;31mAmount must be greater than 0.\33[m")
        else:
            print("\033[3;31mPlease enter a number.\033[m")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How many lines do you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines > 0:
                break
            else:
                print("\033[3;31mEnter a valid number of lines.\033[m")
        else:
            print("\033[3;31mPlease enter a number.\033[m")
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"\033[3;31mBet amount must be between ${MIN_BET} and ${MAX_BET}.\033[m")
        else:
            print("Bet a valid amount.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"\033[3;31mYou do not have enough money to make this bet. Your current balance is ${balance}\033[m")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Total bet = ${total_bet}")
    print('\033[3;34m-\033[m' * 40)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'\033[1;32mYou won ${winnings}\033[m')
    print(f"You won on line(s): ", *winning_lines)
    print('\033[3;34m-\033[m' * 40)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is \033[3;34m${balance}\033[m")
        answer = input("Press enter to spin (q to quit.")
        if answer == "q":
            break
        balance += spin(balance)
    print('\033[3;34m-\033[m' * 40)
    print(f"You lef with \033[3;34m${balance}\033[m")


main()
