import sys
import ply.yacc as yacc
from exp_lex import tokens


def p_geral(p):
    """
    S : Exp
    """
    print(p[1])


def p_exp_add(p):
    """
    Exp : Exp ADD Termo
    """
    p[0] = p[1] + p[3]


def p_exp_sub(p):
    """
    Exp : Exp SUB Termo
    """
    p[0] = p[1] - p[3]


def p_exp_termo(p):
    """
    Exp : Termo
    """
    p[0] = p[1]


def p_exp_mul(p):
    """
    Termo : Termo MUL Fator
    """
    p[0] = p[1] * p[3]


def p_exp_fator(p):
    """
    Termo : Fator
    """
    p[0] = p[1]


def p_exp_par(p):
    """
    Fator : PARA Exp PARF
    """
    p[0] = p[2]


def p_exp_num(p):
    """
    Fator : NUM
    """
    p[0] = int(p[1])


def p_error(p):
    print("Syntax error", p)
    parser.sucess = False


parser = yacc.yacc()

for linha in sys.stdin:
    parser.sucess = True
    parser.parse(linha)
    if parser.sucess:
        print("Valid:", linha)
    else:
        print("Invalid")
