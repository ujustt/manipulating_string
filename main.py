
def count_occurrences(my_string, my_word):
    """
    Takes a string and word and returns the number of instances that word occurs.
    """    
    # Converts string and word to uppercase so matching is not case-sensitive
    my_string = my_string.upper()
    my_word = my_word.upper()
    return my_string.count(my_word)


if __name__ == "__main__":
    # Request Excerpt from user
    print("Please enter an excerpt: ")
    my_string = ""
    user_input = input()
    # Request input until empty line entered to handle multiple lines.
    while user_input:
        my_string += user_input
        user_input = input()

    # Request word from user
    print("Please enter a word")
    my_word = input()
    
    # Count the number of occurrences
    result = count_occurrences(my_string, my_word)

    print("The word {} occurs {} times".format(my_word, result))