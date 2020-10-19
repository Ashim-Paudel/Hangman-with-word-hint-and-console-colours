from os import *
import time
import random
from words import dict1
from fonts import *



COLORS={                     #created a dictionary for colors
"reset": "\u001b[0m",
"black":"\u001b[30m",
"red":"\u001b[31m",
"green":"\u001b[32m",
"yellow":"\u001b[33m",
"blue":"\u001b[34m",
"magenta":"\u001b[35m",
"cyan":"\u001b[36m",
"white":"\u001b[37m",
"bright_green":"\u001b[32;1m",
"bright_yellow":"\u001b[33;1m",
"bright_blue":"\u001b[34;1m",
"bright_black":" \u001b[30;1m",
"bright_red":"\u001b[31;1m",
"bright_magenta": "\u001b[35;1m",
"bright_cyan":"\u001b[36;1m",
"bright_white": "\u001b[37;1m"
}

#functio to return color by replacing colour name
def colortext(text):
    for color in COLORS:
        text=text.replace("[["+color+"]]",COLORS[color])
    return text   
    
#functions to print man    
def man0():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |             
        |             
        |           
        |           
        |             
        |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    
def man1():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             
    [[bright_green]]    |[[yellow]]             
    [[bright_green]]    |[[yellow]]            
    [[bright_green]]    |[[yellow]]          
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    
def man2():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]             
    [[bright_green]]    |[[yellow]]             
    [[bright_green]]    |[[yellow]]           
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    
    
def man3():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]            /  
    [[bright_green]]    |[[yellow]]             
    [[bright_green]]    |[[yellow]]           
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()  
    
def man4():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]            / \ 
    [[bright_green]]    |[[yellow]]             
    [[bright_green]]    |[[yellow]]           
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    
def man5():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]            /|\ 
    [[bright_green]]    |[[yellow]]             |
    [[bright_green]]    |[[yellow]]           
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    
def man6():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]            /|\ 
    [[bright_green]]    |[[yellow]]             |
    [[bright_green]]    |[[yellow]]           _/ 
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    
    
def man7():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]            /|\ 
    [[bright_green]]    |[[yellow]]             |
    [[bright_green]]    |[[yellow]]           _/ \_
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
def man_sample():
    print()
    print()
    print(colortext('''
    [[bright_green]]
        ---------------
        |[[red]]             |
    [[bright_green]]    |[[yellow]]             O
    [[bright_green]]    |[[yellow]]           _/|\_
    [[bright_green]]    |[[yellow]]             |
    [[bright_green]]    |[[yellow]]           _/ \_
    [[bright_green]]    |
    [[bright_red]]_________
    ---------
    [[reset]]
    '''))
    print()
    print()
    

#This is final function for printing man:

def print_man(error_list):
    if len(error_list)==0:
        man0()
    elif len(error_list)==1:
        man1()
    elif len(error_list)==2:
        man2()
    elif len(error_list)==3:
        man3()
    elif len(error_list)==4:
        man4()
    elif len(error_list)==5:
        man5()
    elif len(error_list)==6:
        man6()
    elif len(error_list)==7:
        man7()
       


#function to replace underscore by guessed letter or word:
def display(word, guessed):
    word =' '.join([ch if ch in guessed else '_' for ch in word])
    return word       


        
