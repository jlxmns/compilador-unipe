# Compilador Léxico e Sintático em Python

Este projeto implementa a parte **léxica e sintática** de um compilador em Python.  
Ele lê o arquivo de código-fonte `programa_ckp2_traduzido.mc` e realiza a análise sintática e imprime os **tokens** encontrados.

## Estrutura

- `main.py`: arquivo principal que executa o scanner e imprime os tokens.
- `lexical.py`: contém a classe `Scanner`, responsável por percorrer o código e gerar tokens.
- `syntatic.py`: contém a classe `Parser`, responsável pela análise sintática.
- `keywords.py`: define as palavras reservadas da linguagem.
- `utils.py`: define os tipos de tokens (`TokenType`).
- `errors.py`: contém as exceções (`LexicalError`, `SyntacticError`).
- `programa_ckp2_traduzido.mc`: arquivo de entrada (código-fonte de teste).
- `gramatica_ckp2.txt`: especificação da gramática formal da linguagem.

## Como executar

1. Tenha o Python 3 instalado.
2. Clone ou baixe este repositório.
3. Certifique-se de que existe um arquivo `programa_ckp2_traduzido.mc` na raiz do projeto.  
4. Rode o comando: `python main.py`
