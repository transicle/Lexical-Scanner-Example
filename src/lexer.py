from tokens import Token, TokenType

# If you are implementing a scanner in C or C++, things will look significantly different,
#   however they will share identical execution.

# I recommend writing your first lexers in basic languages such as Python or JavaScript to
#  build that initial understanding of how they work, and once you feel more comfortable,
#  you can always switch to a faster, lower level language like C. :)

class Lexer():
    def __init__(self,
                 source: str,
                 position: int,
                 line: int, col: int):
        self.source = source
        self.position = position
        self.line = line
        self.col = col


    ####### Core functions #######

    # The purpose of core functions is generally just to make *our life easier*.

    def peek(self, offset: int = 0): # Reads and returns a character in the source code, following the provided offset.
        return "\0" if (self.position + offset) >= len(self.source) else self.source[self.position + offset]

    def peek_next(self): # Reads the character 1 from the current character, does not shift.
        return self.peek(1)

    def consume(self): # Reads the current character and shifts the scanner up 1.
        char = self.peek()
        if char == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        self.position += 1

    def match(self, expected: str):
        if self.peek() != expected:
            return False
        self.consume()
        return True

    
    ####### Helper functions #######
    
    def is_alnum(self, input: str):
        return input.isalnum()

    # Although not in the example in itself, I'll show you how to support multi-lined comments :)
    def skip_comment(self): # For languages like Python, we'd be able to peek only the current token,
                          #   but for our sample language, we use `//`, so we need to peek 2 ahead.
        if self.peek() == "/" and self.peek_next() == "/":
            self.consume()
            self.consume()

            while self.peek() not in ["\n", "\0"]:
                self.consume()
        elif self.peek() == "/" and self.peek_next() == "*":
            self.consume()
            self.consume()

            while not (self.peek() == "*" and self.peek_next() == "/"):
                if self.peek() == "\0":
                    raise Exception("Unterminated multi-lined comment")
                
                self.consume()

            self.consume()
            self.consume()
    
    def skip_whitespace(self):
        pass
    

    ####### Primary scanner functions #######

    def lex():
        pass