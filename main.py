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
# Grupo:
# Marcelo Camilo
# Gabriel Coutinho
# Júlio Ximenes
# Eduardo Henrique

from lexical import Scanner
from syntactic import Parser
from errors import SyntacticException, LexicalError

def main():
    file_path = "erros_programa_ckp2_traduzido.mc"

    try:
        with open(file_path, 'r') as file:
        #     sc = Scanner(file)
        #     print(sc.source)

        #     while True:
        #         tk = sc.next_token()
        #         print(tk)
        #         if tk is None:
        #           break

          print(f"Compiling {file_path}...")

          scanner = Scanner(file)
          parser = Parser(scanner)
          
          parser.parse_programa()

          print("\n[SUCCESS] Program compiled successfully")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except SyntacticException as e:
        print(f"\n[COMPILATION ERROR]")
        print(f"{e}")
    except LexicalError as e:
        print(f"\n[COMPILATION ERROR]")
        print(f"{e}")
    except Exception as e:
        print(f"An error occurred: {e}")

main()