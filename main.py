import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in range(len(chosen_word)):
    display +="_"
print(display)
  

end_game= False
word_length = len(chosen_word)
lives = 6


while not end_game:
    user_guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
    print(display)
    
    if user_guess not in chosen_word:
        lives-=1   
    print(f"You have {lives} lives remaining ")
    

    if "_" not in display:
        end_game = True
        print("You Win")
    elif lives == 0:
        end_game = True
        print("Ya Lose")
        



