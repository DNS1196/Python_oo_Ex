"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, path):
        
        file = open(path) 
        self.words = self.format(file)
        print(f"{len(self.words)} word read")

    def format(self, file):
        """Format the file into a list of words"""

        return [w.strip() for w in file]

    def __repr__(self):
        return f"A list of {len(self.words)} words"
        

    def random(self):
        """Choose a random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

    def format(self,file):
        """
        Format the file into a list of words skipping empty str and lines starting with # """
        
        return [w.strip() for w in file if w.strip() and not w.startswith('#')]