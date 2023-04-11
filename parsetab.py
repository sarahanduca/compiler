
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTnonassocEQUALGREATERLESSGREATEREQUALLESSEQUALleftPLUSMINUSleftTIMESDIVIDEADRESS AND BOOL COMMA DIVIDE ELSE ELSEIF EQUAL FALSE FLOAT FOR GREATER GREATEREQUAL ID IF INT LBRAKETS LESS LESSEQUAL LITSTRING LPAREN LSQUAREB MAIN MINUS NOT NOTEQUAL NUMBER OR PLUS PRINT RBRAKETS RETURN RPAREN RSQUAREB SEMICOLON STRING TIMES TRUE WHILEmain : INT MAIN LPAREN RPAREN scope\n    scope : LBRAKETS statement RBRAKETS\n        | LBRAKETS expression RBRAKETS\n\n    expression : expression PLUS expression\n    | expression MINUS expression\n    | expression TIMES expression\n    | expression DIVIDE expression\n    | LPAREN expression RPARENexpression : termterm : type ID\n    type : INT\n        | FLOAT\n        | STRING\n    \n    return : RETURN expression SEMICOLON\n                | RETURN SEMICOLON\n    \n    adress : term ADRESS expression SEMICOLON\n            | term ADRESS term SEMICOLON\n            | term ADRESS NUMBER SEMICOLON\n            | term ADRESS LITSTRING SEMICOLON\n    \n    condition : expression OR expression\n        | expression NOT expression\n        | expression AND expression\n        | expression EQUAL expression\n        | condition OR condition\n        | condition NOT condition\n        | condition AND condition\n        | expression NOTEQUAL expression\n        | expression GREATER expression\n        | expression LESS expression\n        | expression GREATEREQUAL expression\n        | expression LESSEQUAL expression\n        | LPAREN condition RPAREN\n        | NOT condition\n\n    \n    statement : expression SEMICOLON\n        | if\n        | else\n        | for\n        | while\n        | print\n        | adress\n        | return\n    if : IF LPAREN condition RPAREN scope\n    | if elseif\n    | if elseelseif : ELSEIF LPAREN condition RPAREN scope\n    | elseif elseif\n    | elseif else\n    else : ELSE scopeprint : PRINT LPAREN LITSTRING RPAREN SEMICOLON\n    | PRINT LPAREN expression RPAREN SEMICOLONterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN\n    for : FOR LPAREN for_initilizer SEMICOLON condition SEMICOLON expression RPAREN scope\n    \n    for_initilizer : adress\n\n    \n    while : WHILE LPAREN condition RPAREN scope\n\n    '
    
