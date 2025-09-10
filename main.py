"""
IDENTIFIER:
  LETTER (LETTER | DIGIT)*
NUMBER:
  DIGIT+
MATH_OPERATOR:
  + | - | * | /
REL_OPERATOR:
  > | >= | < | <= | == | !
ASSIGNMENT?
  =
"""
from lexical import Scanner


def main():
    file_path = "programa.mc"

    try:
        with open(file_path, 'r') as file:
            sc = Scanner(file)
            print(sc)
            print(sc.source)

            while True:
                tk = sc.next_token()
                print(tk)
                if tk is None:
                  break

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
