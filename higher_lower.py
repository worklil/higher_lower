import random
from art import (logo, vs)
from game_data import data

person1 = random.choice(data)
data.remove(person1)
person2 = random.choice(data)


# def check_answer(guess, answer, point):
#     """ checks answer against guess. Returns the number of turns remaining. """
#     if guess == 'A' or guess == 'a':
#         guess = person1['follower_count']
#     elif guess == 'B' or guess == 'b':
#         guess = person2['follower_count']
#     else:
#         print("Invalid input.")


def game():
    print(logo)

    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
    print(vs)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
    if int(person1['follower_count']) > int(person2['follower_count']):
        answer = int(person1['follower_count'])
        answer1 = "A"
    else:
        answer = int(person2['follower_count'])
        answer1 = "B"
    print(f"This is the answer {answer1}")
    # check = 1
    # while check != 0:
    guess = input("Who has more followers? Type 'A' or 'B'\n")
    if guess == 'A' or guess == 'a':
        guess = person1['follower_count']
    elif guess == 'B' or guess == 'b':
        guess = person2['follower_count']
    else:
        print("Invalid input.")
    print(f"real answer {answer}, your guess {guess}")
game()



        # if point == 0:
        #     print("You've run out of guesses, you lose.")
        #     return
        # elif point != answer:
        #     print("Guess again.")


