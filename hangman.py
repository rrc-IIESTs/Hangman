from hangman_words import word_list
import random

word = random.choice(word_list)
word_length = len(word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)
print("Only alphabets allowed, any violation and you lose")
display = []
for _ in range(word_length):
    display+='_'

while not end_of_game:
    try:
        guess = input("Guess a letter: ").lower()
        if len(guess)>1 or not guess[0].islower():
            raise Exception()
        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(word_length):
            letter = word[position]
            if letter ==guess:
                display[position] = letter
        
        if guess not in word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            lives-=1
            if lives==0:
                end_of_game = True
                print("You've lost all lives, you lose")
        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win")
        from hangman_art import stages
        print(stages[lives])
    except:
        print("Please input a valid alphabet")
        print("You lost for not following instructions")
        print(stages[0])
        end_of_game = True

