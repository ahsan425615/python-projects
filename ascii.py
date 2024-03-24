# def is_ascii(character):
#     ascii_value = ord(character)
#     return 0 <= ascii_value <= 127

# # Test the function
# test_char = 'a'
# if is_ascii(test_char):
#     print(f"'{test_char}' is an ASCII character.")
# else:
#     print(f"'{test_char}' is not an ASCII character.")


# ///////////////////////////////////////////////////////////////

# def is_lowercase_letter(character):
#     ascii_value = ord(character)
#     return 97 <= ascii_value <= 122

# # Test the function
# test_char = 'a'
# if is_lowercase_letter(test_char):
#     print(f"'{test_char}' is a lowercase letter.")
# else:
#     print(f"'{test_char}' is not a lowercase letter.")


# ////////////////////////////////////////////////////////////////////////////////////////////////

def word_to_ascii(word):
    ascii_values = []
    for char in word:
        ascii_values.append(ord(char))
    return ascii_values

# Test the function
input_word = input("Enter a word: ")
ascii_representation = word_to_ascii(input_word)
print("ASCII representation of the word:", ascii_representation)



