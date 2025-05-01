# tutorial-2.py


# VARIABLES
# Can't start with a number or be compiled of only numbers

# This is not a list, but a tuple
# Tuples are immutable (cannot change)
# A list is mutable 
programming_languages = "Python", "Java", "C++", "C#"
print(type(programming_languages))

# Same as above
programming_languages_1 = ("Python", "Java", "C++", "C#")

# FOR LOOP
for language in programming_languages:
    # A tab is always 4 spaces (most of the world uses 4, Google uses 2)
    print(language)