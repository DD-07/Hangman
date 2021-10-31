import random as ran
import sys

# Create list with all the hangman content
#create function to randomly choose the hangman content
# create function to see if the letter is present in the list
# create a function to see whether the player wins

# Ideas:
# Countries?
# Hint?

def main():
    lives = 5
    print("Welcome!")

    print("This is a game of hangman, where the topic will be... COUNTRIES! A random country will be generated and you will have to guess the letters in the word." )
    print("Note that everything will be in lower-case")



    country_list = ["usa", "mexico", "brazil", "egypt", "iran", "turkey", "china", "korea", "peru"]
    length = len(country_list)
    print("You will be tested on " + str(length) + " countries.")

    while True:
        country_chosen = country_list[ran.randrange(0, (length-1))]
        print(country_chosen)
        country_chosen = list(country_chosen)
        unknown_word = []
        unknown_length = len(unknown_word)
        for i in range(len(country_chosen)):
            unknown_word.append("_")
        print(unknown_word)
                while True:
            choice  = input("What letter do you choose?")
            is_in_word = False
            if choice in country_chosen:
                index = country_chosen.index(choice)
                unknown_word[index] = country_chosen[index]
                is_in_word = True
            else:
                is_in_word = False
            print(unknown_word)

            if is_in_word == False:
                lives -= 1


                if lives <= 0:
                    print("The answer was " + str(country_chosen))
                    print("Game over... :(")
                    win_lose()
                else:
                    print("You have " + str(lives) + " lives left.")
            else:
                if '_' in unknown_word:
                    pass
                else:
                    print("Good job!")
                    win_lose()

                pass
def win_lose():

    play_again = input("Play again?")
    while True:
        if play_again == "yes" or play_again == "Yes":
            main()
        else:
            sys.exit()

while True:
    main()



