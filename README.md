# Compilador Léxico em Python

Este projeto implementa a parte **léxica** de um compilador em Python.  
Ele lê um arquivo de código-fonte fictício (`programa.mc`), realiza a análise léxica e imprime os **tokens** encontrados.

## Estrutura

- `main.py`: arquivo principal que executa o scanner e imprime os tokens.
- `lexical.py`: contém a classe `Scanner`, responsável por percorrer o código e gerar tokens.
- `keywords.py`: define as palavras reservadas da linguagem.
- `utils.py`: define os tipos de tokens (`TokenType`).
- `errors.py`: contém a exceção `LexicalError`.
- `programa.mc`: arquivo de entrada (código-fonte de teste).

## Como executar

1. Tenha o Python 3 instalado.
2. Clone ou baixe este repositório.
3. Certifique-se de que existe um arquivo `programa.mc` na raiz do projeto.  
4. Rode o comando: `python main.py`