#i 've created the whole game in a function
def main_game():
    already_guessed=[]                 #keep in track of already guessed letters by creating a list
    error_attempts=[]                  #storing error entries
    hint_list=[]                       #just to enter hint 
    man_num=error_attempts+hint_list   #for counting error attempts
    
    
    random_items=random.choice([item for item in dict1.items()])
    random_word=random.choice(random_items[1]).upper().replace(' ','')
    word_hint=random_items[0]   #creating a random choice/selection of words from a list of some sample words
    time.sleep(0.15)
    
    
    while len(man_num)!=7:  #looping the game
        print(colortext(''+'~'*110+''))
        print()
        print(colortext("[[green]]\t\t\t\t Guess the word:- [[reset]]  "), display(random_word,set(already_guessed)))
        
        #check if hint already accessed!
        if len(hint_list)!=0: 
            print(colortext("\n\t\t\t\t [[cyan]]WORD HINT: [[yellow]]{}[[reset]]").format(word_hint))
            
        else:
            pass
        
        #Displaying total guess and incorrect guesses till now:
        if len(set(already_guessed))+len(set(error_attempts))==0:
            print("\n  no guesses till now")
        else:
            print(' ',len(set(already_guessed))+len(set(error_attempts))," distinct guesses till now")
            
        #displaying set of incorrect entries:
        if len(set(error_attempts))==0:
            print(colortext("  incorrect entries :[[red]]none[[reset]] "))
        else:
            print(colortext("  incorrect entries :[[red]]{}[[reset]] ").format(set(error_attempts)))
            
        print_man(man_num)
        user_guess=input("\t\t\t\t Please input your guess (the word/letter) :-   ").upper()
        print()
            
        if user_guess==random_word:
            system("cls")
            print('~'*110)
            print()
            print_man(man_num)
            print(colortext('\t\t\t\t\t\t[[yellow]]  CONGRATULATIONS !!![[reset]] '))
            print(colortext("\t\t\t\t\t\t[[red]] ====================[[reset]]"))
            print()
            time.sleep(0.1)
            print(colortext("\t\t\t\t Yay!!!  you've guessed the word:[[magenta]] ''{}''[[reset]]correctly".format(random_word)))
            time.sleep(0.1)
            print(colortext("[[yellow]]\n\t\t\t\t\t\t*** YOU WON ***[[reset]]"))
            print()
            print('~'*110)
            print()
            break
            
        elif user_guess[:4]=='HINT':
            if len(hint_list)==1:
                time.sleep(0.1)
                print(colortext("[[yellow]]\t\t\t\t You have already accessed hint"))
                time.sleep(0.1)
                print(colortext("\t\t\t\t The word hint is : [[magenta]]{}[[reset]]" ).format(word_hint))
                time.sleep(1.5)
                system("cls")
            else:
                print()
                print(colortext("\t\t\t[[red]] Your have requested hint."))
                print(colortext("[[red]]\t\t\t Your chance will be reduced by 1.[[reset]]"))
                hint_list.append(user_guess)
                man_num=error_attempts+hint_list
                print_man(man_num)
                print('\t\t\t ---SEARCHING FOR WORD HINT .... ---')
                time.sleep(1)
                print('\t\t\t ---Fetching hint from database..... ---')
                time.sleep(3)
                print()
                print(colortext('\t\t\t'+'[[yellow]]HINT: [[reset]]'),word_hint)
                time.sleep(1)
                system("cls")
           
            
        elif user_guess[0] in already_guessed:
            print(colortext("[[bright_cyan]]\t\t\t\t\t***   ALREADY GUESSED CORRECTLY!!! ***[[reset]]"))
            print("\t\t\t\t You have already guessed  '{}'".format(user_guess[0]))
            print(colortext("\t\t\t\t The letters you've correctly guessed till now are:[[bright_cyan]]  {}[[reset]]").format(set(already_guessed)))
            time.sleep(2.5)
            system("cls")
            
            if set(already_guessed)==set(random_word):
                print()
                system("cls")
                print('~'*110)
                print_man(man_num)
                print(colortext('\t\t\t\t[[yellow]]  CONGRATULATIONS !!![[reset]] '))
                time.sleep(0.100)
                print()
                print("\t\t\t\t Yay!!! you've successfully guessed the correct word.")
                time.sleep(0.100)
                print(colortext("\t\t\t\t The word is:[[magenta]]  {}[[reset]]").format(random_word))
                time.sleep(0.100)
                print(colortext("[[yellow]]\t\t\t\t YOU WON [[reset]]"))
                print()
                print('~'*110)
                print()
                break
            else:
                continue
                
        elif user_guess[0] in random_word:
            already_guessed.append(user_guess[0])
            man_num=error_attempts+hint_list
            print()
            print(colortext("[[yellow]]\t\t\t\t AWESOME GUESS!!![[reset]]"))
            print("\t\t\t\t '{}'  is in that word    ".format(user_guess[0]))
            print("\t\t\t\t You are doing good!!!")
            print()
            print('\t\t\t\t ', display(random_word,set(already_guessed)))
            print()
            time.sleep(1)
            system("cls")
            
            if set(already_guessed)==set(random_word):
                system("cls")
                print()
                print('~'*110)
                print_man(man_num)
                print(colortext('\t\t\t\t[[yellow]]  CONGRATULATIONS !!![[reset]] '))
                time.sleep(0.100)
                print()
                print("\t\t\t\t Yay!!! you've successfully guessed the correct word.")
                time.sleep(0.100)
                print(colortext("\t\t\t\t The word is:[[magenta]]  {}[[reset]]").format(random_word))
                time.sleep(0.100)
                print(colortext("[[yellow]]\t\t\t\t YOU WON [[reset]]"))
                time.sleep(0.100)
                print('~'*110)
                print()
                break
            else:
                continue
                
        elif user_guess[0] in error_attempts:
            print(colortext('[[red]]\t\t\t\t*** ALREADY GUESSED INCORRECTLY ***[[reset]]'))
            print('\t\t\t\t', "You've already guessed the letter:- ",user_guess[0])
            print(colortext("[[yellow]]\t\t\t\t '{}'[[bright_red]] is an incorrect guess[[reset]]").format(user_guess[0]))
            print(colortext('\t\t\t\t You have incorrectly entered: [[bright_red]]{}[[reset]] ,till now').format(set(error_attempts)))
            time.sleep(2.5)
            system("cls")
        elif user_guess[0] not in random_word:
            error_attempts.append(user_guess[0])
            man_num=error_attempts+hint_list
            print()
            print('-'*100)
            print(colortext("[[red]]\t\t\t\t Sorry the letter [[yellow]]'{}'[[red]], you guessed is incorrect. \t\t\t\t   [[reset]]").format(user_guess[0]))
            print('-'*100)
            print()
            display(random_word,set(already_guessed))
            print()
            time.sleep(1)
            system("cls")
            
        
        
    if len(man_num)==7:   #run out of attempts
        print('~'*110)
        print()
        print_man(man_num)
        time.sleep(0.1)
        print(colortext('[[red]]\t\t\t\t *** OUT OF ATTEMPTS ***[[reset]]'))
        print(colortext("[[blue]]\t\t\t\t   ===================[[reset]]"))
        print()
        time.sleep(0.1)
        print(colortext("\t\t\t\t Sorry!!! you ran out of attempts[[reset]]\t\t\t\t\t\t\t  "))
        print("\t\t\t\t Better luck next time!!! ")
        print(colortext("\t\t\t\t The correct word was:  [[yellow]]'{}'[[reset]]\t\t\t\t\t\t\t  ").format(random_word))
        print()
        print()
        print('~'*110)
        print()
        print()
 
 
 
 
 #this are functions for game intro
 
