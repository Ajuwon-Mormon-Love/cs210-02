class Player:
    """The person looking guessing in the game. 
    
    The responsibility of a Player is to keep to keep track of its current guess and pass it.
    
    Attributes:
        _guess (str): The guessed letter.

    Methods:
        __init__(self): A constructor for an instance of Player.
        set_guess(self, guess): Sets the player's guess to a value.
        read_guess(self): Returns the player's guess.
    """ 

    def __init__(self):
        """Constructs a new Player.

        Args:
            self (Player): An instance of Player.
        """
        self._guess = ""

    def set_guess(self, guess):
        """Takes an input and stores it as a guess.

        Args:
            self (Player): An instance of Player.
            guess (str): The letter to be stored.
        """
        self._guess = guess

    def read_guess(self):
        """Provides the letter.

        Returns:
            _guess (str): A str that contains a letter.
        """
        return self._guess