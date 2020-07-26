from anagram_checker import AnagramChecker

class AnagramProgram(AnagramChecker):
    def menu(self):
        self.choice = input("Would you like to enter a word or type exit the program? ").lower()
        return self.choice

    def main(self):
        self.choice = self.menu()
        while self.choice != "exit":
            self.choice = self.choice.lstrip() and self.choice.rstrip()
            if len(self.choice.split()) > 1 or not self.choice.isalpha():
                raise ValueError("You entered more than one word or did not enter only letters.")
            self.valid = self.is_valid_word(self.choice)
            if self.valid:
                self.anagram_list = self.get_anagrams(self.choice)
                print(self)
            else:
                return "Not a valid word."
            self.choice = self.menu()

    def __repr__(self):
        return f"YOUR WORD: {self.choice} \nThis is a valid english word. \nAnagrams for your word are \n{self.anagrams}.\n"