def intro():
    print()
    print()
    print()
    print(colortext("[[bright_blue]]\t\t\t|||"+'~'*65+"|||[[reset]]"))
    time.sleep(0.1)
    print("\t\t\t\t\t      ***WELCOME TO -HANG MAN ***")
    time.sleep(0.09)
    print("\t\t\t\t          ****Developed by- ASHIM PAUDEL****")
    time.sleep(0.9)
    print("\t\t\t\t                  *version 4.0*")
    time.sleep(0.3)
    print(colortext("[[bright_blue]]\t\t\t|||"+'~'*65+"|||[[reset]]"))
    print()
    print()
    print()
    
    
#this function is for game rules
def game_rules():
    print()
    print()
    print()
    print(colortext("[[bright_blue]]\t\t|||"+"~"*95+"|||"))
    print(colortext("[[bright_green]]\t\t"+"\t\t\t\t   **Game instructions**"))
    print(colortext("[[bright_magenta]]"+"\t\t"+"\t\t\t\t     =================[[reset]]"))
    time.sleep(1)
    print("\t\t1.You can guess either :the whole word or any letter. ")
    time.sleep(0.1)
    print("\t\t2.For each wrong attempts ,the program will create a hanging man.")
    time.sleep(0.1)
    print("\t\t3.In total you will have only-7 attempts.")
    time.sleep(0.1)
    print("\t\t4.If you guessed the whole word correctly, whole word will be accepted as your input and you win.")
    time.sleep(0.1)
    print("\t\t5.Else, only first letter of your guess will be accepted and run accordingly.")
    time.sleep(0.1)
    print("\t\t6.The number of characters in probable in word will be equal to no of underscores ' _ '.")
    time.sleep(0.1)
    print("\t\t7. For hint about the word, type ' hint '  . But accessing hint will reduce your attempt too.")
    time.sleep(0.1)
    print(colortext("[[bright_blue]]\t\t|||"+''+"~"*95+"|||[[reset]]"))
    print()
    print()
    print()
    print(colortext("[[red]]\t\t\t Use full screen for better visual effects.[[reset]]\n\n"))
    print("Press enter to continue.")
    input()
    system('cls')
