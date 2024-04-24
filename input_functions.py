from program_functions import *

"""This module contains functions responsible for requesting input from the player.
All functions are arranged in alphabetic order,
and each function includes validation of the input to ensure the user enters appropriate data."""


def enter_animal():
    while True:
        animal = input("Enter an animal: ").lower()
        if check_input(animal):
            return animal


def enter_adjective():
    while True:
        adjective = input("Enter an adjective: ").lower()
        if check_input(adjective):
            return adjective


def enter_adverb_ly():
    while True:
        adverbly = input("Enter an adverb ending with 'ly': ").lower()
        if check_input(adverbly):
            return adverbly


def enter_bodypart():
    while True:
        part = input('Enter a part of the body: ').lower()
        if check_input(part):
            return part


def enter_color():
    while True:
        color = input("Enter an color: ").lower()
        if check_input(color):
            return color


def enter_creature():
    while True:
        creature = input("Enter a magical creature: ").lower()
        if check_input(creature):
            return creature


def enter_decoration():
    while True:
        decor = input("Enter a room decoration item: ").lower()
        if check_input(decor):
            return decor


def enter_feeling():
    while True:
        user_feeling = input("Enter an adjective meaning a feeling: ").lower()
        if check_input(user_feeling):
            return user_feeling


def enter_ing_verb():
    while True:
        verbing = input("Enter a verb ending with -ing: ").lower()
        if check_input(verbing):
            return verbing


def enter_name():
    """Requests the user to enter a proper name and converts it into title case,
    not depending on what register the user entered it in."""

    while True:
        user_input = input("Enter a name: ")
        if check_input(user_input):
            return user_input.title()


def enter_noun():
    while True:
        user_noun = input("Enter a noun: ").lower()
        if check_input(user_noun):
            return user_noun


def enter_number():
    """Asks the user to enter a number and makes sure that user inputs only numbers, not letters or symbols."""

    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            return int(num)
        else:
            print("Please enter an integer.")


def enter_place():
    while True:
        sword = input("Enter a place: ").lower()
        if check_input(sword):
            return sword


def enter_room():
    while True:
        room = input("Enter a room in a house: ").lower()
        if check_input(room):
            return room


def enter_sillyword():
    while True:
        sword = input("Enter any silly, non-existing word or gibberish: ").lower()
        if check_input(sword):
            return sword


def enter_time():
    while True:
        time_unit = input('Choose any measure of time, for example, "hour" or "year, or "month": ').lower()
        if check_input(time_unit):
            return time_unit
        else:
            print("The word must contain letters only.")


def enter_transport():
    while True:
        transportation = input('Type a mode of transport, for example, "bus", "car" or "spaceship": ').lower()
        if check_input(transportation):
            return transportation


def enter_verb():
    while True:
        user_verb = input("Enter a verb: ").lower()
        if check_input(user_verb):
            return user_verb
