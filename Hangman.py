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
    
        
  
    if og_input == 'countries':
        countries_copy = og_input
        countries_choice  = first_pick
        new_countries = list(countries_copy)
        empty_countries = []
        countries_word = countries_choice
        letter = str(input('Please enter a letter: '))

        
        while letter in countries_word:
            
            in_word = letter
            updated = input('Please enter your next letter: ')
            also_in_word = updated
            if in_word == letter:
                print('correct!')
                countries_word_updated = countries_word.replace(' ', also_in_word)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
            #return(countries_word)
                continue
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining') 
                
            
               
        while updated in countries_word:  
                                                          
            temp = updated
            new = input('Please enter your next letter: ')
            temp1 = new 
            if new == updated:
                print('correct!')
                countries_word_updated = countries_word.replace(' ', temp1)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                print('Sorry, wrong guess! The body has been drawn! You have 4 attempts remaining')
                #return(countries_word)
                continue
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining') 
            
                
        
        while updated in countries_word:
                                        
            temp2 = updated
            new2 = input('Please enter your next letter: ')
            also_in_word = new2
            if new2 == updated:
                print('correct!')
                countries_word_updated = empty_countries.replace(' ', also_in_word)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                print('Sorry, wrong guess! The left arm has been drawn! You have 3 attempts remaining')    
                    #return(countries_word)
                continue
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
                
        while updated in countries_word:
             
            temp3 = updated
            new3 = input('Please enter your next letter: ')
            also_in_word2 = new 
            if new3 == updated:
                print('correct!')
                countries_word_updated = empty_countries.replace(' ', also_in_word2)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                print('Sorry, wrong guess! The right arm has been drawn! You have 2 attempts remaining')
                continue
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
                        
        while updated in countries_word:
            
            temp4 = updated
            new4 = input('Please enter your next letter: ')
            also_in_word3 = new 
            if new4 == updated:
                print('correct!')
                countries_word_updated = empty_countries.replace(' ', also_in_word3)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                print('Sorry, wrong guess! The right leg has been drawn! You have 1 attempts remaining')
                continue
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
                           
        while updated in countries_word:
            
            temp5 = updated
            new5 = input('Please enter your next letter: ')
            also_in_word4 = new 
            if new5 == updated:
                print('correct!')
                countries_word_updated = empty_countries.replace(' ', also_in_word4)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                print('Sorry, wrong guess! The left leg has been drawn! You have 1 attempts remaining')
                continue
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
               
        while updated in countries_word:
            
            temp6 = updated
            new6 = input('Please enter your next letter: ')
            also_in_word5 = new 
            if new6 == updated:
                print('correct!')
                countries_word_updated = empty_countries.replace(' ', also_in_word5)
                empty_countries.append(countries_word_updated)
                print(empty_countries)
                print('Sorry, you are out of guesses!')
            else:
                print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
                
                                 
            break                            

                                        
                        
                           
                         
                       
                
            
            # while letter in countries_word
            #     print('Please choose another letter: ')
            #     while letter in countries_word:
            #         print('correct!')
            # print('Sorry, wrong guess!')
        


        #print('Sorry, wrong guess! The head has been drawn! You have 5 attempts remaining')
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
	














