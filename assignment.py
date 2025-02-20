# The is the Codewars project

# This is the Even or Odd function
def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"
#---------------------------------
# This is the Coverting Number to String
def number_to_string(num):
    return str(num)
#---------------------------------
# This is the Remove White Space function
def no_space(x):
    string = ""
    for character in x:
        if character != " ":
            string += character
    return string
#---------------------------------
# This is the Vowel Count function
def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
#---------------------------------