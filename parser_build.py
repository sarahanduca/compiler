import ply.yacc as yacc
from lexer import LexicalAnalysis

tokens = LexicalAnalysis()
tokens = tokens.tokens

precedence = (
    ("left", "OR"),
    ("left", "AND"),
    ("left", "NOT"),
    (
        "nonassoc",
        "EQUAL",
        "GREATER",
        "LESS",
        "GREATEREQUAL",
        "LESSEQUAL",
    ),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)


def p_start(p):
    "main : INT MAIN LPAREN RPAREN scope"
    p[0] = p[5]
    pass


def p_scope(p):
    """
    scope : LBRAKETS statement RBRAKETS
        | LBRAKETS expression RBRAKETS

    """
    p[0] = p[2]


def p_op_expression(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | LPAREN expression RPAREN"""

    if p[2] == "+":
        p[0] = p[1] + p[3]

    elif p[2] == "-":
        p[0] = p[1] - p[3]

    elif p[2] == "*":
        p[0] = p[1] * p[3]

    elif p[2] == "/":
        p[0] = p[1] / p[3]

    else:
        p[0] = p[2]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term(p):
    "term : type ID"
    p[0] = p[2]


def p_type(p):
    """
    type : INT
        | FLOAT
        | STRING
    """

    p[0] = p[1]
    pass


def p_return(p):
    """
    return : RETURN expression SEMICOLON
                | RETURN SEMICOLON
    """

    p[0] = p[2]


def p_adress(p):
    """
    adress : term ADRESS expression SEMICOLON
            | term ADRESS term SEMICOLON
            | term ADRESS NUMBER SEMICOLON
            | term ADRESS LITSTRING SEMICOLON
    """

    p[0] = p[3]


def p_condition(p):
    """
    condition : expression OR expression
        | expression NOT expression
        | expression AND expression
        | expression EQUAL expression
        | condition OR condition
        | condition NOT condition
        | condition AND condition
        | expression NOTEQUAL expression
        | expression GREATER expression
        | expression LESS expression
        | expression GREATEREQUAL expression
        | expression LESSEQUAL expression
        | LPAREN condition RPAREN
        | NOT condition

    """
    p[0] = p[1]
    pass


def p_statement(p):
    """
    statement : expression SEMICOLON
        | if
        | else
        | for
        | while
        | print
        | adress
        | return
    """
    p[0] = p[1]


def p_if(p):
    """if : IF LPAREN condition RPAREN scope
    | if elseif
    | if else"""

    p[0] = p[len(p) - 1]


def p_elseif(p):
    """elseif : ELSEIF LPAREN condition RPAREN scope
    | elseif elseif
    | elseif else
    """

    p[0] = p[len(p) - 1]


def p_else(p):
    "else : ELSE scope"
    p[0] = p[2]


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


def p_for(p):
    """
    for : FOR LPAREN for_initilizer SEMICOLON condition SEMICOLON expression RPAREN scope
    """
    p[0] = p[9]


def p_for_initializer(p):
    """
    for_initilizer : adress

    """
    p[0] = p[1]


def p_while(p):
    """
    while : WHILE LPAREN condition RPAREN scope

    """
    p[0] = p[5]


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
