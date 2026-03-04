# Calculadora em Python

> **Nota:** Este projeto é uma atividade prática desenvolvida para a disciplina de **Testes de Sistemas** do **SENAI**, ministrada pelo professor **Yanes Costa**.

Uma calculadora com interface gráfica construída em Python usando **Tkinter**. O grande foco deste projeto é a aplicação de boas práticas de programação, como a separação de responsabilidades e a criação de **Testes Unitários**.

## Funcionalidades

- Operações básicas: Soma, Subtração, Multiplicação e Divisão.
- Tratamento de exceções (como o erro de divisão por zero).
- Interface gráfica intuitiva (desenvolvida de forma segura, sem o uso de `eval()`).
- Suíte de testes para validar a precisão de todas as operações matemáticas.

## Estrutura do Projeto

O código foi dividido em três arquivos para facilitar a manutenção e os testes:

- `calculadora.py`: Contém apenas a lógica matemática (as funções).
- `interface.py`: Contém a interface gráfica e a conexão com as operações.
- `test_calculadora.py`: Contém os testes automatizados criados com a biblioteca `unittest`.

## Como Executar

O projeto utiliza apenas bibliotecas nativas do Python, então não é necessário instalar dependências externas.

**1. Para abrir a calculadora:**
Abra o terminal na pasta do projeto e rode o comando:

```bash
python interface.py
```

##  Autor
Desenvolvido por **Francisco Pedro**.
