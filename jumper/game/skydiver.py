from game.terminal_service import TerminalService

class Skydiver:
    """The person in a parachute. 
    
    The responsibility of Skydiver is to make guesses, keep track of its alive status, and update the
    drawing relative to the alive status.
    
    Attributes:
        _figure (int): The location of the hider (1-1000).
        _is_dead (boolean): The alive status of the skydiver.
        _index [list(int)]: The number of guesses remaining for the skydiver (0-4)
        _guess: (str): The guess a player makes.
    """
    def __init__(self):
        
        self.is_dead = False
        self.index = 0
        self._terminal_service = TerminalService()
        self.figure = [
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
        for x in self.figure:
            self._terminal_service.write_text(x)


    def check_status(self, evaluation):
        evaluation = evaluation
        
        if evaluation == True:
            return
        else:
            self.is_dead = self.delete_line()
            

    def delete_line(self):
        if self.index < 4:
                self.figure[self.index] = '     '
                self.is_dead = False
        else:
            self.figure[self.index] = '  x  '
            self.is_dead = True
            return self.is_dead

        self.index += 1


    def is_dead_status(self):
        if self.is_dead == True:
            return True
        else:
            return False

    