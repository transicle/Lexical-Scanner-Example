from enum import Enum

# For the sake of simplicity here, we're going to only define the tokens that
#   are used within the `sample.myl` file itself.

# Feel free to edit this program and add your own tokens though! :)

class TokenType(Enum):
    EOF = 1
    IDENTIFIER = 2
    INT = 3

    ####### Keywords #######

    VAR = 4
    FUNC = 5

    ####### Symbols #######

    OPEN_PAREN = 6
    CLOSE_PAREN = 7
    OPEN_BRACE = 8
    CLOSE_BRACE = 9
    EQUALS = 10
    GREATER_THAN = 11
    SEMICOLON = 12

    # Notice how we're excluding comments? It's because these aren't actually tokens!

    # We're going to specifically design the lexer to ignore comments so we don't have
    #   to worry about tokenization for them and waste token space.


class Token():
    def __init__(self,
                 line: int, col: int,
                 lexeme: str,
                 token_type: TokenType):
        self.line = line
        self.col = col
        self.lexeme = lexeme
        self.type = token_type