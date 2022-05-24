from game.terminal_service import TerminalService
from game.skydiver import Skydiver
from game.dictionary import Dictionary

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._skydiver = Skydiver()
        self._dictionary = Dictionary()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._evaluation = True


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._skydiver.draw_figure()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    

    def _get_inputs(self):
        new_guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._evaluation = self._dictionary.evaluate_guess(new_guess)


    def _do_updates(self):
        self._skydiver.check_status(self._evaluation)

    def _do_outputs(self):
        self._dictionary.update_letters(self._dictionary._current_letter)
        self._skydiver.draw_figure()
        if self._skydiver.is_dead_status():
            self._is_playing = False
