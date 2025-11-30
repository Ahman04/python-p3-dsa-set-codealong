# MySet.py

class MySet:

    def __init__(self, elements=None):
        self.dictionary = {}
        if elements:
            for el in elements:
                self.dictionary[el] = True

    def add(self, element):
        """Add element to the set."""
        self.dictionary[element] = True

    def delete(self, element):
        """Delete element from the set."""
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        """Return True if element in set."""
        return element in self.dictionary

   