class Skydiver:

    def __init__(self):
        
        self.is_dead = False
        self.index = 0
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
            print(x) 

    def delete_line(self):
        if self.index < 4:
            self.figure[self.index] = '     '
        else:
            self.figure[self.index] = '  x  '
            self.is_dead = True

        self.index += 1
        
