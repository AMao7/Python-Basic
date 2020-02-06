# The game Fizz AND Buzz!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are FizzBuzz
# as a user I should be ask for a number,
# so that I can play the game with my input
# As a player, I should see the game counting up to my number and
# substituting the multiples of 3 and 5 with the appropriate values,
# So that I can see if it is working
import time
while True:

    num = int(input("give a numnber to count up to, enter 000 to end the game"))
    count_num = 1
    if num == 000:
        break

    while num > count_num:

        if count_num % 15 == 0:
            print("fizzbuzz")
            time.sleep()


        elif count_num % 3 == 0:
            print("fizz")

        elif count_num % 5 == 0:
            print("buzz")

        else:
            print(count_num)
        count_num += 1






# Make a weather/clothing game ## project
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'
# Make it so you keep playing until we say: 'No more Magic'

# s#unny = input("What is the weather like today sir!")
# if input()
