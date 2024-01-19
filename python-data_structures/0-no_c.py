

#function that removes all characters c and C from a string.
def no_c(my_string):

    for char in my_string:
        if char == "c" or char == "C":
            my_string.replace(char, "")
    return my_string

