import os
import sys
from random import randint
from time import sleep
import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

DIFFICULTY = [
    ["легко", 1],
    ["нормально", 2],
    ["тяжко", 3]
]

ATTEMPTS_NUM = {
    1: 3,
    2: 7,
    3: 15,
}

START_MENU = [
    ["розпочати", Fore.GREEN + "введи s" + Style.RESET_ALL],
    ["вийти", Fore.LIGHTRED_EX + "введи e" + Style.RESET_ALL],
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_number(hard_option):
    return randint(1, pow(10, hard_option) - 1)

def game_cycle():

    clear_console()

    print(Fore.YELLOW + "Привіт, ласкаво просимо у грі 'Вгадай число'")

    print(tabulate.tabulate(START_MENU, tablefmt="grid"))

    user_choice = input("Ввести: ")

    clear_console()

    match user_choice:
        case "e":
            print(Fore.YELLOW +  "До зустрічі!")
            sys.exit(0)
        case "s":
            pass

    clear_console()

    print(Fore.YELLOW  + "Вибери рівень складності: ")

    print(Fore.BLUE + tabulate.tabulate(DIFFICULTY, tablefmt="grid") + Style.RESET_ALL)

    difficulty = -1

    while difficulty not in [1, 2, 3]:
        try:
            difficulty = int(input("Ввести: "))
        except ValueError:
            continue

    guess_number = get_random_number(difficulty)

    attempts = ATTEMPTS_NUM[difficulty]

    clear_console()

    print(f"Я загадав число спробуй відгатати, у тебе є {attempts} спроб")

    while attempts > 0:
        sleep(3)
        clear_console()
        try:
            user_number = int(input("Твоє припущення: "))
        except ValueError:
            continue

        if user_number == guess_number:
            print(Fore.YELLOW +  f"Ти вгадав! Це число {user_number}\nДо зустрічі!")
            sys.exit(0)

        elif user_number < guess_number:
            print(Fore.BLUE + "Занадто мале!")
            attempts -= 1
            continue
        else:
            print(Fore.RED + "Занадто велике!")
            attempts -= 1
            continue

    print(Fore.LIGHTGREEN_EX + "Нажаль у тебе закінчилися спроби\nДо зустрічі!")











