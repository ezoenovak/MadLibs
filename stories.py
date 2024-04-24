from input_functions import *


def story_1():
    number = enter_number()
    time = enter_time()
    time_used = check_num(number, time)
    transport = enter_transport()
    adjective = enter_adjective()
    article = choose_article(adjective)
    adjective2 = enter_adjective()
    noun = enter_noun()
    noun_plural = form_plural(noun)
    color = enter_color()
    body_part = enter_bodypart()
    body_part_plural = form_plural(body_part)
    verb = enter_verb()
    number2 = enter_number()
    noun2 = enter_decoration()
    noun2_number = check_num(number2, noun2)
    noun3 = enter_noun()
    body_part2 = enter_bodypart()
    verb2 = enter_verb()
    noun4 = enter_noun()
    adjective3 = enter_adjective()
    silly_word = enter_sillyword()
    noun5 = enter_noun()

    # PRINT THE STORY
    print(f"\n========================\n"
          f"HERE IS YOUR STORY!\n"
          f"========================\n"
          f"\nIt was about {number} {time_used} ago when I arrived at the hospital in a {transport}.\n"
          f"The hospital is {article} {adjective} place, there are a lot of {adjective2} {noun_plural} here.\n"
          f"There are nurses here who have {color} {body_part_plural}.\n"
          f"If someone wants to come into my room I tell them that they have to {verb} first.\n"
          f""
          f"I’ve decorated my room with {number2} {noun2_number}.\n"
          f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}.\n"
          f"I heard that all doctors {verb2} {noun4} every day for breakfast.\n"
          f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!\n"
          )


def story_2():
    propername = enter_name()
    noun = enter_noun()
    feeling = enter_feeling()
    verb = enter_verb()
    feeling2 = enter_feeling()
    animal = enter_animal()
    article = choose_article(animal)
    verb2 = enter_verb()
    color = enter_color()
    verb_ing = enter_ing_verb()
    adverb = enter_adverb_ly()
    number = enter_number()
    time_input = enter_time()
    time_used = check_num(number, time_input)
    color2 = enter_color()
    animal2 = enter_animal()
    number2 = enter_number()
    sillyword = enter_sillyword()
    choose_word_story(number2)
    noun2 = enter_noun()

    print(f"\n========================\n"
          f"HERE IS YOUR STORY!\n"
          f"========================\n"
          f"\nThis weekend I am going camping with {propername}.\n"
          f"I packed my lantern, sleeping bag, and {noun}. I am so {feeling} to {verb} in a tent.\n"
          f"I am {feeling2} we might see {article} {animal}, I hear they’re kind of dangerous.\n"
          f"While we’re camping, we are going to hike, fish, and {verb2}.\n"
          f"I have heard that the {color} lake is great for {verb_ing}.\n"
          f"Then we will {adverb} hike through the forest for {number} {time_used}.\n"
          f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet!\n"
          f"At night we will tell {number2} {sillyword} {choose_word_story(number2)} and roast {noun2} around the campfire!\n"
          )


def story_3():
    propername = enter_name()
    adjective = enter_adjective()
    article = choose_article(adjective)
    color = enter_color()
    animal = enter_animal()
    place = enter_place()
    adjective2 = enter_adjective()
    creature = enter_creature()
    creatures = form_plural(creature)
    adjective3 = enter_adjective()
    creature2 = enter_creature()
    creatures2 = form_plural(creature2)
    house_room = enter_room()
    thing = enter_noun()
    things = form_plural(thing)
    noun2 = enter_noun()
    noun3 = enter_noun()
    nouns3 = form_plural(noun3)
    adjective4 = enter_adjective()
    noun4 = enter_noun()
    nouns4 = form_plural(noun4)
    num = enter_number()
    time_input = enter_time()
    time_used = check_num(num, time_input)
    verb = enter_ing_verb()
    adjective5 = enter_adjective()
    article2 = choose_article(adjective5)
    noun5 = enter_noun()

    print(f"\n========================\n"
          f"HERE IS YOUR STORY!\n"
          f"========================\n"
          f"\nDear {propername}, I am writing to you from {article} {adjective} castle in an enchanted forest.\n"
          f"I found myself here one day after going for a ride on a {color} {animal} in {place}.\n"
          f"There are {adjective2} {creatures} and {adjective3} {creatures2} here!\n"
          f"In the {house_room} there is a pool full of {things}.\n"
          f"I fall asleep each night on a {noun2} of {nouns3} and dream of {adjective4} {nouns4}.\n"
          f"It feels as though I have lived here for {num} {time_used}.\n"
          f"I hope one day you can visit, although the only way to get here now is {verb} "
          f"on {article2} {adjective5} {noun5}!!"
          )
