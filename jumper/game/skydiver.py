from game.terminal_service import TerminalService

class Skydiver:
    """The person in a parachute. 
    
    The responsibility of Skydiver is to display the skydiver in his/her current
    state, and keep track of how much parachute is left. If none, skydiver dies.
    
    Attributes:
        _is_dead_status (boolean): Whether the jumper is dead.
        _index (int): An index pointing to each successive piece of parachute to erase.
        _term (TerminalService): An instance of TerminalService for output.
        _figure (list[str]): The graphical representation of the skydiver.

    Methods:
        __init__(self): Constructor method.
        draw_figure(self): Draws the figure on the screen.
        remove_piece(self): Removes a piece of the parachute.
        is_dead(self): Returns a boolean of whether or not the skydiver is dead.
    """
    
    def __init__(self):
        """Constructor for Skydiver instance.
        
        Args: 
            self (Skydiver): An instance of Skydiver.
        """
        self._is_dead_status = False
        self._index = 0
        self._terminal_service = TerminalService()
        self._figure = [
            ' ___ ',
            '/___\\',
            '\\   /',
            ' \\ /',
            '  0  ',
            ' /|\\',
            ' / \\',
            '      ',
            '^^^^^'
        ]

    def draw_figure(self):
        """Draws the current state of the skydiver figure.
        
        Args: 
            self (Skydiver): An instance of Skydiver.
        """
        for x in self._figure:
            self._terminal_service.write_text(x)
            

    def remove_piece(self):
        """Removes a piece of the parachute.
        
        Args: 
            self (Skydiver): An instance of Skydiver.
        """
        if self._index < 4:
                self._figure[self._index] = '     '
                self._is_dead_status = False
                self._index += 1
        else:
            self._figure[self._index] = '  x  '
            self._is_dead_status = True


    def is_dead(self):
        """Determines if the skydiver has died.
        
        Args: 
            self (Skydiver): An instance of Skydiver.
        
        Returns:
            boolean - True if dead, False if not.
        """
        return self._is_dead_status
    