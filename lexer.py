import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'PRINT',
    'LBRAKETS',
    'RBRAKETS',
    'COMMA',
    'SEMICOLON',
    'GREATER',
    'LESS',
    'EQUAL',
    'NOTEQUAL',
    'GREATEREQUAL',
    'LESSEQUAL',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'INT',
    'FLOAT',
    'STRING',
    'BOOL',
    'ID',
    'NOT',
    'RETURN',
    'AND',
    'OR',
    'MAIN',
    'LSQUAREB',
    'RSQUAREB',
    'TRUE',
    'FALSE',
    'ADRESS'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_GREATER = r'\>'
t_LESS = r'\<'
t_EQUAL = r'\=='
t_ADRESS = r'\='
t_NOTEQUAL = r'\!='
t_GREATEREQUAL = r'\>='
t_LESSEQUAL = r'\<='
t_NOT = r'\!'
t_AND = r'and'
t_OR = r'or'


t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LBRAKETS = r'\{'
t_RBRAKETS = r'\}'

t_RSQUAREB = r'\['
t_LSQUAREB = r'\]'

t_COMMA = r'\,'
t_SEMICOLON = r'\;'

# A regular expression rule with some action code


def t_INT(t):
    r'int'
    return t


def t_PRINT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IF(t):
    r'if'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'float'
    return t


def t_BOOL(t):
    r'bool'
    return t


def t_TRUE(t):
    r'true'
    return t


def t_FALSE(t):
    r'false'
    return t


def t_STRING(t):
    r'string'
    return t


def t_ID(t):
    r'id'
    return t


def t_RETURN(t):
    r'return'
    return t


# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Give the lexer some input
lexer.input("int i = 3 ")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
