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

  # Keywords
  INT = 10
  FLOAT = 11
  PRINT = 12
  IF = 13
  ELSE = 14
  THEN = 15
  OR = 16
  AND = 17
  START = 18
  END_PROG = 19
  DECLS = 20
  END_DECLS = 21