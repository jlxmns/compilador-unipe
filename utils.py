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