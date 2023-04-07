import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'bool': 'BOOL',
    'print': 'PRINT',
    'main': 'MAIN',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

tokens = [
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
    'INT',
    'FLOAT',
    'STRING',
    'ID',
    'LSQUAREB',
    'RSQUAREB',
    'ADRESS'
] + list(reserved.values())

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


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'float'
    return t


def t_STRING(t):
    r'\"([^\']{2,2})\"'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\r\f\v'

def t_comment(t):
    r'\^([^#]*)'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
string = "just tell me"

# Give the lexer some input
lexer.input("if ( x > 5 ) { return x * 7 +  }")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
