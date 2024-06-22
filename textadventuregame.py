
def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are paths to the north, east, south, and west.")
    first_choice()

def first_choice():
    print("Which direction do you want to go? (north/east/south/west)")
    choice = input("> ").lower()
    if choice == "north":
        north_path()
    elif choice == "east":
        east_path()
    elif choice == "south":
        south_path()
    elif choice == "west":
        west_path()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def north_path():
    print("You head north and encounter a wild bear!")
    print("Do you want to fight the bear or run away? (fight/run)")
    choice = input("> ").lower()
    if choice == "fight":
        print("You fought bravely but the bear was too strong. You have been defeated.")
        game_over()
    elif choice == "run":
        print("You run away safely and find yourself back at the starting point.")
        first_choice()
    else:
        print("Invalid choice. Try again.")
        north_path()

def east_path():
    print("You head east and find a treasure chest!")
    print("Do you want to open the chest or leave it alone? (open/leave)")
    choice = input("> ").lower()
    if choice == "open":
        print("Congratulations! You found a rare gem and won the game!")
        play_again()
    elif choice == "leave":
        print("You decide to leave the chest alone and return to the starting point.")
        first_choice()
    else:
        print("Invalid choice. Try again.")
        east_path()

def south_path():
    print("You head south and find a river blocking your path.")
    print("Do you want to swim across or go back? (swim/back)")
    choice = input("> ").lower()
    if choice == "swim":
        print("The current was too strong. You got swept away and lost the game.")
        game_over()
    elif choice == "back":
        print("You decide to go back to the starting point.")
        first_choice()
    else:
        print("Invalid choice. Try again.")
        south_path()

def west_path():
    print("You head west and meet a wise old man.")
    print("He offers you a choice between two potions: one red and one blue. (red/blue)")
    choice = input("> ").lower()
    if choice == "red":
        print("You drink the red potion and gain super strength! You win the game!")
        play_again()
    elif choice == "blue":
        print("You drink the blue potion and fall into a deep sleep. You lose the game.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        west_path()

def game_over():
    print("Game over!")
    play_again()

def play_again():
    print("Do you want to play again? (yes/no)")
    choice = input("> ").lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Try again.")
        play_again()

# Start the game
intro()
