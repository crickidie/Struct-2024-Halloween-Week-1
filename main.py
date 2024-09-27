##############################################################
# created by: Deborah Sanchez
# email: debsanchez.business@outlook.com
# date: 9-27-2024
# desc: This sample Python project teaches you how to capture 
# user input. This project is week 1 of a 5 week project which
# can be downloaded at https://github.com/crickidie.
##############################################################

import os

def generate_title():
    print(" _    _                           _    _       _ _                              ")
    print("| |  | |                         | |  | |     | | |                             ")
    print("| |__| | __ _ _ __  _ __  _   _  | |__| | __ _| | | _____      _____  ___ _ __  ")
    print("|  __  |/ _` | '_ \| '_ \| | | | |  __  |/ _` | | |/ _ \ \ /\ / / _ \/ _ \ '_ \ ")
    print("| |  | | (_| | |_) | |_) | |_| | | |  | | (_| | | | (_) \ V  V /  __/  __/ | | |")
    print("|_|  |_|\__,_| .__/| .__/ \__, | |_|  |_|\__,_|_|_|\___/ \_/\_/ \___|\___|_| |_|")
    print("             | |   | |     __/ |                                                ")
    print("             |_|   |_|    |___/                                                 ")
    print("\n")

def generate_input(i):
    match i:
        case 0:
            txt = input("What's your name? ")
        case 1:
            txt = input("What's your favorite Halloween candy? ")
        case 2:
            txt = input("What's your favorite Halloween monster? ")
        case _:
            txt = input("What's your favorite Halloween movie? ")

    return txt

def generate_output(i, txt):
    match i:
        case 0:
            print("Hello", txt, end='')
            print(".")
        case 1:
            print("Oh, you like", txt, end='')
            print(".")
            print("My favorite Halloween candy is M&Ms!")
        case 2:
            print(txt, "is a great choice!")
            print("My favorite is Frankenstein.")
        case _:
            print("I also like", txt, "but my favorite movie is Friday the 13th: Jason Takes Manhattan.")
            print("How'd even get to the city? He's like magic!")

def main():
    os.system('cls')
    generate_title()

    txt = generate_input(0)
    generate_output(0, txt)

    txt = generate_input(1)
    generate_output(1, txt)

    txt = generate_input(2)
    generate_output(2, txt)

    txt = generate_input(3)
    generate_output(3, txt)

    input("Press enter to exit.")

if __name__ == "__main__":
    main()
