import ply.lex as lex

tokens = ['NUM',
          'ADD',
          'SUB',
          'MUL',
          'PARA',
          'PARF']


t_ADD = r'\+'
t_SUB = r'\-'
t_NUM = r'\d+'
t_MUL = r'\*'
t_PARA = r'\('
t_PARF = r'\)'

t_ignore = " \n\t"


def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
