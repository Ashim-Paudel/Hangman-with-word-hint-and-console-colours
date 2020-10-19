#importing all the functions that i created on another file
from os import *
import time
import random
from words import *
from fonts import *
from all_functions import *

system("cls")

# i made a python module containing all the required functions,  all_functions for
#module fonts is for some interesting font effects
#module words is for collection of words that are to be displayed randomly

#appending all the functions to a game

#intro field
time.sleep(2)
hangman()
time.sleep(0.2)
by()
time.sleep(0.2)
ashim()
time.sleep(2.9)
system("cls")

#rules for game
print()
print(colortext("[[bright_magenta]]"+"\t\t\t"+'~'*70))
print(colortext("[[reset]]\t\t\t    Do you want to look the rules and instructions ? (y/n)"))
print(colortext("[[bright_magenta]]\t\t\t"+'~'*70+'[[reset]]'))
ask=input()
response=ask[0].upper()
while response!='Y' and response!="N":
    print(colortext('[[red]]\t\t\t\t '+"Sorrry! '{}' was an invalid input.[[yellow]] Say (y/n)[[reset]]").format(ask))
    ask=input()
    response=ask[0].upper()
if response=='Y':
    game_rules()
    lets()
    time.sleep(0.12)
    play()
    time.sleep(1.5)
else:
    lets()
    time.sleep(0.12)
    play()
    time.sleep(1.5)
   
 
#creating a variable to make program active
program_active= True

#looping through whole program
while program_active: 
    system("cls")
    main_game()   #running the main game created as function

    #restart dialogue.
    print()
    print(colortext("[[bright_magenta]]"+"\t\t\t"+'~'*70))
    print(colortext("[[reset]]\t\t\t    Do you want to play again ? (y/n)"))
    print(colortext("[[bright_magenta]]\t\t\t"+'~'*70+'[[reset]]'))
    ask=input()
    response=ask[0].upper()
    while response!='Y' and response!="N":
        print(colortext('[[red]]\t\t\t\t '+"Sorrry! '{}' was an invalid input.[[yellow]] Say (y/n)[[reset]]").format(ask))
        ask=input()
        response=ask[0].upper()
    if response=='N':
        program_active=False
        system("cls")
        thankyou()
    else:
        system("cls")
        lets()
        time.sleep(0.12)
        play()
        time.sleep(0.12)
        again()
        time.sleep(1.6)
print()
print()        
print(colortext("press enter to exit."))
input()