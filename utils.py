## UTILS

from enum import Enum

class TokenType(Enum):
  IDENTIFIER = 0
  NUMBER = 1
  MATH_OPERATOR = 2
  REL_OPERATOR = 3
  ASSIGNMENT = 4