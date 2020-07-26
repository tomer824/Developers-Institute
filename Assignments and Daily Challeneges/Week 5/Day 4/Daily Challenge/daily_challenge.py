

# Write a TextModification class that inherits from Text
# Implement the following:
# a method that returns the text without punctuation
# a method that returns the text without english stop-words (check out what this is !!)
# a method that returns the text without special characters
# Now, use the provided txt file and try using the class you created above.
# Provide a meaningful word frequency insight (meaning if ‘the’ is the most used word it is no surprise, try to come up with a way to get something better).

# Note: Feel free to implement every attribute or method or function to succeed, be creative

class Text():
    def __init__(self, string):
        self.string = string
        self.word_list = self.string.split()

    def how_many(self, word):
        if word in self.word_list:
            count = 0
            for x in self.word_list:
                if x == word:
                    count += 1
            return f"The word \"{word}\" is in the text {count} times."
        return "The word \"{word}\" is not in the text"

    def most_common(self):
        self.word_dict = {}
        self.most_used_word = ""
        times_used = 0
        for word in self.word_list:
            if word in self.word_dict:
                self.word_dict[word] = self.word_dict[word] + 1
            else:
                self.word_dict[word] = 1
        for item in self.word_dict.items():
            if item[1] > times_used:
                times_used = item[1]
                self.most_used_word = item[0]
        return self.most_used_word

    def unique_words(self):
        my_set = set(self.word_list)
        print(list(my_set))  

    @classmethod
    def text_file(cls, file):
        with open(file, "r") as f:
            my_lines = str(f.read().replace("\n", " "))
        return cls(my_lines)