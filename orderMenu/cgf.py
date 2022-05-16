#Common Game Funtions

def flipCoin():
    """ Determines whether the user or the AI gets to play as X, using heads or tails"""
    import random
    results = None
    choices = ["Heads", "Tails"]
    results = random.choice(choices)

    return results


def askNuminRange(question, low, high):
    """ ask the user a number withing a given range, and return the number if it is a good value"""
    while True:
        number = input(question)
        try:
            number = int(number)
            if number >= low:
                if number <= high:
                    return number
                else:
                    print("that number is too high")
            else:
                print("that number is too low")
        except:
            print("not a good number")

    return number


def rol_die(di_size):
    """gives random int between one and a given range"""
    import random
    roll = random.randint(1, di_size)
    return roll


def rancard(deck):
    """picks random item(card) from a list(deck)"""
    import random
    card = random.choice(deck)
    return card


def ask(question):
    """ask yes or no for questions"""
    while True:
        answer = input(question)
        if "y" in answer.lower() and "n" in answer.lower():
            print("not a valid option")
        elif "y" in answer.lower():
            return "yes"
        elif "n" in answer.lower():
            return "no"
        else:
            print("not a valid option")


def pick_from_menu(question, options):
    while True:
        for i in range(len(options)):
            print(str.format("\t{0} ...... {1:<30}", i + 1, options[i]))
        choice = input("what would you like to do? ")
        if choice.isnumeric():
            if int(choice) <= len(options):
                choice = int(choice)
                return choice
            else:
                print("That's not an option")
        else:
            print("That's' not a option")


if __name__ == "__main__":
    print("\nThis is a module, not a script. Try running the main")
    input("\n\n Press enter to exit")