from tokens import Token, TokenType

class Lexer():
    def __init__(self,
                 source: str):
        self.source = source

    ####### Helper functions #######

    # The purpose of helper functions is generally just to make *our life easier*..

    # Stuff like `skip_whitespace`, `is_ident` will genuinely save us so much time and
    #   computational power.

    def peek(self): # Reads the current character in the source code.
        pass

    def peek_next(self): # Reads the character 1 from the current character, does not shift.
        pass

    def consume(self): # Reads the current character and shifts the scanner up 1.
        pass