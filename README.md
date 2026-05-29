# Lexical-Scanner-Example
Writing your own lexical scanner / tokenizer from scratch is the easiest aspect of any compiler, learn how to write your own from scratch to avoid relying on tools to do it for you.

<details>
    <summary>Preview Results</summary>
    <br>
    <img width="506" height="549" alt="image" src="https://github.com/user-attachments/assets/fccbc34a-8f2d-4a85-aad2-09e65cde2108" />
    <br>
</details>

> [!TIP]
> Review [an explanation of the process](#process-explanation) as well as the [technical breakdown](#technical-breakdown-of-the-hand-written-lookahead-scanner).

Run the lexical scanner yourself to see the results:

```bash
$ python ./src/main.py
```

## Example Language

```
var age = 18;

func is18() {
    if age >= 18 {
        return 0;
    }
    return 1;
}

// Comments are awesome!
```

## Process Explanation

A lexical scanner is the first process of compilers or modern interpreters, with its primary job being to turn high level source code into a stream (or array) of tokens.

Tokens are non-literal representations of character(s) that are usually created within a `struct` (C/C++) with a type that holds data to be referenced in the future.

We can essentially "scan" (or analyze) a source file of all its high level code and search for specific keywords, if found, we map them to designated tokens, if unknown, we can map them to an unknown token (typically something like `TOKEN_UNKNOWN`).

If you do not understand, here is a *very simple* visual representation of the lexical scanning process:

```
var myVariable = 1;
```
```
[TOKEN_VAR, TOKEN_IDENTIFIER, TOKEN_EQUALS, TOKEN_INTEGER, TOKEN_SEMICOLON]
```

If tokens in itself were literal representations of code, we would have to create a token for every possible combination, hence why we use `TOKEN_INTEGER` and `TOKEN_IDENTIFIER` for something like numbers or variable names.

Each token *does* in fact hold information though, otherwise we would not be able to do anything with these tokens. Each token should at least hold the **line number**, **column number**, **lexeme** (or value) and optionally (though recommended), the **position** of the character in the file it's currently in (i.e. line 3, column 4, char. 50).

## Technical Breakdown of the Hand-Written Lookahead Scanner.

This scanner is a hand-written lookahead scanner, with a time complexity taking up $O(n)$ time.

The core idea is simple:

1. Store the current character in a variable (for example, `curr = peek(0)`).
2. Branch based on what `curr` is (identifier start, digit, symbol, whitespace, etc.).
3. Use lookahead (`peek(1)`, `peek(2)`, ...) when needed for multi-character tokens.
4. Consume exactly the characters that belong to the token, then emit it.
5. Repeat until the end of input, then emit `TOKEN_EOF`.

### Identifier and Keyword Flow

1. If `curr` is a letter or `_`, begin scanning an identifier.
2. Keep consuming while the next character is a letter, digit, or `_`.
3. Build the full lexeme.
4. Check that lexeme in the keyword map.
5. If present, emit a keyword token; otherwise emit `TOKEN_IDENTIFIER`.

This keeps keyword detection reliable and prevents false splits like `ifCount` becoming `if` + `Count`.

### Symbol Flow with Lookahead

For operators, branch on the current symbol and then inspect the next character:

- If `curr` is `>`, check whether `peek(1)` is `=` to choose between `>=` and `>`.
- If `curr` is `=`, check whether `peek(1)` is `=` to choose between `==` and `=`.

In general, choose the longest valid token first.
