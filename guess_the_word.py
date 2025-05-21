import random

word = "valentine"
seed = 1

def turn_the_word(seed=None):
    if seed is not None:
        random.seed(seed)

    result = ['_' for i in enumerate(word)]
    return result

def reveal_letter(current_state, seed=None):
    unrevealed_letters = [i for i, char in enumerate(current_state) if char == '_']
    if not unrevealed_letters:
        return current_state  

    if seed is not None:
        random.seed(seed)

    reveal_letter_index = random.choice(unrevealed_letters) 

    current_state[reveal_letter_index] = word[reveal_letter_index]
    return current_state

result = turn_the_word(seed)
current_state = result[:]



name = input("Please input your name: ")
print(f"Hello {name}! Try to guess a todays word!")

while True:
    should_we_start = input("Do you wanna start? y/n: ").lower()
    if should_we_start == "y":
        print("Okay! Lets start!")
        break
    elif should_we_start == "n":
        print("It's okay. See you later!")
        break
    else:
        print("Please enter the valid command")


tries = 0
while True:
    guess = input(f"Word is {current_state}. Print your guess: ").lower()
    if guess != word:
        tries += 1
        print(f"You are wrong! Try again! Tries count: {tries}")
        if tries % 3 == 0:
            while True:
                hint = input(f"You have used {tries} tries. Do you want a hint?(y/n): ").lower()
                if hint == "y":
                    current_state = reveal_letter(current_state)
                    print(f"You are given one letter.")
                    break
                elif hint == "n":
                    print("You are a stubborn one!")
                    break
                else:
                    print("Enter a valid response!")

    elif guess == word:
        print(f"Wow, you guessed it right! You have used {tries} tries. See you later {name}!")
        break

#make a func that will check if the letter is in the word and reveal it?