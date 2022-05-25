from game.terminal_service import TerminalService
from game.skydiver import Skydiver
from game.dictionary import Dictionary
from game.player import Player

class Director:
    """A person or thing that directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        _skydiver (Skydiver): An instance of Skydiver.
        _dictionary (Dictionary): An instance of Dictionary.
        _player (Player): An instance of Player.
        _term (Terminal_Service): An instance of Terminal_Service.
        _is_playing (boolean): Whether we are still playing the game or not.
        _evaluation: A variable to hold the results of any evaluations.

    Methods:
        __init__(self): Constructor for an instance of Director.
        start_game(self): Starts the game and runs the loop until we are not playing anymore.
        _end_game(self): Handles end-of-game to display some appropriate messages.
        _get_inputs(self): The get input phase of a round.
        _do_updates(self): The update statuses phase of the round.
        _do_outputs(self): The display outputs phase of the round.
        
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._skydiver = Skydiver()
        self._dictionary = Dictionary()
        self._player = Player()
        self._term = TerminalService()
        self._is_playing = True


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:   
            self._do_outputs()
            self._get_inputs()
            self._do_updates()

        self._end_game()


    def _end_game(self):
        """Handles the ending of the game: Either we saved the jumpers life, or we didn't.
        
        Args:
            self (Director): an instance of Director.
        """
        if self._dictionary.is_word_complete():
            self._term.write_text("Congratulations! You saved the skydiver!")
        if self._skydiver.is_dead():
            self._term.write_text("Oh no! The skydiver lost his parachute and didn't survive.")
            self._dictionary.display_mystery_word(self._term)
    

    def _get_inputs(self):
        """The get input phase of the round.
        
        Args:
            self (Director): an instance of Director.
        """
        self._player.set_guess(self._term.read_text("\nGuess a letter [a-z]: "))


    def _do_updates(self):
        """The update statuses phase of the round.
        
        Args:
            self (Director): an instance of Director.
        """
        if not self._dictionary.check_guess(self._player):
            self._skydiver.remove_piece()
        self._is_playing = not (self._dictionary.is_word_complete() or self._skydiver.is_dead())
        

    def _do_outputs(self):
        """The display outputs phase of the round.
        
        Args:
            self (Director): an instance of Director.
        """
        self._skydiver.draw_figure()
        self._term.write_text(self._dictionary.get_revealed_word())

        