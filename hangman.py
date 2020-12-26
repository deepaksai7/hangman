
import random
from words import words
c=7
print(f"""

************************************************************
*              H A N G M A N                               *
*                                                          *
*              Only {c} errors are allowed                   *
************************************************************

""")

def get_valid_word():
    word=random.choice(words)
    while " " in word or "-" in word:
        word=random.choice(words)
    return word

def substitute(arr,letter,word):
    for i,l in enumerate(word):
        if l==letter:
            arr[i]=letter
    return arr

def display_current_status(arr):
    for i in arr:
        print(i+" ",end=" ")
    print()

def listIsNotFull(current_status):
    for i in current_status:
        if i=="_":
            return True
    return False

def run(c):
    word=get_valid_word().upper()
    current_status=["_" for i in range(0,len(word))]
    
    while c>=1 and listIsNotFull(current_status):
        print(f"{c} errors are available")
        display_current_status(current_status)
        letter=input("Enter the letter: ").upper()
        if letter in word:
            current_status=substitute(current_status,letter,word)
            
        else:
            c-=1
    if c<1:
        print(f"oops, the chances are over. The word was {word}")
    else:
        display_current_status(current_status)
        print(f"congratulations!! you have completed the word {word}")

choice=input("Want to start? Enter Y for Yes and N to cancel.  ").upper()
if choice=="Y":
    run(c)
elif choice=="N":
    pass
else:
    print("incorrect choice")




