import ply.lex as lex
import re


reserved = {
    'select': 'SELECT',
    'where': 'WHERE',
    'limit': 'LIMIT',
    'a': 'A'
}

tokens = [
    "COMMENT",
    "VAR",
    "LBRA",
    "RBRA",
    "NUM",
    "PREFIX",
    "TERM",
    "QUERY",
    "TAG",
    "DOT",
    "ID"
]


tokens = tokens + list(reserved.values())

t_COMMENT = r'\#\s*.*\S'
t_VAR = r'\?'
t_LBRA = r'\{'
t_RBRA = r'\}'
t_QUERY = r'\"[\w\s*]+\"'
t_TAG = r'@\w+'
t_DOT = r'\.'


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_PREFIX(t):
    r'\w+(?=\:)'
    return t


def t_TERM(t):
    r'\:\w+'
    return t


def t_ID(t):
    r'[_A-Za-z]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = """
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
"""


lexer.input(data)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
