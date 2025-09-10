## LEXICAL

from typing import TextIO
from utils import TokenType


class Token:
    token: TokenType
    text: str

    def __init__(self, token: TokenType, text: str):
        self.token = token
        self.text = text

    def __str__(self):
        return f"Token({self.token}, {self.text})"


class Scanner:
    state: int
    source: list[str]
    pos: int

    def __init__(self, source: TextIO):
        self.state = 0
        self.source = list(source.read())
        self.pos = 0

    @staticmethod
    def _is_letter(c: str) -> bool:
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    @staticmethod
    def _is_digit(c: str) -> bool:
        return '0' <= c <= '9'

    @staticmethod
    def _is_math_operator(c: str) -> bool:
        return c == '+' or c == '-' or c == '*' or c == '/'

    @staticmethod
    def _is_rel_operator(c: str) -> bool:
        return c == '>' or c == '<' or c == '==' or c == '<=' or c == '>=' or c == "!"

    @staticmethod
    def _is_space(c: str) -> bool:
        return c == ' ' or c == '\n' or c == '\t' or c == '\r'

    def _next_char(self) -> str:
        result = self.source[self.pos]
        self.pos += 1
        return result

    def _is_end_of_file(self) -> bool:
        return self.pos >= len(self.source)

    def next_token(self) -> Token | None:
        content_buffer: str = ""
        current_char: str

        while True:
            if self._is_end_of_file():
                return None

            current_char = self._next_char()

            if self.state == 0:
                print('entrou em state 0')
                if self._is_space(current_char):
                    continue
                elif self._is_letter(current_char):
                    print('entrou em is letter')
                    content_buffer += current_char
                    self.state = 1

            elif self.state == 1:
                if self._is_letter(current_char) or self._is_digit(current_char):
                    content_buffer += current_char
                    self.state = 1
                else:
                    self.state = 2

            elif self.state == 2:
                self.back()
                self.state = 0
                return Token(TokenType.IDENTIFIER, content_buffer)

    def back(self):
        self.pos -= 1
