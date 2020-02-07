# The game Fizz AND Buzz!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are FizzBuzz
# as a user I should be ask for a number,
# so that I can play the game with my input
# As a player, I should see the game counting up to my number and
# substituting the multiples of 3 and 5 with the appropriate values,
# So that I can see if it is working
# import time
# while True:
#
#     num = int(input("give a numnber to count up to, enter 000 to end the game"))
#     count_num = 1
#     if num == 000:
#         break
#
#     while num >= count_num:
#
#         if count_num % 15 == 0:
#             print("fizzbuzz")
#             time.sleep()
#
#         elif count_num % 3 == 0:
#             print("fizz")
#
#         elif count_num % 5 == 0:
#             print("buzz")
#
#         else:
#             print(count_num)
#         count_num += 1


# def fizz(x):
#     if x % 5 == 0:
#         return "fizz"
#
#
# def buzz(x):
#     if x % 3 == 0:
#         return "buzz"
#
#
# def fizz_buzz(x):
#     if x % 15 == 0:
#         return "fizzbuzz"
#
#
# print(buzz(6))
while True:
    question = input("what is your question sir")
    print("questions are wise, but for now. Wax on, and Wax off!")


    if question != "sensei":
        print("You are smart, but not wise, address me as sensei please")

    elif question == "sensei im at peace":
        print('Sometimes, what heart know, head forget')

    elif question == "block" or "blocking:":
            print("Rememeber, best block, not to be there")

    else:
           print("do not lose focus. Wax on. Wax off.")


