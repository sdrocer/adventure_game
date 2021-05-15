import time
import random

monsters = ["vampire", "gorgon", "oger", "giant", "troll",
            "death eater", "storm trooper", "idiot"]
jokes = ["I ate a clock yesterday, it was very time-consuming.",
         "Money talks. Mine always says goodbye.",
         "Don’t spell part backward. It’s a trap.",
         "My math teacher called me average. She’s so mean!",
         "When dogs go to sleep, they read bite-time stories before bed.",
         "I didn’t like my beard at first, but it grew on me.",
         "I had an “hourglass” figure, but then the sand shifted.",
         "Never trust atoms; they make up everything.",
         "Russian dolls are so full of themselves.",
         "A termite walks into the bar and asks, ‘Is the bar tender here?’"]


def print_slow(text_to_print):
    time.sleep(2)
    print(text_to_print)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt)
        if choice == option1:
            return choice
        elif choice == option2:
            return choice
        elif choice == "n":
            break
        else:
            print("This is not a valid option.")


def intro(monster):
    print_slow("You find yourself standing on an open clearing "
               "in the midst of a magical forest.")
    print_slow("Rumors has it that a " + monster + " is somewhere "
               "around here, and has been terryfing the nearby village.")
    print_slow("In front of you there is a wooden drawbridge leading to "
               "the entrance of a huge black castle.")
    print_slow("To your left there is a small brick house.\n")


def step_on_drawbridge(actions_taken, joke, monster):
    print_slow("Very carefully you step on to the drawbridge and "
               "make your way towards the castle.")
    print_slow("You are almost there, when suddenly the massive "
               "gate of the castle opens up.")
    print_slow("Out comes the " + monster + ".")
    print_slow("Oh no! This is the " + monster + "´s castle!")
    print_slow("The " + monster + " attacks you!")
    fight_monster(actions_taken, joke, monster)


def fight_monster(actions_taken, joke, monster):
    fight_or_flight = valid_input("Would you like to "
                                  "(1) fight or (2) run away?\n", "1", "2")
    if fight_or_flight == "1":
        if "talked_to_dwarf" in actions_taken:
            print_slow("You are about to fight the " + monster + " when "
                       "you remember the advice the dwarf has given you.")
            print_slow('"Hey ' + monster + ' have you heard of this one."')
            print_slow("The " + monster + " stops in front of you and "
                       "listens.")
            print_slow('"' + joke + '"')
            print_slow("This is too much for the " + monster + ".")
            print_slow("He lies on the floor laughing and shouting:")
            print_slow('"HAHAHA! Oh I need to leave this place! '
                       'Too many good jokes."')
            print_slow("You have rid the village of the " + monster + ". "
                       "You are victorious!")
            replay()
        else:
            print_slow("Unsure what to do you raise your fist.")
            print_slow("But the " + monster + " is quicker "
                       "He strikes you once and you fall to the ground.")
            print_slow("You have been defeated!")
            replay()
    elif fight_or_flight == "2":
        print_slow("You run back into the field. "
                   "Luckily, you don´t seem to have been followed.\n")
        take_action(actions_taken, joke, monster)


def enter_house(actions_taken, joke, monster):
    print_slow("You are about to knock when the "
               "door opens and out steps a little dwarf.")
    print_slow("He greets you, and begins talking:")
    if "talked_to_dwarf" in actions_taken:
        print_slow('"I already told you everything I know."')
        print_slow('"Farewell my friend!"')
        print_slow("You make your way back into the field.\n")
        take_action(actions_taken, joke, monster)
    else:
        print_slow('"Oh hello my dear fellow!"')
        print_slow('"If ever you will meet the '
                   + monster + ' these days, do not worry."')
        print_slow('"There is an easy but effective way to defeat him."')
        print_slow('"All you will have to do is make him laugh!"')
        print_slow('"Just tell him a good joke and he will leave this place!"')
        print_slow('"Farewell my friend!"')
        actions_taken.append("talked_to_dwarf")
    print_slow("You walk back out to the field.\n")
    take_action(actions_taken, joke, monster)


def take_action(actions_taken, joke, monster):
    print_slow("Enter 1 to step on the drawbridge.")
    print_slow("Enter 2 to knock on the door of the house.")
    print_slow("What would you like to do?")

    action = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if action == "1":
        step_on_drawbridge(actions_taken, joke, monster)
    elif action == "2":
        enter_house(actions_taken, joke, monster)


def replay():
    time.sleep(2)
    play_again = valid_input("Would you like to play again? (y/n)\n", "y", "n")
    if play_again == "y":
        print_slow("Restarting the game...\n")
        play_game()
    elif play_again == "n":
        print_slow("Thanks for playing! I hope you liked the game.")


def play_game():
    monster = random.choice(monsters)
    joke = random.choice(jokes)
    actions_taken = []
    intro(monster)
    take_action(actions_taken, joke, monster)


play_game()