_lr_action_items = {'INT':([0,7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[2,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'$end':([1,6,31,32,],[0,-1,-2,-3,]),'MAIN':([2,],[3,]),'LPAREN':([3,7,17,19,21,22,23,25,34,35,36,37,40,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[4,17,17,44,46,47,48,17,17,17,17,17,58,17,64,68,64,17,64,64,64,17,64,64,64,17,17,17,17,17,17,17,17,17,64,17,]),'RPAREN':([4,24,27,41,42,51,52,53,54,55,59,65,72,73,74,76,81,82,96,97,103,105,106,107,108,109,110,111,112,113,114,115,116,124,],[5,-52,-51,59,-9,-10,-4,-5,-6,-7,-8,83,99,100,101,102,103,59,-33,117,-32,-24,-25,-26,-20,-21,-22,-23,-27,-28,-29,-30,-31,125,]),'LBRAKETS':([5,20,83,99,102,125,],[7,7,7,7,7,7,]),'IF':([7,],[19,]),'ELSE':([7,10,31,32,38,39,45,56,57,104,122,],[20,20,-2,-3,20,-44,-48,20,-47,-42,-45,]),'FOR':([7,],[21,]),'WHILE':([7,],[22,]),'PRINT':([7,],[23,]),'RETURN':([7,],[25,]),'FLOAT':([7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'STRING':([7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'NUMBER':([7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[24,24,24,24,24,24,24,62,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'RBRAKETS':([8,9,10,11,12,13,14,15,16,18,24,27,31,32,33,38,39,42,45,50,51,52,53,54,55,56,57,59,75,77,78,79,80,104,119,120,121,122,126,],[31,32,-35,-36,-37,-38,-39,-40,-41,-9,-52,-51,-2,-3,-34,-43,-44,-9,-48,-15,-10,-4,-5,-6,-7,-46,-47,-8,-14,-17,-16,-18,-19,-42,-56,-49,-50,-45,-54,]),'SEMICOLON':([9,18,24,25,27,42,49,51,52,53,54,55,59,60,61,62,63,69,70,77,78,79,80,96,100,101,103,105,106,107,108,109,110,111,112,113,114,115,116,118,],[33,-9,-52,50,-51,-9,75,-10,-4,-5,-6,-7,-8,77,78,79,80,98,-55,-17,-16,-18,-19,-33,120,121,-32,-24,-25,-26,-20,-21,-22,-23,-27,-28,-29,-30,-31,123,]),'PLUS':([9,18,24,27,41,42,49,51,52,53,54,55,59,60,61,62,66,74,82,97,108,109,110,111,112,113,114,115,116,124,],[34,-9,-52,-51,34,-9,34,-10,-4,-5,-6,-7,-8,-9,34,-52,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'MINUS':([9,18,24,27,41,42,49,51,52,53,54,55,59,60,61,62,66,74,82,97,108,109,110,111,112,113,114,115,116,124,],[35,-9,-52,-51,35,-9,35,-10,-4,-5,-6,-7,-8,-9,35,-52,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TIMES':([9,18,24,27,41,42,49,51,52,53,54,55,59,60,61,62,66,74,82,97,108,109,110,111,112,113,114,115,116,124,],[36,-9,-52,-51,36,-9,36,-10,36,36,-6,-7,-8,-9,36,-52,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'DIVIDE':([9,18,24,27,41,42,49,51,52,53,54,55,59,60,61,62,66,74,82,97,108,109,110,111,112,113,114,115,116,124,],[37,-9,-52,-51,37,-9,37,-10,37,37,-6,-7,-8,-9,37,-52,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'ELSEIF':([10,31,32,38,39,45,56,57,104,122,],[40,-2,-3,40,-44,-48,40,-47,-42,-45,]),'ADRESS':([18,24,27,51,59,71,117,],[43,-52,-51,-10,-53,43,-53,]),'OR':([24,27,42,51,52,53,54,55,59,65,66,72,76,81,82,96,103,105,106,107,108,109,110,111,112,113,114,115,116,118,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,84,87,84,84,84,87,-33,-32,-24,-25,-26,-20,-21,-22,-23,-27,-28,-29,-30,-31,84,]),'NOT':([24,27,42,44,47,51,52,53,54,55,58,59,64,65,66,67,72,76,81,82,84,85,86,96,98,103,105,106,107,108,109,110,111,112,113,114,115,116,118,],[-52,-51,-9,67,67,-10,-4,-5,-6,-7,67,-8,67,85,88,67,85,85,85,88,67,67,67,-33,67,-32,85,-25,85,-20,-21,-22,-23,-27,-28,-29,-30,-31,85,]),'AND':([24,27,42,51,52,53,54,55,59,65,66,72,76,81,82,96,103,105,106,107,108,109,110,111,112,113,114,115,116,118,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,86,89,86,86,86,89,-33,-32,86,-25,-26,-20,-21,-22,-23,-27,-28,-29,-30,-31,86,]),'EQUAL':([24,27,42,51,52,53,54,55,59,66,82,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,90,90,]),'NOTEQUAL':([24,27,42,51,52,53,54,55,59,66,82,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,91,91,]),'GREATER':([24,27,42,51,52,53,54,55,59,66,82,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,92,92,]),'LESS':([24,27,42,51,52,53,54,55,59,66,82,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,93,93,]),'GREATEREQUAL':([24,27,42,51,52,53,54,55,59,66,82,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,94,94,]),'LESSEQUAL':([24,27,42,51,52,53,54,55,59,66,82,],[-52,-51,-9,-10,-4,-5,-6,-7,-8,95,95,]),'ID':([26,28,29,30,],[51,-11,-12,-13,]),'LITSTRING':([43,48,],[63,73,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'scope':([5,20,83,99,102,125,],[6,45,104,119,122,126,]),'statement':([7,],[8,]),'expression':([7,17,25,34,35,36,37,43,44,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[9,41,49,52,53,54,55,61,66,66,74,66,82,66,97,66,66,66,108,109,110,111,112,113,114,115,116,66,124,]),'if':([7,],[10,]),'else':([7,10,38,56,],[11,39,57,57,]),'for':([7,],[12,]),'while':([7,],[13,]),'print':([7,],[14,]),'adress':([7,46,],[15,70,]),'return':([7,],[16,]),'term':([7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[18,42,42,42,42,42,42,60,42,71,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'type':([7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'factor':([7,17,25,34,35,36,37,43,44,46,47,48,58,64,67,68,84,85,86,87,88,89,90,91,92,93,94,95,98,123,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'elseif':([10,38,56,],[38,56,56,]),'condition':([44,47,58,64,67,84,85,86,98,],[65,72,76,81,96,105,106,107,118,]),'for_initilizer':([46,],[69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> INT MAIN LPAREN RPAREN scope','main',5,'p_start','parser_build.py',25),
  ('scope -> LBRAKETS statement RBRAKETS','scope',3,'p_scope','parser_build.py',32),
  ('scope -> LBRAKETS expression RBRAKETS','scope',3,'p_scope','parser_build.py',33),
  ('expression -> expression PLUS expression','expression',3,'p_op_expression','parser_build.py',40),
  ('expression -> expression MINUS expression','expression',3,'p_op_expression','parser_build.py',41),
  ('expression -> expression TIMES expression','expression',3,'p_op_expression','parser_build.py',42),
  ('expression -> expression DIVIDE expression','expression',3,'p_op_expression','parser_build.py',43),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_op_expression','parser_build.py',44),
  ('expression -> term','expression',1,'p_expression_term','parser_build.py',63),
  ('term -> type ID','term',2,'p_term','parser_build.py',68),
  ('type -> INT','type',1,'p_type','parser_build.py',74),
  ('type -> FLOAT','type',1,'p_type','parser_build.py',75),
  ('type -> STRING','type',1,'p_type','parser_build.py',76),
  ('return -> RETURN expression SEMICOLON','return',3,'p_return','parser_build.py',85),
  ('return -> RETURN SEMICOLON','return',2,'p_return','parser_build.py',86),
  ('adress -> term ADRESS expression SEMICOLON','adress',4,'p_adress','parser_build.py',94),
  ('adress -> term ADRESS term SEMICOLON','adress',4,'p_adress','parser_build.py',95),
  ('adress -> term ADRESS NUMBER SEMICOLON','adress',4,'p_adress','parser_build.py',96),
  ('adress -> term ADRESS LITSTRING SEMICOLON','adress',4,'p_adress','parser_build.py',97),
  ('condition -> expression OR expression','condition',3,'p_condition','parser_build.py',105),
  ('condition -> expression NOT expression','condition',3,'p_condition','parser_build.py',106),
  ('condition -> expression AND expression','condition',3,'p_condition','parser_build.py',107),
  ('condition -> expression EQUAL expression','condition',3,'p_condition','parser_build.py',108),
  ('condition -> condition OR condition','condition',3,'p_condition','parser_build.py',109),
  ('condition -> condition NOT condition','condition',3,'p_condition','parser_build.py',110),
  ('condition -> condition AND condition','condition',3,'p_condition','parser_build.py',111),
  ('condition -> expression NOTEQUAL expression','condition',3,'p_condition','parser_build.py',112),
  ('condition -> expression GREATER expression','condition',3,'p_condition','parser_build.py',113),
  ('condition -> expression LESS expression','condition',3,'p_condition','parser_build.py',114),
  ('condition -> expression GREATEREQUAL expression','condition',3,'p_condition','parser_build.py',115),
  ('condition -> expression LESSEQUAL expression','condition',3,'p_condition','parser_build.py',116),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition','parser_build.py',117),
  ('condition -> NOT condition','condition',2,'p_condition','parser_build.py',118),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','parser_build.py',127),
  ('statement -> if','statement',1,'p_statement','parser_build.py',128),
  ('statement -> else','statement',1,'p_statement','parser_build.py',129),
  ('statement -> for','statement',1,'p_statement','parser_build.py',130),
  ('statement -> while','statement',1,'p_statement','parser_build.py',131),
  ('statement -> print','statement',1,'p_statement','parser_build.py',132),
  ('statement -> adress','statement',1,'p_statement','parser_build.py',133),
  ('statement -> return','statement',1,'p_statement','parser_build.py',134),
  ('if -> IF LPAREN condition RPAREN scope','if',5,'p_if','parser_build.py',140),
  ('if -> if elseif','if',2,'p_if','parser_build.py',141),
  ('if -> if else','if',2,'p_if','parser_build.py',142),
  ('elseif -> ELSEIF LPAREN condition RPAREN scope','elseif',5,'p_elseif','parser_build.py',148),
  ('elseif -> elseif elseif','elseif',2,'p_elseif','parser_build.py',149),
  ('elseif -> elseif else','elseif',2,'p_elseif','parser_build.py',150),
  ('else -> ELSE scope','else',2,'p_else','parser_build.py',157),
  ('print -> PRINT LPAREN LITSTRING RPAREN SEMICOLON','print',5,'p_print','parser_build.py',163),
  ('print -> PRINT LPAREN expression RPAREN SEMICOLON','print',5,'p_print','parser_build.py',164),
  ('term -> factor','term',1,'p_term_factor','parser_build.py',169),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_build.py',174),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser_build.py',179),
  ('for -> FOR LPAREN for_initilizer SEMICOLON condition SEMICOLON expression RPAREN scope','for',9,'p_for','parser_build.py',185),
  ('for_initilizer -> adress','for_initilizer',1,'p_for_initializer','parser_build.py',192),
  ('while -> WHILE LPAREN condition RPAREN scope','while',5,'p_while','parser_build.py',200),
]
