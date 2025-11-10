from typing import TextIO

from errors import LexicalError
from utils import TokenType
from keywords import KEYWORDS


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
    col: int
    line: int
    prev_col: int
    prev_line: int
    isComment: bool

    def __init__(self, source: TextIO):
        self.state = 0
        self.source = list(source.read())
        self.pos = 0
        self.col = 0
        self.line = 1
        self.prev_col = 0
        self.prev_line = 0
        self.isComment = False

    @staticmethod
    def _is_letter(c: str) -> bool:
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    @staticmethod
    def _is_underscore(c: str) -> bool:
        return c == '_'

    @staticmethod
    def _is_digit(c: str) -> bool:
        return '0' <= c <= '9'

    @staticmethod
    def _is_math_operator(c: str) -> bool:
        return c == '+' or c == '-' or c == '*' or c == '/'

    @staticmethod
    def _is_rel_operator_start(c: str) -> bool:
        return c == '>' or c == '<' or c == '=' or c == '!'

    @staticmethod
    def _is_assignment_operator(c: str) -> bool:
        return c == '='

    @staticmethod
    def _is_left_paren(c: str) -> bool:
        return c == '('

    @staticmethod
    def _is_right_paren(c: str) -> bool:
        return c == ')'

    @staticmethod
    def _is_colon(c: str) -> bool:
        return c == ':'

    @staticmethod
    def _is_block(c: str) -> bool:
        return c == '{'

    @staticmethod
    def _is_end_block(c: str) -> bool:
        return c == '}'

    @staticmethod
    def _is_space(c: str) -> bool:
        return c == ' ' or c == '\n' or c == '\t' or c == '\r'

    def _is_comment(self, c: str) -> bool:
        if c == '/' and not self._is_end_of_file():
            nxt = self._next_char()
            if nxt == '*':
                self._skip_multiline_comment()
                return True
            else:
                self.back()
        self.isComment = c == '#' or self.isComment
        return self.isComment

    def _skip_multiline_comment(self):
        while not self._is_end_of_file():
            c = self._next_char()
            if c == '*' and not self._is_end_of_file():
                nxt = self._next_char()
                if nxt == '/':
                    return
                else:
                    self.back()


    def _next_char(self) -> str:
        self.prev_line = self.line
        self.prev_col = self.col

        result = self.source[self.pos]
        self.pos += 1

        if result == '\n' or result == '\r':
            self.line += 1
            self.col = 0
            self.isComment = False
        else:
            self.col += 1

        return result

    def _is_end_of_file(self) -> bool:
        return self.pos >= len(self.source)

    def next_token(self) -> Token | None:
        content_buffer: str = ""
        current_char: str

        while True:
            if self._is_end_of_file():
                if content_buffer:
                    if self.state == 1:
                        self.state = 0
                        token_type = KEYWORDS.get(content_buffer, TokenType.IDENTIFIER)
                        return Token(token_type, content_buffer)
                    elif self.state == 3:
                        self.state = 0
                        return Token(TokenType.NUMINT, content_buffer)
                    elif self.state == 4:
                        if content_buffer.endswith('.'):
                            raise LexicalError(f"Invalid number '{content_buffer}'", self.line, self.col)
                        self.state = 0
                        return Token(TokenType.NUMREAL, content_buffer)
                    elif self.state == 5 or self.state == 6:
                        raise LexicalError(f"Unterminated string", self.line, self.col)
                return None

            current_char = self._next_char()

            if self.state == 0:
                if self._is_comment(current_char):
                    continue
                elif self._is_space(current_char):
                    continue
                elif self._is_letter(current_char) or self._is_underscore(current_char):
                    content_buffer += current_char
                    self.state = 1
                elif self._is_digit(current_char):
                    content_buffer += current_char
                    self.state = 3
                elif current_char == '.':
                    content_buffer += current_char
                    self.state = 4
                elif current_char == '"':
                    self.state = 5
                elif current_char == "'":
                    self.state = 6
                

                # caracteres relacionais

                elif self._is_rel_operator_start(current_char):

                    next_char = None
                    if not self._is_end_of_file():
                        next_char = self._next_char()
                    else:
                        next_char = None

                    two_char = None
                    if next_char is not None:
                        two_char = current_char + next_char

                    # caracteres relacionais validos
                    if two_char in ('>=', '<=', '!=', '=='):
                        return Token(TokenType.REL_OPERATOR, two_char)
                    else:
                        # Se não formou operador  "desfazemos" o peek (voltar o next_char)
                        if next_char is not None:
                            self.back()

                        # Agora tratamos os operadores de caractere único
                        if current_char in ('>', '<'):
                            return Token(TokenType.REL_OPERATOR, current_char)
                        elif current_char == '=':

                            return Token(TokenType.ASSIGNMENT, current_char)
                        else:
                            # '!' sozinho não é reconhecido como operador válido -> erro léxico
                            raise LexicalError(f"Invalid character '{current_char}'", self.line, self.col)

                elif self._is_math_operator(current_char):
                    return Token(TokenType.MATH_OPERATOR, current_char)
                elif self._is_left_paren(current_char):
                    return Token(TokenType.LEFT_PAREN, current_char)
                elif self._is_right_paren(current_char):
                    return Token(TokenType.RIGHT_PAREN, current_char)
                elif self._is_colon(current_char):
                    return Token(TokenType.COLON, current_char)
                elif self._is_block(current_char):
                    return Token(TokenType.BLOCK, current_char)
                elif self._is_end_block(current_char):
                    return Token(TokenType.END_BLOCK, current_char)
                else:
                    raise LexicalError(f"Invalid character '{current_char}'", self.line, self.col)

            # States for IDENTIFIER
            elif self.state == 1:
                if self._is_letter(current_char) or self._is_digit(current_char):
                    content_buffer += current_char
                else:
                    # Any character that ends IDENTIFIER
                    # self.state = 2
                    if (
                            self._is_space(current_char)
                            or self._is_math_operator(current_char)
                            or self._is_assignment_operator(current_char)
                            or self._is_left_paren(current_char)
                            or self._is_right_paren(current_char)
                            or self._is_colon(current_char)
                    ):
                        self.back()
                        self.state = 0

                        token_type = KEYWORDS.get(content_buffer, TokenType.IDENTIFIER)
                        return Token(token_type, content_buffer)
                    else:
                        raise LexicalError(f"Invalid character '{current_char}' after identifier '{content_buffer}'", self.line, self.col)


            # elif self.state == 2:
            #     self.back()
            #     self.state = 0
            #     return Token(TokenType.IDENTIFIER, content_buffer)

            # States for NUMBER INT
            elif self.state == 3: # before '.'
                if self._is_digit(current_char):
                    content_buffer += current_char
                elif current_char == '.':
                    content_buffer += current_char
                    self.state = 4
                else:
                    if (
                            self._is_space(current_char)
                            or self._is_math_operator(current_char)
                            or self._is_assignment_operator(current_char)
                            # or self._is_rel_operator_start(current_char)
                            or self._is_left_paren(current_char)
                            or self._is_right_paren(current_char)
                    ):
                        if content_buffer.endswith('.'):
                            raise LexicalError(f"Invalid number '{content_buffer}'", self.line, self.col)
                        self.back()
                        self.state = 0
                        return Token(TokenType.NUMINT, content_buffer)
                    else:
                        raise LexicalError(f"Invalid character '{current_char}' after number '{content_buffer}'", self.line, self.col)

            elif self.state == 4: # After '.'
                if self._is_digit(current_char):
                    content_buffer += current_char
                else:
                    if content_buffer.endswith('.'):
                        raise LexicalError(f"Invalid number '{content_buffer}'", self.line, self.col)
                    if (
                            self._is_space(current_char)
                            or self._is_math_operator(current_char)
                            or self._is_assignment_operator(current_char)
                            or self._is_left_paren(current_char)
                            or self._is_right_paren(current_char)
                    ):
                        self.back()
                        self.state = 0
                        return Token(TokenType.NUMREAL, content_buffer)
                    else:
                        raise LexicalError(f"Invalid character '{current_char}' after number '{content_buffer}'", self.line, self.col)

            elif self.state == 5: # Reading String double quotes ("string") State
                if current_char == '"':
                    self.state = 0
                    return Token(TokenType.STRING, content_buffer)
                elif current_char == '\n' or current_char == '\r':
                    raise LexicalError(f"Unterminated string", self.line, self.col)
                else:
                    content_buffer += current_char

            elif self.state == 6: # Reading String single quotes ('string') State
                if current_char == "'":
                    self.state = 0
                    return Token(TokenType.STRING, content_buffer)
                elif current_char == '\n' or current_char == '\r':
                    raise LexicalError(f"Unterminated string", self.line, self.col)
                else:
                    content_buffer += current_char

    def back(self):
        self.col = self.prev_col
        self.line = self.prev_line
        self.pos -= 1
