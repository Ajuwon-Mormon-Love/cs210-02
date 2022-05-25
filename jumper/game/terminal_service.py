class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        try:
            if prompt.lower() == 'a'or'b'or'c'or'd'or'e'or'f'or'g'or'h'or'i'or'j'or'k'or'l'or'm'or'n'or'o'or'p'or'q'or'r'or's'or't'or'u'or'v'or'w'or'x'or'y'or'z':
            # for testing purposes:
                print('valid input+')
            # 
                return input(prompt)

        except:
            print('invalid input')

        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)