from game.skydiver import Skydiver

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
        self.figure = Skydiver()


    def start_game(self):
        self.figure.draw_figure()
        while self.figure.index <= 4:
            self.figure.delete_line()
            self.figure.draw_figure()
            self.do_checks()
    
    def do_checks(self):
        if self.figure.is_dead:
            print('Game Over!')
