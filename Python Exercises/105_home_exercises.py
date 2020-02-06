#Assignment for post class
# Learning outcome: [variables, print, different data types]
# ask and store the following in variables:
 # Name, last_name, age, age_of_mother, 3 skills
 # Print out the information in a formated manor
 # Calculate age difference between response and mother
 # Store skills in a list
 # Print each skill in a formated way.
# Definition of formated
 # a little context text
 # appropriate string formating like lower case or upper case, or other
# assignment to variable
print("What is your name?")
first_name = input().strip().capitalize()
print("what is your last name")
last_name = input().strip().capitalize()
print("what is your age in years")
age = int(input().strip())
print("What is your mother's age?")
age2 = int(input().strip())
print("what skills do you have?, name 3")
skills = [input().strip().capitalize()]

print("Hello", first_name, last_name, "!", "your age is",  age, "your mother's age is", age2,
      "And you are", "you and your mum have a difference of", f"{age2-age}", "and your main skills are", skills)

# Assignment2 for post class
#
# define an empty dictionary# name_dict = {}
# Prompt user for input for a story.
# it should have:
    # hero, beggiging, middle, end
    # 2 other things you define to be part of the story.
    # add each response to the dictionary under an appropriate key
# Print out a the dictionary information in an ordered way so we can read the story.

story_dictionary = {}

print("Who is the hero of the story?")
hero_key = input().strip().capitalize()
print("Who is the villain in the story?")
villain_key = input().strip().capitalize()
print("What is the beginning of the story?")
beginning_key = input().strip().capitalize()
print("What is the middle of the story?")
middle_key = input().strip().capitalize()
print("What is the end of the story?")
end_key = input().strip().capitalize()
print("What type of ending is the story?")
type_of_ending = input().strip().capitalize()

story_dictionary = {hero_key, villain_key, beginning_key, middle_key, end_key, type_of_ending}
print(story_dictionary)

print("The hero of the story is", hero_key, "and the villain is", villain_key, ", The story begins with", beginning_key,
      "And then", middle_key, "Finally,", end_key, "The ending was very", type_of_ending);





