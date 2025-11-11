from utils import TokenType

KEYWORDS = {
    "INT": TokenType.INT,
    "FLOAT": TokenType.FLOAT,
    "ESCREVA": TokenType.PRINT,
    "SE": TokenType.IF,
    "SENAO": TokenType.ELSE,
    "ENTAO": TokenType.THEN,
    "OU": TokenType.OR,
    "E": TokenType.AND,
    "INICIO": TokenType.START,
    "CODIGO": TokenType.CODE,
    "FIMPROG": TokenType.ENDPROG,
    "DECLS": TokenType.DECLS,
    "FIMDECLS": TokenType.ENDDECLS,
    "LEIA": TokenType.SCAN,
    "REPITA": TokenType.WHILE,
    "BLOCO": TokenType.BLOCK,
    "FIMBLOCO": TokenType.END_BLOCK
}