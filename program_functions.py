import random
from nouns_exclusions import *
import stories

"""These are the game functions, input request functions excluded"""


def choose_story_and_play():
    input("Press ENTER to start ")
    story_template = random.randint(1, 3)
    if story_template == 1:
        stories.story_1()
    elif story_template == 2:
        stories.story_2()
    else:
        stories.story_3()


def check_input(input_str):
    """Makes sure the user enters only letters, not numbers or special symbols"""

    if input_str.isalpha():
        return True
    else:
        print("Your input should contain letters only.")
        return False


def choose_article(word):
    """Chooses the article before a noun or an adjective entered by the player"""

    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return "an"
    else:
        return "a"


def form_plural(word):
    """Puts a noun entered by the player in plural form, not depending on a number"""

    vowels = "aeiou"
    exceptions = ['s', 'ss', 'ch', 'sh', 'z']

    if word[-2:] in exceptions:
        return word + 'es'
    elif word.endswith(('f', 'fe')):
        return word[:-1] + 'ves'
    elif word.endswith('o') and word[:-2] not in vowels:
        return word + "es"
    elif word.endswith('y'):
        if word[-2] not in vowels:
            return word[:-1] + 'ies'
        else:
            return word + "s"
    elif word.endswith('is'):
        return word[:-2] + 'es'
    elif word in nouns_not_changing:
        return word
    elif word.endswith('x') and word not in [noun['singular'] for noun in other_nouns]:
        return word + 'es'
    for noun in irregular_nouns:
        if word == noun['singular']:
            return noun['plural']
    for noun in other_nouns:
        if word == noun['singular']:
            return noun['plural']
    else:
        return word + 's'


def check_num(number, noun):
    """Checks the number the user entered before a noun to put the noun in the correct form"""
    if number > 1:
        return form_plural(noun)
    else:
        return noun


def choose_word_story (number):
    """Returns the word 'story' in singular or plural form based on the given number.
    This function addresses a small bug in Template3 where the word 'stories' was used in plural.
    It ensures proper grammar by returning the word 'story' when the number is 1"""

    word = "story"
    if number == 1:
        return word
    else:
        form_plural(word)


def continue_or_exit():
    """This function repeatedly asks the player to choose if they want to continue playing or exit the game,
    allowing for the game to run until the player decides to exit."""

    while True:
        question = input("\nDo you want to play again? Pres 'Y' for yes, 'N' for no: ").upper()
        if question == 'N':
            print("\nEXITING GAME... HAVE A NICE DAY!")
            return False
        elif question == 'Y':
            choose_story_and_play()
            return True
        else:
            print("Invalid input. Please choose 'N' or 'Y'")
