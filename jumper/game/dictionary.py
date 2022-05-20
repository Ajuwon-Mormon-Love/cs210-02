import random
import re

class Dictionary:
    """A dictionary of words.

    Attributes:
        - _word_list : list[str] - A list of words to be picked from. Could come from anywehere.
        - _mystery_word: str - A single word picked from the list, kept hidden from player. Use for comparison.
        - _revealed_word: str - The mystery word with correctly guessed letters revealed, unguessed
            letters remain hidden.

    Methods:
        + 
        - load_word_list(self): None - Loads up the _word_list with a variety of words.
        + pick_word(self): None - Picks a single word at random from _word_list.
        + display_hidden_word(self): None - Meant for the end of the game if the user does not complete the word.
        + get_revealed_word(self): str - Provides the correctly guessed portions of the word.
        + is_word_complete(self): boolean - Determines if all of the letters have been revealed or not. 
        + check_guess(self, player): Obtains the player's guess and determines if and how it fits into 
            the word. Updates the revealed_word if a match is made.
    """

    def __init__(self):
        """A constructor.

        Parameters:
            self (Dictionary): An instance of Dictionary.
        """
        self._word_list = []
        self._mystery_word = ''
        self._revealed_word = ''
        self._load_word_list()
        self.pick_word()


    def _load_word_list(self):
        """Loads up a list of words.
        
        Parameters:
            self (Dictionary): An instance of Dictionary.
        """
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

        Parameters:
            self (Dictionary): An instance of Dictionary.
        """
        # Pick a random number
        random_index = random.randint(0, len(self._word_list) - 1)
        # Grab the mystery word that appears at that index.
        self._mystery_word = self._word_list[random_index]
        # Generate a string of blanks equal to the length of the mystery word.
        # Only letters should be blanked out, so we will use regex for replacement.
        self._revealed_word = re.sub('[a-zA-Z]','_',self._mystery_word)


    def display_hidden_word(self):
        """Displays the hidden word, usually at the end of the game if the
        player was unable to guess it.

        Parameters:
            self (Dictionary): An instance of Dictionary.
        """
        print(f"The mystery word is: {self._mystery_word}.")


    def get_revealed_word(self):
        """Returns a string of the word with the correctly guessed portions revealed.

        Parameters:
            self (Dictionary): An instance of Dictionary.
        """
        return self._revealed_word


    def is_word_complete(self):
        """Determine if all of the letters in the word have been guessed. Looks at the
        _revealed_word to see if any blanks (_) are left. If there are none, find() 
        returns a -1 which we can check for.

        Parameters:
            self (Dictionary): An instance of Dictionary.
        """
        find_result = self._revealed_word.find('_')
        return find_result == -1


    def check_guess(self, player):
        """Looks at the player's guess and determines if and how it applies to the mystery word.

        Parameters:
            self (Dictionary): An instance of Dictionary.
            player (Player): An instance of Player.
        """
        # make sure we are taking only the first letter of input as lower-case
        # This type of sanitizing should probably be done at the time of input
        # either in the Terminal class or the Player class.
        guess = player.read_guess().lower()[0] 
        
        # Loop through each letter of the mystery word.
        #   With each letter
        #   Compare it to the guess, case-insensitive
        #   If it IS NOT a match, set the corresponding letter in the 
        #       revealed word to itself (could be either a _ or an already guessed letter) 
        #   If it IS a match, set the corresponding letter in the
        #       revealed word to the corresponding letter in the mystery word (could be
        #       a lowercase or Capitalized letter.) 

        # Assume incorrect guess at start.
        correct_guess = False
        new_str = ''
        for i in range(0,len(self._mystery_word)):
            # One-liner below, but we'll expand to more discrete lines just for understanding.
            # new_str += self._mystery_word[i] if guess.lower() == self._mystery_word[i].lower() else self._revealed_word[i] 
            if guess.lower() == self._mystery_word[i].lower():
                new_str += self._mystery_word[i]
                correct_guess = True
            else:
                new_str += self._revealed_word[i]

        # Update the revealed word with our new string.
        self._revealed_word = new_str
        # Return whether the guess was successful or not.
        return correct_guess
















