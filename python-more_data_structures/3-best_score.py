

#Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    value = a_dictionary.values()
    score = 0
    for val in value:
        if score < val:
            score = val
    key = ""
    for item in a_dictionary.keys():
        if a_dictionary[item] == score:
            key = a_dictionary[item]
    return key



