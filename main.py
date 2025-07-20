import json
import os

# OS clear helper function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# UNICODE CP437
with open('dictionaries/unicode/437/symbols.json', 'r', encoding='utf-8') as f:
    cp437_symbol_to_code = json.load(f)

with open('dictionaries/unicode/437/codes.json', 'r', encoding='utf-8') as f:
    cp437_code_to_symbol = json.load(f)

# UNICODE CP850
with open('dictionaries/unicode/850/symbols.json', 'r', encoding='utf-8') as f:
    cp850_symbol_to_code = json.load(f)

with open('dictionaries/unicode/850/codes.json', 'r', encoding='utf-8') as f:
    cp850_code_to_symbol = json.load(f)

# UNICODE CP1252
with open('dictionaries/unicode/1252/symbols.json', 'r', encoding='utf-8') as f:
    cp1252_symbol_to_code = json.load(f)

with open('dictionaries/unicode/1252/codes.json', 'r', encoding='utf-8') as f:
    cp1252_code_to_symbol = json.load(f)

# ASCII
with open('dictionaries/ascii/symbols.json', 'r', encoding='utf-8') as f:
    ascii_symbols = json.load(f)

with open('dictionaries/ascii/codes.json', 'r', encoding='utf-8') as f:
    ascii_codes = json.load(f)

# Symbol to code
def symbol_to_code_437(symbol):
    return cp437_symbol_to_code.get(symbol, None)

def symbol_to_code_850(symbol):
    return cp850_symbol_to_code.get(symbol, None)

def symbol_to_code_1252(symbol):
    return cp1252_symbol_to_code.get(symbol, None)

def ascii_symbol_to_code(symbol):
    return ascii_symbols.get(symbol, None)

# Code to symbol
def code_to_symbol_437(code):
    return cp437_code_to_symbol.get(str(code), None)

def code_to_symbol_850(code):
    return cp850_code_to_symbol.get(str(code), None)

def code_to_symbol_1252(code):
    return cp1252_code_to_symbol.get(str(code), None)

def ascii_code_to_symbol(code):
    return ascii_codes.get(str(code), None)

# Symbol to code
def symbol_to_code(symbol):
    clear_console()
    formats = [
        ("ASCII", ascii_symbol_to_code(symbol)),
        ("CP437", symbol_to_code_437(symbol)),
        ("CP850", symbol_to_code_850(symbol)),
        ("CP1252", symbol_to_code_1252(symbol))
    ]
    
    print(f"Symbol: '{symbol}'")
    print("┌────────┬────────┐")
    print("│ Format │ Code   │")
    print("├────────┼────────┤")

    for format_name, code in formats:
        code_str = str(code) if code is not None else "None"
        print(f"│ {format_name:<6} │ {code_str:<6} │")

    print("└────────┴────────┘")

    input("Press Enter to continue...")
    clear_console()

    return formats

# Code to symbol
def code_to_symbol(code):
    clear_console()
    formats = [
        ("ASCII", ascii_code_to_symbol(code)),
        ("CP437", code_to_symbol_437(code)),
        ("CP850", code_to_symbol_850(code)),
        ("CP1252", code_to_symbol_1252(code))
    ]
    
    print(f"Code: {code}")
    print("┌────────┬────────┐")
    print("│ Format │ Symbol │")
    print("├────────┼────────┤")

    for format_name, symbol in formats:
        symbol_str = symbol if symbol is not None else "None"
        print(f"│ {format_name:<6} │ {symbol_str:<6} │")

    print("└────────┴────────┘")

    input("Press Enter to continue...")
    clear_console()

    return formats

# Print dictionaries
def print_dictionaries():
    clear_console()
    choice = input("Available dictionaries:\n1. ASCII\n2. CP437\n3. CP850\n4. CP1252\n> ")

    if choice == '1':
        print("ASCII Dictionary")
        print("┌────────┬────────┐")
        print("│ Symbol │ Code   │")
        print("├────────┼────────┤")
        for symbol, code in ascii_symbols.items():
            print(f"│ {symbol:<6} │ {str(code):<6} │")
        print("└────────┴────────┘")
    elif choice == '2':
        print("CP437 Dictionary")
        print("┌────────┬────────┐")
        print("│ Symbol │ Code   │")
        print("├────────┼────────┤")
        for symbol, code in cp437_symbol_to_code.items():
            print(f"│ {symbol:<6} │ {str(code):<6} │")
        print("└────────┴────────┘")
    elif choice == '3':
        print("CP850 Dictionary")
        print("┌────────┬────────┐")
        print("│ Symbol │ Code   │")
        print("├────────┼────────┤")
        for symbol, code in cp850_symbol_to_code.items():
            print(f"│ {symbol:<6} │ {str(code):<6} │")
        print("└────────┴────────┘")
    elif choice == '4':
        print("CP1252 Dictionary")
        print("┌────────┬────────┐")
        print("│ Symbol │ Code   │")
        print("├────────┼────────┤")
        for symbol, code in cp1252_symbol_to_code.items():
            print(f"│ {symbol:<6} │ {str(code):<6} │")
        print("└────────┴────────┘")
    else:
        print("Invalid choice, returning to main menu.")
        return
    
    input("Press Enter to return to the main menu...")
    clear_console()

def main():
    clear_console()
    while True:
        choice = input("Choose an option:\n1. Symbol to Code\n2. Code to Symbol\n3. Print Dictionaries\n4. Exit\n> ")

        if choice == '1':
            symbol = input("Enter the symbol: ")
            symbol_to_code(symbol)
        elif choice == '2':
            code = input("Enter the code: ")
            code_to_symbol(code)
        elif choice == '3':
            print_dictionaries()
        elif choice == '4':
            clear_console()
            print("Bye ☺")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()