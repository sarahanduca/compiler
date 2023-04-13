import ply.yacc as yacc
from tree import Node
from lexer import LexicalAnalysis

code_input = open("test_input.txt", "r")
tokens = LexicalAnalysis()
tokens = tokens.tokens
# variables = {x: {type: 'int', scope: 0}}
variables = {}


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
    p[0] = Node("main", [p[5]])
    pass


def p_scope(p):
    """
    scope : LBRAKETS multiple_statements RBRAKETS
        | LBRAKETS expression RBRAKETS

    """
    p[0] = Node("scope", [p[2]])


def p_expression(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | LPAREN expression RPAREN
    | term"""

    if len(p) == 2:
        p[0] = Node("expression", [p[1]])
    else:
        p[0] = Node("expression", [p[1], p[3]], p[2])


def p_term(p):
    """term : instance
    | factor
    """

    if p[1].type == "NUMBER":
        p[0] = Node("factor", [p[1]])

    else:
        p[0] = Node("instance", [p[1]])


def p_instance(p):
    """
    instance : type ID
     | ID

    """

    if len(p) == 3:
        if p[2] in variables:
            print("Variavel ja declarada")
            exit()
        else:
            p[0] = Node("type", [p[1], Node("ID", leaf=p[2])], p[2])
            variables[p[2]] = p[1].leaf

    else:
        if p[1] in variables:
            p[0] = Node("ID", leaf=p[1])
        else:
            print("Variavel não declarada")
            exit()


def p_factor(p):
    "factor : NUMBER"
    p[0] = Node("NUMBER", leaf=p[1])


def p_type(p):
    """
    type : INT
        | FLOAT
        | STRING
    """

    p[0] = Node("type", leaf=p[1])
    pass


def p_litstring(p):
    """
    litstring : LITSTRING
    """
    p[0] = Node("STRING", leaf=p[1])


# TODO variavel recebe variavel ja declarada
def p_adress(p):
    """
    adress : instance ADRESS factor SEMICOLON
            | instance ADRESS litstring SEMICOLON
            | instance ADRESS expression SEMICOLON
    """

    if p[3].type == "NUMBER" and variables[p[1].leaf] != "string":
        instance_type = int if (variables[p[1].leaf]) else float
        if not isinstance(p[3].leaf, instance_type):
            print("Erro de tipo")
            exit()
    elif variables[p[1].leaf] == "string":
        if p[3].type != "STRING":
            print("Erro de tipo")
            exit()
    else:
        print("Erro de tipo terceiro")
        exit()

    p[0] = Node("adress", [p[1], p[3]])


def p_return(p):
    """
    return : RETURN expression SEMICOLON
            | RETURN SEMICOLON
    """
    p[0] = Node("return", [p[2]])
    p[0] = Node("return", leaf=p[1])


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
    p[0] = Node("condition", [p[1], p[3]], p[2])
    pass


def p_multiple_statements(p):
    """
    multiple_statements : multiple_statements statement
    | statement
    """
    if len(p) == 2:
        p[0] = Node("multiple_statements", [p[1]])
    else:
        p[0] = Node("multiple_statements", [p[1], p[2]])


def p_statement(p):
    """
    statement : expression SEMICOLON
        | if
        | for
        | while
        | print
        | adress
        | return
    """
    p[0] = Node("statement", [p[1]])


def p_param(p):
    """
    param : param COMMA param
        | term
    """
    if len(p) == 2:
        p[0] = Node("param", [p[1]])
    else:
        p[0] = Node("param", [p[1], p[3]], p[2])


# TODO else printando antes do elseif
def p_if(p):
    """if : IF LPAREN condition RPAREN scope
    | IF LPAREN condition RPAREN scope elseif
    | IF LPAREN condition RPAREN scope ELSE scope"""

    if len(p) == 5:
        p[0] = Node("if", [p[3], p[5]])
    elif len(p) == 6:
        p[0] = Node("if", [p[3], p[5], Node("elseif", [p[len(p) - 1]])])
    else:
        p[0] = Node("if", [p[3], p[5], Node("else", [p[len(p) - 1]])])


def p_elseif(p):
    """elseif : ELSEIF LPAREN condition RPAREN scope
    | ELSEIF LPAREN condition RPAREN scope elseif
    | ELSEIF LPAREN condition RPAREN scope ELSE scope
    """

    if len(p) == 5:
        p[0] = Node("elseif", [p[3], p[5]])
    elif len(p) == 6:
        p[0] = Node("elseif", [p[3], p[5], Node("elseif", [p[len(p) - 1]])])
    else:
        p[0] = Node("elseif", [p[3], p[5], Node("else", [p[len(p) - 1]])])


# TODO verificar prints com variaveis
def p_print(p):
    """print : PRINT LPAREN litstring RPAREN SEMICOLON
    | PRINT LPAREN expression RPAREN SEMICOLON
    | PRINT LPAREN litstring COMMA param RPAREN SEMICOLON"""

    if (len(p)) == 6:
        p[0] = Node("print", leaf=p[3])
    else:
        p[0] = Node("print", [p[5]], p[3])


def p_for(p):
    """
    for : FOR LPAREN for_initilizer condition SEMICOLON expression RPAREN scope
    """
    p[0] = Node("for", [p[3], p[4], p[6], p[8]])


def p_for_initializer(p):
    """
    for_initilizer : adress

    """
    p[0] = Node("for_initilizer", [p[1]])


def p_while(p):
    """
    while : WHILE LPAREN condition RPAREN scope

    """
    p[0] = Node("while", [p[3], p[5]])


def p_error(p):
    print("Syntax error in input at line: ", p.lineno)
    print(p)
    exit(1)


par = yacc.yacc()

s = code_input.read()
result = par.parse(s)
result.print_tree()
print(variables)
