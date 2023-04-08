import ply.yacc as yacc
from lexer import LexicalAnalysis

tokens = LexicalAnalysis()
tokens = tokens.tokens

precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)


def p_start(p):
    "main : INT MAIN LPAREN RPAREN LBRAKETS statement RBRAKETS"
    p[0] = p[6]
    pass


def p_op_expression(p):
    """expression : expression PLUS term
    | expression MINUS term
    | expression TIMES term
    | expression DIVIDE term
    | expression GREATER term
    | expression LESS term
    | expression EQUAL term
    | expression NOTEQUAL term
    | expression GREATEREQUAL term
    | expression LESSEQUAL term
    | expression ADRESS term
    | expression NOT term"""

    if p[2] == "+":
        p[0] = p[1] + p[3]

    elif p[2] == "-":
        p[0] = p[1] - p[3]

    elif p[2] == "*":
        p[0] = p[1] * p[3]

    elif p[2] == "/":
        p[0] = p[1] / p[3]

    elif p[2] == ">":
        p[0] = p[1] > p[3]

    elif p[2] == "<":
        p[0] = p[1] < p[3]

    elif p[2] == "==":
        p[0] = p[1] == p[3]

    elif p[2] == "!=":
        p[0] = p[1] != p[3]

    elif p[2] == ">=":
        p[0] = p[1] >= p[3]

    elif p[2] == "<=":
        p[0] = p[1] <= p[3]

    elif p[2] == "=":
        p[0] = p[1] = p[3]

    elif p[2] == "!":
        p[0] = p[1] != p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


# def p_condition(p):
#     """
#     condition : expression OR expression
#         | expression NOT expression
#         | expression AND expression
#         | expression EQUAL expression
#         | condition OR condition
#         | condition NOT condition
#         | condition AND condition
#         | expression NOTEQUAL expression
#         | expression GREATER expression
#         | expression LESSER expression
#         | expression GREATEREQUAL expression
#         | expression LESSEQUAL expression
#         | LPAREN condition RPAREN
#         | NOT condition

#     """
#     p[0] = p[6]
#     pass


def p_statement(p):
    """
    statement : expression SEMICOLON
        | if
        | else
        | for
        | while
        | print
    """
    p[0] = p[1]


def p_if(p):
    """if : IF LPAREN expression RPAREN LBRAKETS statement RBRAKETS"""
    p[0] = p[6]


def p_else(p):
    "else : ELSE LBRAKETS expression RBRAKETS"
    p[0] = p[3]


def p_for(p):
    "for : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LBRAKETS expression RBRAKETS"
    p[0] = p[3]


def p_while(p):
    "while : WHILE LPAREN expression RPAREN LBRAKETS expression RBRAKETS"
    p[0] = p[3]


# TODO print que printa variavel com string print("preco: ", x);
def p_print(p):
    """print : PRINT LPAREN LITSTRING RPAREN SEMICOLON
    | PRINT LPAREN expression RPAREN SEMICOLON"""
    p[0] = p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


def p_error(p):
    print("Syntax error in input at line: ", p.lineno)
    print(p)
    exit(1)


par = yacc.yacc()

while True:
    try:
        s = input("exp > ")
    except EOFError:
        break
    if not s:
        continue
    result = par.parse(s)
    print(result)
