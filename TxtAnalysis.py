from collections import Counter


class Bag:

    def __init__(self):
        """Create a new empty bag."""
        self.items = Counter()
        self.count = 0

    def size(self) -> int:
        """Return the total number of copies of all items in the bag."""
        return self.count

    def is_empty(self):
        return self.count == 0

    def add(self, item: object) -> None:
        """Add one copy of item to the bag.
           Multiple copies are allowed."""
        self.items[item] =  self.items[item] + 1
        self.count = self.count + 1
		
    def discard(self, item: object) -> None:
        """ Remove at most one copy of item from the bag.
            No effect if item is not in the bag.
        """
        if self.items[item] > 0:
            self.items[item] =  self.items[item] - 1   
            self.count = self.count - 1

    def remove(self):
        if self.is_empty():
            return None
        else:
            self.count -= 1
            return self.items.pop()

    def contains(self, item: object) -> bool:
        """ Return True if there is at least
            one copy of item in the bag.
        """
        
        if self.items[item] > 0:
            return True
        else:
            return False

    def multiplicity(self, item: object) -> int:
        """Return the number of copies of item in the bag.      
        Return zero if the item doesn't occur in the bag.
        """
       
        return self.items[item]
         

    def ordered(self)  -> list:    
        """Return the items ordered by decreasing multiplicity.
        Return a list of (count, item) pairs.
        """
        
        wordlist = list()
        countlist = list()
        for word in self.items:
            wordlist.append(word)
            countlist.append(self.multiplicity(word))
        data = list(zip(countlist,wordlist))
        data.sort(key=lambda tup: tup[0],reverse=True)
        return data



def transform_punctuation(line: str) -> str:
    """ transform any punctuation characters in line into spaces
        returns the transformed line
    """
   
    for p in ['(','[', '{',')', ']','}', '.',',',';',':','_'] :
        line = line.replace(p, ' ')

    return line



def get_excluded_words(filename: str) -> list:
    """Return the excluded words occurring in filename in a suitable data
       structure.

       filename is a string with the name of a text file
    """
   

    # open the file in read-only mode
    excluded_words = list()
    with open(filename, 'r' , encoding ='utf-8') as file:

        # go through the file line by line
        for line in file:

            # use space to separate the words in a line
            for word in line.split():
                word = word.strip("'\"!?+-*/#‘’—")
                word = word.lower()
                if not(word in excluded_words):
                    excluded_words.append(word)
                

    return excluded_words



def bag_of_words(filename: str, excluded_words: list) -> Bag:
    """Return the words occurring in filename as a bag-of-words.

       filename is a string with the name of a text file
    """
    
    words = Bag()
    # open the file in read-only mode
    with open(filename, 'r', encoding ='utf-8') as file:
        # go through the file line by line
        for line in file:
            # transform punctuation into space
            line = transform_punctuation(line)

            # use space to separate the words in a line
            for word in line.split():
                # remove quote marks and other characters
                word = word.strip("'\"!?+-*/#‘’—")
                # put in lowercase
                word = word.lower()
                if not(word in excluded_words):
                    words.add(word)
    return words


print("Collecting excluded words from local excluded.txt file")

excluded_words = get_excluded_words('excluded.txt')

print("Collecting words from  local words.txt file")

all_words = bag_of_words('words.txt', excluded_words)


print('Sorting the words by decreasing frequency...')

orderedwords = all_words.ordered()


TOP = input("See top n most frequent words:")
TOP = int(TOP)
print("The", TOP, "most frequent words are:")

print(orderedwords[:TOP])
