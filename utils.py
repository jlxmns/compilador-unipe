## UTILS

from enum import Enum

class TokenType(Enum):
  IDENTIFIER = 0
  NUMINT = 1
  NUMREAL = 2
  MATH_OPERATOR = 3
  REL_OPERATOR = 4
  ASSIGNMENT = 5
  LEFT_PAREN = 6
  RIGHT_PAREN = 7
  COLON = 8
  BLOCK = 9
  END_BLOCK = 10
  STRING = 11

  # Keywords
  INT = 12
  FLOAT = 13
  PRINT = 14
  IF = 15
  ELSE = 16
  THEN = 17
  OR = 18
  AND = 19
  START = 20
  ENDPROG = 21
  DECLS = 22
  ENDDECLS = 23