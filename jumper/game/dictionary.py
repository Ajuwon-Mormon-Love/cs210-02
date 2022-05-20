import random

class Dictionary:
    """A dictionary of words.
    """

    def __init__(self):
        """A constructor.
        """

        self._word_list = []
        self._mystery_word = ''
        self._revealed_word = ''

        self._load_word_list()
        self.pick_word()


    def _load_word_list(self):
        """Loads up a list of words."""
        # Open a file maybe later, but for now we will just define 10 words.
        word_file = [
            'engagement',
            'cluster',
            'material',
            'hour',
            'slip',
            'rotation',
            'executive',
            'pen',
            'context',
            'choose',
        ]

        ## The following is a loop that would be employed if reading a text file. 
        ## This will make the transition easy to using larger data.
        # with open("lexicon.txt") as word_file:
        for word in word_file:
            self._word_list.append(word)


    def pick_word(self):
        """Picks a word at random.
        """
        # Pick a random number
        random_index = random.randint(0, len(self._word_list) - 1)
        # Grab the mystery word that appears at that index.
        self._mystery_word = self._word_list[random_index]
        # Generate a string of blanks equal to the length of the mystery word.
        self._revealed_word = '_' * len(self._mystery_word)


    def display_hidden_word(self):
        """Displays the hidden word, usually at the end of the game if the
        player was unable to guess it."""
        print(f"The mystery word is: {self._mystery_word}.")


    def get_revealed_word(self):
        """Returns a string of the word with the correctly guessed portions revealed.
        """
        return self._revealed_word


    # Now for the heavy one.
    def check_guess(self, player):
        """Looks at the player's guess and determines if and how it applies to the mystery word.
        """
        # make sure we are taking only the first letter of input as lower-case
        # unless @Spencer can guarantee that this is the input we will get.
        guess = player.read_guess().lower()[0] 
        
        # Loop through each letter of the mystery word.
        #   With each letter
        #   Compare it to the guess, case-insensitive
        #   If it IS NOT a match, set the corresponding letter in the 
        #       revealed word to itself (could be either a _ or a already guessed letter) 
        #   If it IS a match, set the corresponding letter in the
        #       revealed word to the corresponding letter in the mystery word (could be
        #       a lowercase or Capitalized letter.) 

        # Assume incorrect guess.
        correct_guess = False
        new_str = ''
        for i in range(0,len(self._mystery_word)):
            # One-liner below, but we'll expand to smaller pieces just for understanding.
            # new_str += self._mystery_word[i] if guess.lower() == self._mystery_word[i].lower() else self._revealed_word[i] 
            if guess.lower() == self._mystery_word[i].lower():
                new_str += self._mystery_word[i]
                correct_guess = True
            else:
                new_str += self._revealed_word[i]

        self._revealed_word = new_str
        return correct_guess
















