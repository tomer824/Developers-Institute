#write a function that gives the number of words
#write a function that takes a letter, and counts the 
# occurrances of that letter

text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
isi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit sse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt n culpa qui officia deserunt mollit anim id est laborum."""


# def count_words(text):
#     words = 0
#     for char in text:
#         if char == " ":
#             words += 1
#     return words

# word_count = count_words(text)
# print(f"There are {word_count} words in the text.")




def count_letters(text, letter_choice):
    letters = 0
    for letter in text:
        if letter == letter_choice:
            letters += 1
    return letters