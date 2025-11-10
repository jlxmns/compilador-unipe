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

            print(f"   [MATCH OK] Token '{self.token.text}' ({expected_type.name}) consumed.")

            self.next_token()
        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}: "
                f"Unexpected Token '{self.token.text}'. "
                f"Expected '{expected_type.name}'."
            )
    
    def parse_programa(self):
        # REGRA: 
        #   'INICIO' 'DECLS' blocoDeclaracoes 'FIMDECLS' 'CODIGO' blocoComandos 'FIMPROG';
        self.match(TokenType.START)
        self.match(TokenType.DECLS)

        self.parse_blocoDeclaracoes()

        self.match(TokenType.ENDDECLS)
        self.match(TokenType.CODE)

        self.parse_blocoComandos()

        self.match(TokenType.ENDPROG)

    def parse_blocoDeclaracoes(self):
        # REGRA: 
        #   declaracao blocoDeclaracoes | 
        #   declaracao;

        self.parse_declaracao()
        
        while self.token is not None and self.token.token == TokenType.IDENTIFIER:
            self.parse_declaracao()

    def parse_declaracao(self):
        # REGRA: 
        #   ID ':' tipo;

        self.match(TokenType.IDENTIFIER)
        self.match(TokenType.COLON)
        self.parse_tipo()

    def parse_tipo(self):
        # REGRA: 
        #   'INT' | 
        #   'FLOAT';

        if self.token is not None and self.token.token == TokenType.INT:
            self.match(TokenType.INT)        
        
        elif self.token is not None and self.token.token == TokenType.FLOAT:
            self.match(TokenType.FLOAT)
        
        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}: "
                f"Expected 'int' or 'float', found '{self.token.text}'."
            )
        
    def parse_expressaoAritmetica(self):
        # REGRA: 
        #   expressaoAritmetica '+' termo | 
        #   expressaoAritmetica '-' termo | 
        #   termo;

        self.parse_termo()

        while (
            self.token is not None and
            self.token.token == TokenType.MATH_OPERATOR and
            (self.token.text == '+' or self.token.text == '-')
        ):
            self.match(TokenType.MATH_OPERATOR)
            self.parse_termo()

    def parse_termo(self):
        # REGRA: 
        #   termo '*' fator | 
        #   termo '/' fator | 
        #   fator;

        self.parse_fator()

        while(
            self.token is not None and
            self.token.token == TokenType.MATH_OPERATOR and
            (self.token.text == '*' or self.token.text == '/')
        ):
            self.match(TokenType.MATH_OPERATOR)
            self.parse_fator()
    
    def parse_fator(self):
        # REGRA: 
        #   NUMINT | 
        #   NUMREAL |	
        #   ID | 
        #   '(' expressaoAritmetica ')';

        if self.token is not None and self.token.token == TokenType.NUMINT:
            self.match(TokenType.NUMINT)
        
        elif self.token is not None and self.token.token == TokenType.NUMREAL:
            self.match(TokenType.NUMREAL)
        
        elif self.token is not None and self.token.token == TokenType.IDENTIFIER:
            self.match(TokenType.IDENTIFIER)
        
        elif self.token is not None and self.token.token == TokenType.LEFT_PAREN:
            self.match(TokenType.LEFT_PAREN)
            self.parse_expressaoAritmetica()
            self.match(TokenType.RIGHT_PAREN)
        
        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}: "
                f"Expected Number, Identifier or '(', found '{self.token.text}'."
            )
    
    def parse_expressaoRelacional(self):
        # REGRA: 
        #   expressaoRelacional operadorLogico termoRelacional | 
        #   termoRelacional;

        self.parse_termoRelacional()

        while (
            self.token is not None and
            (self.token.token == TokenType.AND or self.token.token == TokenType.OR)
        ):
            self.parse_operadorLogico()
            self.parse_termoRelacional()
    
    def parse_termoRelacional(self):
        # REGRA: 
        #   expressaoAritmetica OP_REL expressaoAritmetica | 
        #   '(' expressaoRelacional ')';

        if self.token is not None and self.token.token == TokenType.LEFT_PAREN:
            self.match(TokenType.LEFT_PAREN)
            self.parse_expressaoRelacional()
            self.match(TokenType.RIGHT_PAREN)
        
        elif self.token is not None and (
            self.token.token == TokenType.IDENTIFIER or
            self.token.token == TokenType.NUMINT or
            self.token.token == TokenType.NUMREAL
        ):
            self.parse_expressaoAritmetica()
            self.match(TokenType.REL_OPERATOR)
            self.parse_expressaoAritmetica()
        
        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}: "
                f"Expected start of an relacional expression (Identifier, Number or '('), "
                f"found '{self.token.text}'."
            )
    
    def parse_operadorLogico(self):
        # REGRA: 
        #   'E' | 
        #   'OU';

        if self.token is not None and self.token.token == TokenType.AND:
            self.match(TokenType.AND)
        
        elif self.token is not None and self.token.token == TokenType.OR:
            self.match(TokenType.OR)

        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}"
                f"Expected 'and' or 'or', found '{self.token.text}'."
            )
    
    def parse_blocoComandos(self):
        # REGRA: 
        #   comando blocoComandos | 
        #   comando;

        self.parse_comando()
        
        while (
            self.token is not None and (
                self.token.token == TokenType.IDENTIFIER or
                self.token.token == TokenType.SCAN or
                self.token.token == TokenType.PRINT or
                self.token.token == TokenType.IF or
                self.token.token == TokenType.WHILE or
                self.token.token == TokenType.BLOCK
            )
        ):
            self.parse_comando()
        
    
    def parse_comando(self):
        # REGRA: 
        #   atribuicao | 
        #   entrada |	
        #   saida | 
        #   condicional | 
        #   repeticao | 
        #   subrotina;

        if self.token is None:
            raise SyntacticException("Error: Unexpected end of file, expected a command.")
        
        elif self.token.token == TokenType.IDENTIFIER:
            self.parse_atribuicao()

        elif self.token.token == TokenType.SCAN:
            self.parse_entrada()

        elif self.token.token == TokenType.PRINT:
            self.parse_saida()

        elif self.token.token == TokenType.IF:
            self.parse_condicional()

        elif self.token.token == TokenType.WHILE:
            self.parse_repeticao()

        elif self.token.token == TokenType.BLOCK:
            self.parse_subrotina()

        else:
            raise SyntacticException(f"Error: '{self.token.text}' is not a valid start of a command.")
    
    def parse_atribuicao(self):
        # REGRA: 
        #   ID '=' expressaoAritmetica;

        self.match(TokenType.IDENTIFIER)
        self.match(TokenType.ASSIGNMENT)
        self.parse_expressaoAritmetica()

    def parse_entrada(self):
        # REGRA: 
        #   'LEIA' ID;

        self.match(TokenType.SCAN)
        self.match(TokenType.IDENTIFIER)
    
    def parse_saida(self):
        # REGRA: 
        #   'ESCREVA' '(' (ID | CADEIA) ')';

        self.match(TokenType.PRINT)
        
        self.match(TokenType.LEFT_PAREN)
        
        if self.token is not None and self.token.token == TokenType.IDENTIFIER:
            self.match(TokenType.IDENTIFIER)

        elif self.token is not None and self.token.token == TokenType.STRING:
            self.match(TokenType.STRING)
        
        else:
            raise SyntacticException(
                f"Error on line {self.scanner.line}"
                f"Expected Identifier or String in Print, found '{self.token.text}'."
            )
        
        self.match(TokenType.RIGHT_PAREN)
    
    def parse_condicional(self):
        # REGRA: 
        #   'SE' expressaoRelacional 'ENTAO' comando |	
        #   'SE' expressaoRelacional 'ENTAO' comando 'SENAO' comando;

        self.match(TokenType.IF)
        self.parse_expressaoRelacional()
        self.match(TokenType.THEN)
        self.parse_comando()

        if self.token is not None and self.token.token == TokenType.ELSE:
            self.match(TokenType.ELSE)
            self.parse_comando()
    
    def parse_repeticao(self):
        # REGRA: 
        #   'REPITA' expressaoRelacional comando;

        self.match(TokenType.WHILE)
        self.parse_expressaoRelacional()
        self.parse_comando()
    
    def parse_subrotina(self):
        # REGRA:
        #   'BLOCO' blocoComandos 'FIMBLOCO';

        self.match(TokenType.BLOCK)
        self.parse_blocoComandos()
        self.match(TokenType.END_BLOCK)