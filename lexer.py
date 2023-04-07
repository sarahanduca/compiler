import ply.lex as lex

class LexicalAnalysis(object):
    def __init__(self):
        self.build()

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
        'int': 'INT',
        'float': 'FLOAT',
        'string': 'STRING',
    }

    tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
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
        'LITSTRING',
        'ID',
        'LSQUAREB',
        'RSQUAREB',
        'NOT',
        'ADRESS'
    ] + list(reserved.values())

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'\/'
    t_GREATER = r'\>'
    t_LESS = r'\<'
    t_EQUAL = r'\=='
    t_NOTEQUAL = r'\!='
    t_ADRESS = r'\='
    t_GREATEREQUAL = r'\>='
    t_LESSEQUAL = r'\<='
    t_NOT = r'\!'


    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    t_LBRAKETS = r'\{'
    t_RBRAKETS = r'\}'

    t_RSQUAREB = r'\['
    t_LSQUAREB = r'\]'

    t_COMMA = r'\,'
    t_SEMICOLON = r'\;'

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_LITSTRING(self, t):
        r'\"([^\']{2,})\"'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')
        return t

    def t_comment(self, t):
        r'\#.*'
        pass


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t\r\f\v'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            print(tok)
