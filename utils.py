## UTILS

from enum import Enum

class TokenType(Enum):
  IDENTIFIER = 0
  NUMBER = 1
  MATH_OPERATOR = 2
  REL_OPERATOR = 3
  ASSIGNMENT = 4
  LEFT_PAREN = 5
  RIGHT_PAREN = 6
  COLON = 7
  BLOCK = 8
  END_BLOCK = 9
  STRING = 10

  # Keywords
  INT = 11
  FLOAT = 12
  PRINT = 13
  IF = 14
  ELSE = 15
  THEN = 16
  OR = 17
  AND = 18
  START = 19
  ENDPROG = 20
  DECLS = 21
  ENDDECLS = 22