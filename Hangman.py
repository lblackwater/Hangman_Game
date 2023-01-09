#hangman - guess a letter
#if correct if will be listed (in a list?)
#if not correct, will be marked as wrong
#six chances, if wrong will be told as such,(if elif else?)
#how do I get the word list to guess from? (ask player to pick a subject and have a list of words ready)
#enter different word list and can maybe pick at random (import random function)
#how to represent the hanging man..just list parts of body struck and turns left?




print('Hello, and welcome to my Hangman game')
print('There are 6 subjects to choose from: flowers, gems, states, colors, apps, and countries.')
import random
og_input = str(input ("Please enter a subject to begin : "))
countries = ["Germany", "Jamaica", "Canada", "America", "Japan"]
flowers = ["Rose", "Daisy", "Sunflower", "Tulip", "Lily"]
gems = ["Diamond", "Emerald", "Pearl", "Ruby", "Opal"]
states = ["Arizona", "California", "Montana", "Nevada", "Hawaii"]
colors = ["Green", "Blue", "Yellow", "Pink", "Black"]
apps = ["Tik Tok", "Facebook", "Instagram", "Twitter", "LinkedIn"]

categories = ['countries', 'flowers', 'gems', 'states', 'colors', 'apps']



first_pick = random.choice(countries)
second_pick = random.choice(flowers)
third_pick = random.choice(gems)
fourth_pick = random.choice(states)
fifth_pick = random.choice(colors)
sixth_pick = random.choice(apps)
def hangman():
    if og_input == 'countries':
        countries_choice  = first_pick
        return countries_choice
    elif og_input == 'flowers':
        flowers_choice = second_pick
        return flowers_choice
    elif og_input == 'gems':
        gems_choice = third_pick
        return gems_choice
    elif og_input == 'states':
        states_choice = fourth_pick
        return states_choice
    elif og_input == 'colors':
        colors_choice = fifth_pick
        return colors_choice
    elif og_input == 'apps':
        apps_choice = sixth_pick
        return apps_choice
    else:
        print('Please select from the choices listed!')
hangman()
    


#1/8 - 17:00 - printing every category 

#work on - print one category, correct one, 
	














