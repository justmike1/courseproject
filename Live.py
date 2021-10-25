import json
import pandas as pd
from abc import ABC, abstractmethod

def next_level():
    print('This is what you chose:')
    print(pd.read_json('input_data.json'))

def load_game():
    name = input("Hello There! What is your name? ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play!")
    d = {}
    d['Game'] = int(input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD to ILS. \n : "))
    if d['Game'] not in range(1, 4):
        print('num is invalid')
        return (main())
    d['Difficulty'] = int(input("Please choose game difficulty from 1 to 5: "))
    if d['Difficulty'] not in range(1, 6):
        print('num is invalid')
        return(main())
    return(name,d)


def main():
    out = {}
    while True:
        exit = input('Are you sure you want to play (y/n)? ')
        if exit.lower() == "n":
            break
        elif exit.lower() != "y":
            print("Try again")
            return(main())
        else:
            name, d = load_game()
            out[name] = d
    with open('input_data.json', 'w') as f: # I made a json to save input data
        json.dump(out, f, indent=2)


class WoG(ABC):
    pass

class MemoryGame(WoG):
    pass

class CurrencyRouletteGame(WoG):
    pass

class GuessGame(WoG):
    pass

if __name__ == "__main__":
    main()
