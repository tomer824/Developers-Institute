import random

def get_words_from_file():
    my_words = []
    with open('words.txt') as f:
        for line in f.readlines():
            my_words.append(line)
    return my_words

def get_random_sentence(length):
    new_sentence = []
    newest = []
    my_words = get_words_from_file()
    for words in range(length):
        my_rand = random.randint(0, len(my_words))
        new_sentence.append(my_words[my_rand].replace("\n", " "))
    new_sentence = " ".join(new_sentence)
    print(new_sentence)


def main():
    print("This program takes a random set of words and creates a new sentenced with the selected number of words. ")
    length = int(input("How many words would you like to use between 2 and 20? "))
    if length < 2 or length > 20:
        raise "Incorrect information provided."
    else:
        get_random_sentence(length)

main()