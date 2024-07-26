import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")
print(display)

user_guess=input("Guess a letter: ").lower()



for letter in chosen_word:
    if letter == user_guess:
        display.append(user_guess)
    else:
        print('incorrect')

print(display )


