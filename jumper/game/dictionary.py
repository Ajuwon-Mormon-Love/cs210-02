import random
import re
# import os

class Dictionary:
    """A dictionary of words which picks a random mystery word and evaluates letter guesses 
    to see if they are a part of the mystery word.

    Attributes:
        - _word_list : list[str] 
            A list of words to be picked from. Could come from anywehere.
        
        - _mystery_word: str
            A single word picked from the list, kept hidden from player. Use for comparison.
        
        - _revealed_word: str
            The mystery word with correctly guessed letters revealed, unguessed
            letters remain hidden.

    Methods: 
        - load_word_list(self): None 
            Loads up the _word_list with a variety of words.
        
        + pick_word(self): None 
            Picks a single word at random from _word_list.
        
        + display_mystery_word(self): None 
            Meant for the end of the game if the user does not complete the word.
        
        + get_revealed_word(self): str 
            Provides the correctly guessed portions of the word as a string.
        
        + is_word_complete(self): boolean 
            Determines if all of the letters have been revealed or not. 
        
        + check_guess(self, player): int
            Obtains the player's guess and determines if and how it fits into 
            the word. Updates the revealed_word if a match is made. Returns the
            number of matches in the word.
    """

    def __init__(self):
        """A constructor for the Dictionary class.

        Parameters:
            self (Dictionary): An instance of Dictionary.

        Returns: 
            None
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
            
        Returns: 
            None
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

        # with open(f"jumper/data/lexicon.txt") as word_file:
        for word in word_file:
            self._word_list.append(word.replace('\n',''))


    def pick_word(self):
        """Picks a word at random.

        Parameters:
            self (Dictionary): An instance of Dictionary.
            
        Returns: 
            None
        """
        # Pick a random number
        random_index = random.randint(0, len(self._word_list) - 1)
        # Grab the mystery word that appears at that index.
        self._mystery_word = self._word_list[random_index]
        # Generate a string of blanks equal to the length of the mystery word.
        # Only letters should be blanked out, so we will use regex for replacement.
        self._revealed_word = re.sub('[a-zA-Z]','_',self._mystery_word)


    def display_mystery_word(self, terminal):
        """Returns the hidden word, usually at the end of the game if the
        player was unable to guess it.

        Parameters:
            self (Dictionary): An instance of Dictionary.
            terminal (Terminal): An instance of Terminal.
            
        Returns: 
            None
        """
        terminal.write_text(f"The mystery word is: {self._mystery_word}.")


    def get_revealed_word(self):
        """Returns a string of the word with the correctly guessed portions revealed.

        Parameters:
            self (Dictionary): An instance of Dictionary.
            
        Returns: 
            string containing the partially revealed word
        """
        return self._revealed_word


    def is_word_complete(self):
        """Determine if all of the letters in the word have been guessed. Looks at the
        _revealed_word to see if any blanks (_) are left. If there are none, find() 
        returns a -1 which we can check for.

        Parameters:
            self (Dictionary): An instance of Dictionary.

        Returns: 
            boolean - True if all letters have been revealed, False if not 
        """
        find_result = self._revealed_word.find('_')
        return find_result == -1


    def check_guess(self, player):
        """Looks at the player's guess and determines if and how it applies to the mystery word.

        Parameters:
            self (Dictionary): An instance of Dictionary.
            player (Player): An instance of Player.
            
        Returns: 
            integer containing the number of times the letter was found
                (can be inferred as boolean for True/False evaluation)
        """
        # Make sure we are taking only the first letter of input as lower-case.
        # This type of sanitizing should probably be done at the time of input
        # either in the Terminal class or the Player class.
        guess = player.read_guess().lower()[0] 
        number_matches = 0
        new_str = ''

        for i in range(0,len(self._mystery_word)):
            if guess.lower() == self._mystery_word[i].lower():
                new_str += self._mystery_word[i]
                number_matches += 1
            else:
                new_str += self._revealed_word[i]

        # Update the revealed word with our new string.
        self._revealed_word = new_str

        return number_matches