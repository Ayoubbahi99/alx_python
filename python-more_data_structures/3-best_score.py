

#Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if a_dictionary:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
    else:
        return None




