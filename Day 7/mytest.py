import random
import hangman_arts
import hangman_words
from os import system


print(hangman_arts.logo)
print("Welcome to Hagman Game")


chosen_word= random.choice(hangman_words.word_list)
print(chosen_word)
display=[]
lives = 6
for i in chosen_word:
    display.append("_")

game_over = False
while not game_over :
    
    guess= input("Guess a letter: ")
    system("cls")
    print(hangman_arts.stages[lives])
    for l in range(len(chosen_word)):
        if guess == chosen_word[l]:
            display[l]=guess
            
    if guess not in chosen_word:
        lives-=1
        print(f"Wrong! You have {lives} now")
        print(hangman_arts.stages[lives])
    print(display)
    if lives ==0 :
        game_over= True
        print("You lose !")
    if "_" not in display:
        print("You won")
        game_over= True
    
