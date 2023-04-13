import ply.yacc as yacc
from utils.tree import Node
from analyzers.lexer import LexicalAnalysis

tokens = LexicalAnalysis()
tokens = tokens.tokens
variables = {}
scope_id = 0
scope_stack = []


def display_error(var1, var2):
    print("Erro semantico, variveis atribuidas de forma errada.")
    print(f"Tipo {var1} recebendo {var2}.")
    exit()


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


def p_new_scope(p):
    """
    new_scope :
    """
    global scope_id
    scope_stack.append(scope_id)
    scope_id += 1
    pass


def p_scope(p):
    """
    scope : new_scope LBRAKETS multiple_statements RBRAKETS
          | new_scope LBRAKETS expression RBRAKETS
    """
    p[0] = Node("scope", [p[3]])
    scope_stack.pop()


def p_expression(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | LPAREN expression RPAREN
    | term"""

    if len(p) > 2 and p[1] != "(":
        if p[1].validate_type("string", variables) or p[3].validate_type(
            "string", variables
        ):
            print("String atribuida a um dos valores da expressão.")
            exit()

        elif p[2] == "/":
            if p[3].is_zero():
                print("Divisão por zero.")
                exit()

    if len(p) == 2:
        p[0] = Node("expression", [p[1]])

    elif p[1] == "(":
        p[0] = Node("expression", [Node("expression", [p[2]])], [p[1], p[3]])

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
        for variable in variables:
            if p[2] == variable[0] and variable[1] in scope_stack:
                print("Variavel já declarada")
                exit()
        p[0] = Node("type", [p[1], Node("ID", leaf=p[2])], p[2])
        variables[(p[2], scope_stack[-1])] = p[1].leaf

    else:
        for variable in variables:
            if p[1] == variable[0] and variable[1] in scope_stack:
                p[0] = Node("ID", [Node("ID_Scope", leaf=variable[1])], leaf=p[1])
                return

        if p[1] not in variables:
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

    p[0] = Node("var_type", leaf=p[1])
    pass


def p_litstring(p):
    """
    litstring : LITSTRING
    """
    p[0] = Node("STRING", leaf=p[1])


def p_adress(p):
    """
    adress : instance ADRESS factor SEMICOLON
            | instance ADRESS litstring SEMICOLON
            | instance ADRESS expression SEMICOLON
    """
    if p[1].type == "type":
        variable_type = p[1].children[0].leaf
    else:
        variable_type = variables[(p[1].leaf, p[1].children[0].leaf)]

    try:
        if p[3].type == "NUMBER":
            if variable_type == "string":
                raise Exception
            else:
                instance_type = int if (variable_type == "int") else float
                if not isinstance(p[3].leaf, instance_type):
                    raise Exception

        elif p[3].type == "STRING":
            if variable_type != "string":
                raise Exception

        elif p[3].type == "expression":
            if not p[3].validate_all_leafs(variable_type, variables):
                raise Exception
    except:
        display_error(variable_type, p[3].leaf)

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

    if p[3].type != "RPAREN":
        if p[1].type != "NOT":
            if p[1].validate_type("string", variables) or p[3].validate_type(
                "string", variables
            ):
                print("String atribuida a um dos valores da condição.")
                exit()

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
    if p[1].validate_type("string", variables):
        print("Inicializador de for não pode ser do tipo string.")
        exit()
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


def analyze_code(code_file):
    par = yacc.yacc()
    result = par.parse(code_file)
    result.print_tree()
