from lexical import Scanner, Token
from utils import TokenType
from errors import SyntacticException

class Parser:
    scanner: Scanner
    token: Token

    def __init__(self, scanner: Scanner, token: Token):
        self.scanner = scanner
        self.token = token