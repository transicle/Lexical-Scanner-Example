from pathlib import Path
from lexer import Lexer

# Unlike other programing languages, Python will handle memory allocation for us!

# If you are planning to write your lexical scanner in a language such as C or C++,
#   you'll need to consider proper deallocation to avoid memory leaks.

# For the sake of simplicity I chose Python for this example, to help teach you :)

def read_source_file() -> str:
    project_root = Path(__file__).resolve().parent.parent
    sample_file = project_root / "sample.myl"
    return sample_file.read_text(encoding="utf-8")


def print_tokens(tokens):
    for token in tokens:
        print(
            f"line={token.line:>2} col={token.col:>2} "
            f"type={token.type.name:<12} lexeme={token.lexeme!r}"
        )

lexer = Lexer(
    source=read_source_file(), 
    position=0, line=1, col=1
)

print_tokens(lexer.lex())