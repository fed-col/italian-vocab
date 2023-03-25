import random
from utils import create_dict, tell_programming_joke

# Greeting message to the user
print(f"Ciao! Come stai? \nThis is an interactive tool to revise vocabulary.\n")
print(
    "Firstly, what lamguage would you like to translate from?\nYou can choose between ITA and ENG.\n"
)
from_lan = input("So my answer is... ").upper().strip()

# Check if the user's response is valid
while from_lan not in ("ITA", "ENG"):
    print("Your answer is not valid. Answer with either ITA or ENG, please.")
    from_lan = input("I would like to translate FROM... ").upper().strip()

# Set language to translate into
from_lan = "ITALIAN" if from_lan == "ITA" else "ENGLISH"
to_lan = "ENGLISH" if from_lan == "ITALIAN" else "ITALIAN"

# Create a dictionary from two text files and get the keys and values as lists
vocab_dict, keys = create_dict(
    file_path="ita_eng_db.csv", from_lan=from_lan, to_lan=to_lan
)

print(
    f"You will be given a word in {from_lan.capitalize()} and you have to translate it correctly into {to_lan.capitalize()}."
)
print("You have 3 attempts per word.\n")
print("Let's get started!")

# Initialise variables for the while loop
word = True
game = True
words_done = 0

# The main while loop to play the game
while game:
    try:
        # Choose a random word to ask the user to translate
        random_key = random.choice(keys)
        # Remove the chosen word from the list of words, so it's not repeated
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
        ans = (
            input(f'How do you translate into {to_lan.capitalize()} "{random_key}"?\n')
            .capitalize()
            .strip()
        )

        if ans == vocab_dict[random_key]:
            # If the answer is correct
            print(
                f'You got it right! It took you {count} attempt{"s" if count != 1 else ""}!\n'
            )

            # Ask the user if they want to continue with a new word
            cont = (
                input("Would you like to carry on with a new word? [Y / N] --> ")
                .strip()
                .upper()
            )

            # Check if the user's response is valid
            while cont[0] not in ("Y", "N"):
                print("Your answer is not valid. Answer with either Y or N, please.")
                cont = (
                    input("Would you like to carry on with a new word? [Y / N] --> ")
                    .strip()
                    .upper()
                )

            words_done += 1
            # End the current word loop and continue with the game loop if the user wants to continue
            word = False
            game = True if cont[0] == "Y" else False

        elif ans != vocab_dict[random_key] and count < 3:
            # If the answer is incorrect and the user has attempts remaining
            print(f"The answer is incorrect! This was your attempt number {count}!")
            print(
                f'Try again! You have {3-count} attempt{"s" if count != 1 else ""} remaining ^_^'
            )
            count += 1

        elif ans != vocab_dict[random_key]:
            # If the answer is incorrect and the user has used all attempts
            print(f"\nYour answer is incorrect! This was your 3rd attempt!")
            print(f"The correct answer was {vocab_dict[random_key]}")

            # Ask the user if they want to continue
            cont = input("Would you like to carry on? [Y / N] --> ").strip().upper()

            # Check if the user's response is valid
            while cont[0] not in ("Y", "N"):
                print("Your answer is not valid. Answer with either Y or N, please.")
                cont = (
                    input("Would you like to carry on with a new word? [Y / N] --> ")
                    .strip()
                    .upper()
                )

            words_done += 1
            # End the current word loop and continue with the game loop if the user wants to continue
            word = False
            game = True if cont[0] == "Y" else False


# Print a message to congratulate the user on revising words
print("--------------------")
print(
    f'\nNice work! You revised {words_done} word{"s" if words_done != 1 else ""} today! \U0001f600 \n'
)

# Print a joke to amuse the user
print("--------------------")
print("Here's a great joke as reward:\n")
tell_programming_joke()
print("--------------------")

# Print a message to say goodbye to the user
print(
    "\nGreat job! You've finished revising your vocabulary for today. Why not come back tomorrow and see how many words you can remember? Have fun learning! \U0001f389"
)
