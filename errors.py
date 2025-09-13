class LexicalError(Exception):
    def __init__(self, message: str, line: int, col: int):
        self.message = message
        super().__init__(f"Lexical Error [ln {line}, col {col}]: {message}.")