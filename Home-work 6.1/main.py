import string

def get_letters_range(input_str):
    start, end = input_str.split('-')
    all_letters = string.ascii_letters
    start_index = all_letters.index(start)
    end_index = all_letters.index(end) + 1  
    return all_letters[start_index:end_index]


print(get_letters_range("a-c"))  # abc
print(get_letters_range("a-a"))  # a
print(get_letters_range("s-H"))  # stuvwxyzABCDEFGH
print(get_letters_range("a-A"))  # abcdefghijklmnopqrstuvwxyzA
