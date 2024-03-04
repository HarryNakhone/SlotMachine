import random

ROW =3
COL = 3

symbol_counts = {
    "S": 1,
    "A": 3,
    "B": 4,
    "C": 5
}

symbol_values = {

    "A":5,
    "B":4,
    "C":3,
    "D": 2

}

LINES = [1,2,3]
BET_MAX = 100
BET_MIN = 2
def deposit(): 
    while True:
        amount = input("Deposit the amount $$$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The Amount must be larger than zero - 0")
        else:
            print("Please enter a number.")
    
    return amount

def run_slot_wheels(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_num in symbols.items():
        for _ in range(symbol_num):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column =[]
        copied_syms = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            copied_syms.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot(columns):
   
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")
        
        print()


def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check= column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_num_lines():
    while True:
        lines = input("Please enter the amount of lines from 1 to "+ str(LINES[len(LINES)-1]) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if lines in LINES:
                break
            else:
                print("print enter the number of line between 1 - 3 ONLY ")
        else:
            print("Enter only integer VALUES")

    return lines

def bet_values():
    while True:
        betAmount = input("Input how much do you want to bet $ ")
        if betAmount.isdigit():
            betAmount = int(betAmount)
            if BET_MIN <= betAmount <= BET_MAX:
                break
            else:
                print(f"Please enter number only between ${BET_MIN} to ${BET_MAX}")
        else:
            print("Please enter only valid integer")
    return betAmount
def start(balance):
    lines = get_num_lines()
    while True:
        bet = bet_values()
        total = bet * lines

        if total > balance:
            print (f"You only have ${balance} in your balance, pick smaller number to bet")
        else:
            break
        
  
    print(f"You bet ${bet} on each of {lines} lines and the total bet will be ${total}")
    
    slot = run_slot_wheels(ROW, COL, symbol_counts)
    print_slot(slot)
    winnings, winning_lines = check_win(slot, lines, bet, symbol_values)
    print(f"You won {winnings}")
    print(f"You won on lines : ", *winning_lines)
    return winnings - total

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press ener to start the slot machine or q to quit")
        if spin == "q":
            break
        balance += start(balance)

    print(f"you have ${balance}")
    


main()