# control the flow of code using if statements (through assertions which returns true or false)

# if <condition>:
    # block of code - refers to consecutive line of code that are indented and will run together.
# elif <condition2>
    # block of code
# else:
    # block of code

weather = 'rainy'

if weather == 'rainy and stormy':
    print('take umbrella')
    print("I'm still in the block of code as well :D ")
elif weather == 'stormy':
    print("take raincoat")

elif ('stormy' in weather) and ('rainy' in weather):
    print("stay at home g")
else:
    print('take sunglasses')

#       print("I'm outside and will always run")

age = 19
driver_license = True

if age > 17 and driver_license == True:
    print("yay you can drive and drink")
elif age > 17:
    print("you can drive")
elif driver_license == True:
    print("you can drive")
elif age > 16:
    print("you can't legally drink but your mates might have your back")
else:
    print("You're too young go back to school")
