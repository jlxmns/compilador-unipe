from lexical import Scanner, Token
from utils import TokenType
from errors import SyntacticException

class Parser:
    scanner: Scanner
    token: Token

    def __init__(self, scanner: Scanner):
        self.scanner = scanner
        self.token = None
        self.next_token()

    def next_token(self):
        try:
            self.token = self.scanner.next_token()
        except Exception as e:
            raise SyntacticException(f"Lexical Error: {e}")

    def match(self, expected_type: TokenType):
        if self.token is None:
            raise SyntacticException(
                f"Error: Unexpected end of file. Expected '{expected_type.name}'"
            )
        
        if self.token.token == expected_type:
            self.next_token()
        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}: "
                f"Unexpected Token '{self.token.text}'. "
                f"Expected '{expected_type.name}'."
            )
    
    def parse_programa(self):
        
        self.match(TokenType.START)

        self.match(TokenType.DECLS)

        self.parse_blocoDeclaracoes()

        self.match(TokenType.ENDDECLS)

        self.match(TokenType.CODE)

        self.parse_blocoComandos()

        self.match(TokenType.ENDPROG)

    def parse_blocoDeclaracoes(self):

    def parse_declaracao(self):

    def parse_tipo(self):

    def parse_expressaoAritmetica(self):

    def parse_termo(self):
    
    def parse_fator(self):
    
    def parse_expressaoRelacional(self):
    
    def parse_termoRelacional(self):
    
    def parse_operadorLogico(self):
    
    def parse_blocoComandos(self):
    
    def parse_comando(self):
    
    def parse_atribuicao(self):
    
    def parse_entrada(self):
    
    def parse_saida(self):
    
    def parse_condicional(self):
    
    def parse_repeticao(self):
    
    def parse_subrotina(self):