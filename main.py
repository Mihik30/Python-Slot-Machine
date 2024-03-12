import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

symbol_count = {
    "♠︎" : 2 ,
    "7" : 2 ,
    "☘︎" : 2 , 
    "♣︎" : 2 
}

symbol_value = {
    "♠︎" : 2 ,
    "7" : 2 ,
    "☘︎" : 2 , 
    "♣︎" : 2 
}

def check_win(columns , lines , bet , values):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol]*bet
            winning_line.append(line + 1)

    return winning,winning_line

def get_slots(rows,cols,symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symblo = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symblo.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if 1 != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("Enter an amount you want to deposite? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Enter a number.")

    return amount

def get_no_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1 to " +str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Enter a number.")

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet?₹")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} and ₹{MAX_BET}")
        else:
            print("Enter a number.")

    return bet

def spin(balence):
    lines = get_no_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balence:
            print(f"You dont have enough money , current balence ₹{balence}")
        else:
            break

    print(f"You are betting ₹{bet} on {lines} , total bet amount is ₹{total_bet}.")
    slots = get_slots(ROWS , COLS , symbol_count)
    print_slots(slots)
    winnings , winning_line = check_win(slots,lines,bet,symbol_value)
    print(f"You won ₹{winnings}")
    print(f"You won on {winning_line} lines")
    return winnings - total_bet


def main():
    balence = deposit()
    while True:
        print(f"Current balance is ₹{balence}")
        answer = input("Press enter to spin or q to quit ")
        if answer == 'q':
            break
        balence += spin(balence)
    print(f"You left with ₹{balence}")


main()