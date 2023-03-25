import random
from utils import create_dict

# Greeting message to the user
print(f"Ciao! Come stai? \nThis is an interactive tool to revise vocabulary.")
print(
    "You will be given a word in Italian and you have to translate it correctly into English."
)
print("You have 3 attempts per word.\n")
print("Let's get started!")

# Create a dictionary from two text files and get the keys and values as lists
vocab_dict, keys, values = create_dict("ITA_vocab.txt", "ENG_vocab.txt")

# Initialise variables for the while loop
word = True
game = True
words_done = 0

# The main while loop to play the game
while game:
    try:
        # Choose a random key from the list of keys
        random_key = random.choice(keys)
        # Remove the chosen key from the list of keys
        keys.remove(random_key)
    except:
        # End the game if all keys have been used
        print(f"Wow! You have revised all the words you've studied!")
        print("You have no more revision to do!")
        break
    word = True

    # Counter for the number of attempts
    count = 1

    while word:
        # Get the user's answer
        ans = input(f'How do you translate into English "{random_key}"?\n')

        if str(ans).capitalize() == vocab_dict[random_key]:
            # If the answer is correct
            print(
                f'The answer is correct! It took you {count} attempt{"s" if count != 1 else ""}!\n'
            )
            # Ask the user if they want to continue with a new word
            cont = input("Would you like to carry on with a new word? [Y / N] --> ")

            # Check if the user's response is valid
            while cont[0].upper() not in ("Y", "N"):
                print("Your answer is not valid. Answer with either Y or N, please.")
                cont = input("Would you like to carry on with a new word? [Y / N] --> ")

            words_done += 1
            # End the current word loop and continue with the game loop if the user wants to continue
            word = False
            game = True if cont[0].upper() == "Y" else False

        elif str(ans).capitalize() != vocab_dict[random_key] and count < 3:
            # If the answer is incorrect and the user has attempts remaining
            print(f"The answer is incorrect! This was your attempt number {count}!")
            print(
                f'Try again! You have {3-count} attempt{"s" if count != 1 else ""} remaining ^_^'
            )
            count += 1

        elif str(ans).capitalize() != vocab_dict[random_key]:
            # If the answer is incorrect and the user has used all attempts
            print(f"\nYour answer is incorrect! This was your 3rd attempt!")
            print(f"The correct answer was {vocab_dict[random_key]}")

            # Ask the user if they want to continue
            cont = input("Would you like to carry on? [Y / N] --> ")

            # Check if the user's response is valid
            while cont[0].upper() not in ("Y", "N"):
                print("Your answer is not valid. Answer with either Y or N, please.")
                cont = input("Would you like to carry on with a new word? [Y / N] --> ")

            words_done += 1
            # End the current word loop and continue with the game loop if the user wants to continue
            word = False
            game = True if cont[0].upper() == "Y" else False


# Print a message to congratulate the user on revising words
print(f'Well done! You revised {words_done} word{"s" if words_done != 1 else ""} today :)')

# Print a message to say goodbye to the user
print(f"Take care!")
