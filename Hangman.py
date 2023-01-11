#hangman - guess a letter
#if correct if will be listed (in a list?)
#if not correct, will be marked as wrong
#six chances, if wrong will be told as such,(if elif else?)
#how do I get the word list to guess from? (ask player to pick a subject and have a list of words ready) x
#enter different word list and can maybe pick at random (import random function) x
#how to represent the hanging man..just list parts of body struck and turns left?




print('Hello, and welcome to my Hangman game')
print('There are 6 subjects to choose from: flowers, gems, states, colors, apps, and countries.')
import random
og_input = str(input ("Please enter a subject to begin : "))
countries = ["germany", "jamaica", "canada", "america", "japan"]
flowers = ["rose", "daisy", "sunflower", "tulip", "lily"]
gems = ["diamond", "emerald", "pearl", "ruby", "opal"]
states = ["arizona", "california", "montana", "nevada", "hawaii"]
colors = ["green", "blue", "yellow", "pink", "black"]
apps = ["tiktok", "facebook", "instagram", "twitter", "linkedIn"]

categories = ['countries', 'flowers', 'gems', 'states', 'colors', 'apps']



first_pick = random.choice(countries)
second_pick = random.choice(flowers)
third_pick = random.choice(gems)
fourth_pick = random.choice(states)
fifth_pick = random.choice(colors)
sixth_pick = random.choice(apps)
def hangman():
    
        
  
    while og_input == 'countries':
        countries_copy = og_input
        countries_choice  = first_pick
        empty_countries = []
        pick_copy = countries_choice
        countries_list = str(list(pick_copy))
        

        

        letter = str(input('Please enter a letter: '))
        new_temp = letter
        while new_temp in countries_list:
            print('correct!')                                       
            countries_word_updated = countries_list.replace(' ', new_temp)
            empty_countries.append(countries_word_updated)
            print(empty_countries)
            updated = input('Please enter your next letter: ')
            temp = updated
            else temp in countries_list:
                print('correct!')
                countries_word_updated = countries_list.replace(' ', temp)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                updated = input('Please enter your next letter: ')
                temp2 = updated
                else temp2 in countries_list:
                    print('correct!')
                    countries_word_updated = countries_list.replace(' ', temp2)
                    empty_countries.append(countries_word_updated)
                    print(empty_countries)
                    updated = input('Please enter your next letter: ')
                    temp3 = updated
                    else temp3 in countries_list:
                        print('correct!')
                        countries_word_updated = countries_list.replace(' ', temp3)
                        empty_countries.append(countries_word_updated)
                        print(empty_countries)
                        updated = input('Please enter your next letter: ')
                        temp4 = updated
                        else temp4 in countries_list:
                            print('correct!')
                            countries_word_updated = countries_list.replace(' ', temp4)
                            empty_countries.append(countries_word_updated)
                            print(empty_countries)
                            updated = input('Please enter your next letter: ')
                            temp5 = updated
                            else temp5 in countries_list:
                                print('correct!')             
                                countries_word_updated = countries_list.replace(' ', temp5)
                                empty_countries.append(countries_word_updated)
                                print(empty_countries)
                                updated = input('Please enter your next letter: ') 
                                temp6 = updated
                                else temp6 in countries_list:    
                                    print('correct!')
                                    countries_word_updated = countries_list.replace(' ', temp6)
                                    empty_countries.append(countries_word_updated)
                                    print(empty_countries)
                                    break                           
                                print('Sorry, you are out of guesses!')
                                
                            print('Sorry, wrong guess! The left leg has been drawn! You have 1 attempts remaining')                            
                            
                        print('Sorry, wrong guess! The right leg has been drawn! You have 1 attempts remaining')                                           
                        
                    print('Sorry, wrong guess! The left arm has been drawn! You have 4 attempts remaining')
                print('Sorry, wrong guess! The right arm has been drawn! You have 1 attempts remaining')                                           
                
            print('Sorry, wrong guess! The body has been drawn! You have 4 attempts remaining')
            
            
        print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
        
        
            
        return countries_choice
hangman()


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

#1/9 - 02:21 - set up to print category
#work on - guess letter, in if loop? if letter matches with one in chosen word, add to a new empty list
#list - need a way to match letters with word returned, 
#need to make word returned into new list to match letters to new word

#1/9 - 22:10 - "raw_input was called, but this frontend does not support input requests." - on Jupyter
#working for first input, need a different loop

# 1/10 - 21:05 - else temp in countries_list:SyntaxError: invalid syntax
# using else wrong or wrong variables
	














