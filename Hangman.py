#hangman - guess a letter
#if correct if will be listed (in a list?)
#if not correct, will be marked as wrong
#six chances, if wrong will be told as such,(if elif else?)
#how do I get the word list to guess from? (ask player to pick a subject and have a list of words ready)
#enter different word list and can maybe pick at random (import random function)
#how to represent the hanging man..just list parts of body struck and turns left?




print('Hello, and welcome to my Hangman game')
print('There are 6 subjects to choose from: flowers, gems, states, colors, apps, and countries.')
categories = ['countries', 'flowers', 'gems', 'states', 'colors', 'apps']
og_input = input ("Please enter a subject to begin : ")


# take input and match to list of categories






#randomly assigns a word based on category chosen



def hangman():
    for first_pick in categories:
        for second_pick in first_pick:
            if "countries" in categories:
                countries = ["Germany", "Jamaica", "Canada", "America", "Japan"]
            import random
            countries_choice = random.choice(countries)
            
            print(countries_choice)
            if 'flowers' in categories:
                flowers = ["Rose", "Daisy", "Sunflower", "Tulip", "Lily"]
            import random
            flowers_choice = random.choice(flowers)
            
            print(flowers_choice)
            if 'gems' in categories:
                gems = ["Diamond", "Emerald", "Pearl", "Ruby", "Opal"]
            import random
            gems_choice = random.choice(gems)
            
            print(gems_choice)
            if 'states' in categories:
                states = ["Arizona", "California", "Montana", "Nevada", "Hawaii"]
            import random
            states_choice = random.choice(states)
            
            print(states_choice)
            if 'colors' in categories:
                colors = ["Green", "Blue", "Yellow", "Pink", "Black"]
            import random
            colors_choice = random.choice(colors)
            
            print(colors_choice)
            if 'apps' in categories:
                apps = ["Tik Tok", "Facebook", "Instagram", "Twitter", "LinkedIn"]
            import random
            apps_choice = random.choice(apps)
            
            print(apps_choice)
        else:
            print('Please select from the choices listed!')

hangman()


#1/8 - 17:00 - printing every category 

#work on - print one category, correct one, 
	














