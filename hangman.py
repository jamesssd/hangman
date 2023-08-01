import random
from hangman_words import word_list
from hangman_art import logo, stages


print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
live = 6
while not end_of_game:  
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'You have already used the letter {guess}, pick a different letter')
   
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(stages[live])

    if guess not in chosen_word:
        live -= 1
        print(stages[live])
        print(f'The letter you picked "{guess}", is not part of the word, you lose a life')
        if live == 0:
            end_of_game=True
            print("You lost!")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("Game is over, you won!")