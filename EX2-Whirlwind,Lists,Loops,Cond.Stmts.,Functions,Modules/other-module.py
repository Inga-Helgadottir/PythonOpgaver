# Create a small program with 2 modules. First module contains a list of names. 
# Second module has a function that can take a list of names and print each name with the word "hello" in front. 
# Let the second module import the first module and use the list of names from it. 
# Run the second module from a notebook cell.
# module1 and module2

import module
def printing_names(people):
    for i in people:
        print("Hello " + i)

printing_names(module.members)

