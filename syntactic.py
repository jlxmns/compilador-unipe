from lexical import Scanner, Token
from utils import TokenType
from errors import SyntacticException

class Parser:
    scanner: Scanner
    token: Token