
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTnonassocEQUALGREATERLESSGREATEREQUALLESSEQUALleftPLUSMINUSleftTIMESDIVIDEADRESS AND BOOL COMMA DIVIDE ELSE ELSEIF EQUAL FALSE FLOAT FOR GREATER GREATEREQUAL ID IF INT LBRAKETS LESS LESSEQUAL LITSTRING LPAREN LSQUAREB MAIN MINUS NOT NOTEQUAL NUMBER OR PLUS PRINT RBRAKETS RETURN RPAREN RSQUAREB SEMICOLON STRING TIMES TRUE WHILEmain : INT MAIN LPAREN RPAREN scope\n    new_scope :\n    \n    scope : new_scope LBRAKETS multiple_statements RBRAKETS\n          | new_scope LBRAKETS expression RBRAKETS\n    expression : expression PLUS expression\n    | expression MINUS expression\n    | expression TIMES expression\n    | expression DIVIDE expression\n    | LPAREN expression RPAREN\n    | termterm : instance\n    | factor\n    \n    instance : type ID\n            | ID\n    factor : NUMBER\n    type : INT\n        | FLOAT\n        | STRING\n    \n    litstring : LITSTRING\n    \n    adress : instance ADRESS factor SEMICOLON\n            | instance ADRESS litstring SEMICOLON\n            | instance ADRESS expression SEMICOLON\n    \n    return : RETURN expression SEMICOLON\n            | RETURN SEMICOLON\n    \n    condition : expression OR expression\n        | expression NOT expression\n        | expression AND expression\n        | expression EQUAL expression\n        | condition OR condition\n        | condition NOT condition\n        | condition AND condition\n        | expression NOTEQUAL expression\n        | expression GREATER expression\n        | expression LESS expression\n        | expression GREATEREQUAL expression\n        | expression LESSEQUAL expression\n        | LPAREN condition RPAREN\n        | NOT condition\n    \n    multiple_statements : multiple_statements statement\n    | statement\n    \n    statement : expression SEMICOLON\n        | if\n        | for\n        | while\n        | print\n        | adress\n        | return\n    \n    param : param COMMA param\n        | term\n    if : IF LPAREN condition RPAREN scope\n    | IF LPAREN condition RPAREN scope elseif\n    | IF LPAREN condition RPAREN scope ELSE scopeelseif : ELSEIF LPAREN condition RPAREN scope\n    | ELSEIF LPAREN condition RPAREN scope elseif\n    | ELSEIF LPAREN condition RPAREN scope ELSE scope\n    print : PRINT LPAREN litstring RPAREN SEMICOLON\n    | PRINT LPAREN expression RPAREN SEMICOLON\n    | PRINT LPAREN litstring COMMA param RPAREN SEMICOLON\n    for : FOR LPAREN for_initilizer condition SEMICOLON expression RPAREN scope\n    \n    for_initilizer : adress\n    \n    while : WHILE LPAREN condition RPAREN scope\n    '
    
_lr_action_items = {'INT':([0,8,9,11,12,14,15,16,17,18,19,26,33,34,37,38,39,40,41,42,45,46,47,48,49,51,62,65,66,67,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,95,98,111,112,113,116,117,121,123,124,127,129,131,132,134,],[2,30,30,-40,30,-42,-43,-44,-45,-46,-47,30,-3,-39,-4,30,30,30,30,-41,30,30,30,30,30,-24,30,30,30,-60,-23,-20,-21,-22,30,30,30,30,30,30,30,30,30,30,30,30,30,-50,30,-61,-56,-57,-51,30,-52,30,-58,-59,-53,-54,-55,]),'$end':([1,6,33,37,],[0,-1,-3,-4,]),'MAIN':([2,],[3,]),'LPAREN':([3,8,9,11,12,14,15,16,17,18,19,22,23,24,25,26,33,34,37,38,39,40,41,42,45,46,48,49,51,62,65,66,67,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,98,111,112,113,116,117,119,123,124,127,129,131,132,134,],[4,12,12,-40,12,-42,-43,-44,-45,-46,-47,46,47,48,49,12,-3,-39,-4,12,12,12,12,-41,12,62,62,12,-24,62,62,62,-60,-23,-20,-21,-22,62,62,62,12,12,12,12,12,12,12,12,12,-50,12,-61,-56,-57,-51,124,-52,62,-58,-59,-53,-54,-55,]),'RPAREN':([4,13,21,28,29,43,44,52,53,54,55,56,57,61,63,69,70,71,76,77,91,97,99,100,101,102,103,104,105,106,107,108,109,110,114,115,120,126,128,],[5,-10,-12,-14,-15,57,-11,-13,-5,-6,-7,-8,-9,-19,78,93,94,96,97,57,-38,-37,-29,-30,-31,-25,-26,-27,-28,-32,-33,-34,-35,-36,122,-49,125,-48,130,]),'LBRAKETS':([5,7,78,93,118,125,130,133,],[-2,8,-2,-2,-2,-2,-2,-2,]),'IF':([8,9,11,14,15,16,17,18,19,33,34,37,42,51,72,73,74,75,98,112,113,116,117,123,127,129,131,132,134,],[22,22,-40,-42,-43,-44,-45,-46,-47,-3,-39,-4,-41,-24,-23,-20,-21,-22,-50,-61,-56,-57,-51,-52,-58,-59,-53,-54,-55,]),'FOR':([8,9,11,14,15,16,17,18,19,33,34,37,42,51,72,73,74,75,98,112,113,116,117,123,127,129,131,132,134,],[23,23,-40,-42,-43,-44,-45,-46,-47,-3,-39,-4,-41,-24,-23,-20,-21,-22,-50,-61,-56,-57,-51,-52,-58,-59,-53,-54,-55,]),'WHILE':([8,9,11,14,15,16,17,18,19,33,34,37,42,51,72,73,74,75,98,112,113,116,117,123,127,129,131,132,134,],[24,24,-40,-42,-43,-44,-45,-46,-47,-3,-39,-4,-41,-24,-23,-20,-21,-22,-50,-61,-56,-57,-51,-52,-58,-59,-53,-54,-55,]),'PRINT':([8,9,11,14,15,16,17,18,19,33,34,37,42,51,72,73,74,75,98,112,113,116,117,123,127,129,131,132,134,],[25,25,-40,-42,-43,-44,-45,-46,-47,-3,-39,-4,-41,-24,-23,-20,-21,-22,-50,-61,-56,-57,-51,-52,-58,-59,-53,-54,-55,]),'RETURN':([8,9,11,14,15,16,17,18,19,33,34,37,42,51,72,73,74,75,98,112,113,116,117,123,127,129,131,132,134,],[26,26,-40,-42,-43,-44,-45,-46,-47,-3,-39,-4,-41,-24,-23,-20,-21,-22,-50,-61,-56,-57,-51,-52,-58,-59,-53,-54,-55,]),'ID':([8,9,11,12,14,15,16,17,18,19,26,27,30,31,32,33,34,37,38,39,40,41,42,45,46,47,48,49,51,62,65,66,67,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,95,98,111,112,113,116,117,121,123,124,127,129,131,132,134,],[28,28,-40,28,-42,-43,-44,-45,-46,-47,28,52,-16,-17,-18,-3,-39,-4,28,28,28,28,-41,28,28,28,28,28,-24,28,28,28,-60,-23,-20,-21,-22,28,28,28,28,28,28,28,28,28,28,28,28,28,-50,28,-61,-56,-57,-51,28,-52,28,-58,-59,-53,-54,-55,]),'NUMBER':([8,9,11,12,14,15,16,17,18,19,26,33,34,37,38,39,40,41,42,45,46,48,49,51,62,65,66,67,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,95,98,111,112,113,116,117,121,123,124,127,129,131,132,134,],[29,29,-40,29,-42,-43,-44,-45,-46,-47,29,-3,-39,-4,29,29,29,29,-41,29,29,29,29,-24,29,29,29,-60,-23,-20,-21,-22,29,29,29,29,29,29,29,29,29,29,29,29,29,-50,29,-61,-56,-57,-51,29,-52,29,-58,-59,-53,-54,-55,]),'FLOAT':([8,9,11,12,14,15,16,17,18,19,26,33,34,37,38,39,40,41,42,45,46,47,48,49,51,62,65,66,67,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,95,98,111,112,113,116,117,121,123,124,127,129,131,132,134,],[31,31,-40,31,-42,-43,-44,-45,-46,-47,31,-3,-39,-4,31,31,31,31,-41,31,31,31,31,31,-24,31,31,31,-60,-23,-20,-21,-22,31,31,31,31,31,31,31,31,31,31,31,31,31,-50,31,-61,-56,-57,-51,31,-52,31,-58,-59,-53,-54,-55,]),'STRING':([8,9,11,12,14,15,16,17,18,19,26,33,34,37,38,39,40,41,42,45,46,47,48,49,51,62,65,66,67,72,73,74,75,79,80,81,82,83,84,85,86,87,88,89,90,95,98,111,112,113,116,117,121,123,124,127,129,131,132,134,],[32,32,-40,32,-42,-43,-44,-45,-46,-47,32,-3,-39,-4,32,32,32,32,-41,32,32,32,32,32,-24,32,32,32,-60,-23,-20,-21,-22,32,32,32,32,32,32,32,32,32,32,32,32,32,-50,32,-61,-56,-57,-51,32,-52,32,-58,-59,-53,-54,-55,]),'RBRAKETS':([9,10,11,13,14,15,16,17,18,19,20,21,28,29,33,34,37,42,44,51,52,53,54,55,56,57,72,73,74,75,98,112,113,116,117,123,127,129,131,132,134,],[33,37,-40,-10,-42,-43,-44,-45,-46,-47,-11,-12,-14,-15,-3,-39,-4,-41,-11,-24,-13,-5,-6,-7,-8,-9,-23,-20,-21,-22,-50,-61,-56,-57,-51,-52,-58,-59,-53,-54,-55,]),'PLUS':([10,13,20,21,28,29,35,36,43,44,50,52,53,54,55,56,57,58,60,64,71,77,102,103,104,105,106,107,108,109,110,120,],[38,-10,-11,-12,-14,-15,38,-11,38,-11,38,-13,-5,-6,-7,-8,-9,-12,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'MINUS':([10,13,20,21,28,29,35,36,43,44,50,52,53,54,55,56,57,58,60,64,71,77,102,103,104,105,106,107,108,109,110,120,],[39,-10,-11,-12,-14,-15,39,-11,39,-11,39,-13,-5,-6,-7,-8,-9,-12,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'TIMES':([10,13,20,21,28,29,35,36,43,44,50,52,53,54,55,56,57,58,60,64,71,77,102,103,104,105,106,107,108,109,110,120,],[40,-10,-11,-12,-14,-15,40,-11,40,-11,40,-13,40,40,-7,-8,-9,-12,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'DIVIDE':([10,13,20,21,28,29,35,36,43,44,50,52,53,54,55,56,57,58,60,64,71,77,102,103,104,105,106,107,108,109,110,120,],[41,-10,-11,-12,-14,-15,41,-11,41,-11,41,-13,41,41,-7,-8,-9,-12,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'SEMICOLON':([10,13,20,21,26,28,29,35,36,44,50,52,53,54,55,56,57,58,59,60,61,91,92,94,96,97,99,100,101,102,103,104,105,106,107,108,109,110,122,],[42,-10,-11,-12,51,-14,-15,42,-11,-11,72,-13,-5,-6,-7,-8,-9,73,74,75,-19,-38,111,113,116,-37,-29,-30,-31,-25,-26,-27,-28,-32,-33,-34,-35,-36,127,]),'OR':([13,21,28,29,44,52,53,54,55,56,57,63,64,69,76,77,91,92,97,99,100,101,102,103,104,105,106,107,108,109,110,128,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,79,82,79,79,82,-38,79,-37,-29,-30,-31,-25,-26,-27,-28,-32,-33,-34,-35,-36,79,]),'NOT':([13,21,28,29,44,46,48,52,53,54,55,56,57,62,63,64,65,66,67,69,73,74,75,76,77,79,80,81,91,92,97,99,100,101,102,103,104,105,106,107,108,109,110,124,128,],[-10,-12,-14,-15,-11,65,65,-13,-5,-6,-7,-8,-9,65,80,83,65,65,-60,80,-20,-21,-22,80,83,65,65,65,-38,80,-37,80,-30,80,-25,-26,-27,-28,-32,-33,-34,-35,-36,65,80,]),'AND':([13,21,28,29,44,52,53,54,55,56,57,63,64,69,76,77,91,92,97,99,100,101,102,103,104,105,106,107,108,109,110,128,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,81,84,81,81,84,-38,81,-37,81,-30,-31,-25,-26,-27,-28,-32,-33,-34,-35,-36,81,]),'EQUAL':([13,21,28,29,44,52,53,54,55,56,57,64,77,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,85,85,]),'NOTEQUAL':([13,21,28,29,44,52,53,54,55,56,57,64,77,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,86,86,]),'GREATER':([13,21,28,29,44,52,53,54,55,56,57,64,77,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,87,87,]),'LESS':([13,21,28,29,44,52,53,54,55,56,57,64,77,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,88,88,]),'GREATEREQUAL':([13,21,28,29,44,52,53,54,55,56,57,64,77,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,89,89,]),'LESSEQUAL':([13,21,28,29,44,52,53,54,55,56,57,64,77,],[-10,-12,-14,-15,-11,-13,-5,-6,-7,-8,-9,90,90,]),'ADRESS':([20,28,36,52,68,],[45,-14,45,-13,45,]),'COMMA':([21,28,29,44,52,61,70,114,115,126,],[-12,-14,-15,-11,-13,-19,95,121,-49,121,]),'ELSE':([33,37,98,131,],[-3,-4,118,133,]),'ELSEIF':([33,37,98,131,],[-3,-4,119,119,]),'LITSTRING':([45,49,],[61,61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'scope':([5,78,93,118,125,130,133,],[6,98,112,123,129,131,134,]),'new_scope':([5,78,93,118,125,130,133,],[7,7,7,7,7,7,7,]),'multiple_statements':([8,],[9,]),'expression':([8,9,12,26,38,39,40,41,45,46,48,49,62,65,66,79,80,81,82,83,84,85,86,87,88,89,90,111,124,],[10,35,43,50,53,54,55,56,60,64,64,71,77,64,64,64,64,64,102,103,104,105,106,107,108,109,110,120,64,]),'statement':([8,9,],[11,34,]),'term':([8,9,12,26,38,39,40,41,45,46,48,49,62,65,66,79,80,81,82,83,84,85,86,87,88,89,90,95,111,121,124,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,115,13,115,13,]),'if':([8,9,],[14,14,]),'for':([8,9,],[15,15,]),'while':([8,9,],[16,16,]),'print':([8,9,],[17,17,]),'adress':([8,9,47,],[18,18,67,]),'return':([8,9,],[19,19,]),'instance':([8,9,12,26,38,39,40,41,45,46,47,48,49,62,65,66,79,80,81,82,83,84,85,86,87,88,89,90,95,111,121,124,],[20,36,44,44,44,44,44,44,44,44,68,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'factor':([8,9,12,26,38,39,40,41,45,46,48,49,62,65,66,79,80,81,82,83,84,85,86,87,88,89,90,95,111,121,124,],[21,21,21,21,21,21,21,21,58,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'type':([8,9,12,26,38,39,40,41,45,46,47,48,49,62,65,66,79,80,81,82,83,84,85,86,87,88,89,90,95,111,121,124,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'litstring':([45,49,],[59,70,]),'condition':([46,48,62,65,66,79,80,81,124,],[63,69,76,91,92,99,100,101,128,]),'for_initilizer':([47,],[66,]),'param':([95,121,],[114,126,]),'elseif':([98,131,],[117,132,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> INT MAIN LPAREN RPAREN scope','main',5,'p_start','parser_build.py',32),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','parser_build.py',39),
  ('scope -> new_scope LBRAKETS multiple_statements RBRAKETS','scope',4,'p_scope','parser_build.py',49),
  ('scope -> new_scope LBRAKETS expression RBRAKETS','scope',4,'p_scope','parser_build.py',50),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser_build.py',57),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser_build.py',58),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser_build.py',59),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser_build.py',60),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser_build.py',61),
  ('expression -> term','expression',1,'p_expression','parser_build.py',62),
  ('term -> instance','term',1,'p_term','parser_build.py',71),
  ('term -> factor','term',1,'p_term','parser_build.py',72),
  ('instance -> type ID','instance',2,'p_instance','parser_build.py',84),
  ('instance -> ID','instance',1,'p_instance','parser_build.py',85),
  ('factor -> NUMBER','factor',1,'p_factor','parser_build.py',107),
  ('type -> INT','type',1,'p_type','parser_build.py',113),
  ('type -> FLOAT','type',1,'p_type','parser_build.py',114),
  ('type -> STRING','type',1,'p_type','parser_build.py',115),
  ('litstring -> LITSTRING','litstring',1,'p_litstring','parser_build.py',124),
  ('adress -> instance ADRESS factor SEMICOLON','adress',4,'p_adress','parser_build.py',132),
  ('adress -> instance ADRESS litstring SEMICOLON','adress',4,'p_adress','parser_build.py',133),
  ('adress -> instance ADRESS expression SEMICOLON','adress',4,'p_adress','parser_build.py',134),
  ('return -> RETURN expression SEMICOLON','return',3,'p_return','parser_build.py',162),
  ('return -> RETURN SEMICOLON','return',2,'p_return','parser_build.py',163),
  ('condition -> expression OR expression','condition',3,'p_condition','parser_build.py',171),
  ('condition -> expression NOT expression','condition',3,'p_condition','parser_build.py',172),
  ('condition -> expression AND expression','condition',3,'p_condition','parser_build.py',173),
  ('condition -> expression EQUAL expression','condition',3,'p_condition','parser_build.py',174),
  ('condition -> condition OR condition','condition',3,'p_condition','parser_build.py',175),
  ('condition -> condition NOT condition','condition',3,'p_condition','parser_build.py',176),
  ('condition -> condition AND condition','condition',3,'p_condition','parser_build.py',177),
  ('condition -> expression NOTEQUAL expression','condition',3,'p_condition','parser_build.py',178),
  ('condition -> expression GREATER expression','condition',3,'p_condition','parser_build.py',179),
  ('condition -> expression LESS expression','condition',3,'p_condition','parser_build.py',180),
  ('condition -> expression GREATEREQUAL expression','condition',3,'p_condition','parser_build.py',181),
  ('condition -> expression LESSEQUAL expression','condition',3,'p_condition','parser_build.py',182),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition','parser_build.py',183),
  ('condition -> NOT condition','condition',2,'p_condition','parser_build.py',184),
  ('multiple_statements -> multiple_statements statement','multiple_statements',2,'p_multiple_statements','parser_build.py',192),
  ('multiple_statements -> statement','multiple_statements',1,'p_multiple_statements','parser_build.py',193),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','parser_build.py',203),
  ('statement -> if','statement',1,'p_statement','parser_build.py',204),
  ('statement -> for','statement',1,'p_statement','parser_build.py',205),
  ('statement -> while','statement',1,'p_statement','parser_build.py',206),
  ('statement -> print','statement',1,'p_statement','parser_build.py',207),
  ('statement -> adress','statement',1,'p_statement','parser_build.py',208),
  ('statement -> return','statement',1,'p_statement','parser_build.py',209),
  ('param -> param COMMA param','param',3,'p_param','parser_build.py',217),
  ('param -> term','param',1,'p_param','parser_build.py',218),
  ('if -> IF LPAREN condition RPAREN scope','if',5,'p_if','parser_build.py',228),
  ('if -> IF LPAREN condition RPAREN scope elseif','if',6,'p_if','parser_build.py',229),
  ('if -> IF LPAREN condition RPAREN scope ELSE scope','if',7,'p_if','parser_build.py',230),
  ('elseif -> ELSEIF LPAREN condition RPAREN scope','elseif',5,'p_elseif','parser_build.py',241),
  ('elseif -> ELSEIF LPAREN condition RPAREN scope elseif','elseif',6,'p_elseif','parser_build.py',242),
  ('elseif -> ELSEIF LPAREN condition RPAREN scope ELSE scope','elseif',7,'p_elseif','parser_build.py',243),
  ('print -> PRINT LPAREN litstring RPAREN SEMICOLON','print',5,'p_print','parser_build.py',256),
  ('print -> PRINT LPAREN expression RPAREN SEMICOLON','print',5,'p_print','parser_build.py',257),
  ('print -> PRINT LPAREN litstring COMMA param RPAREN SEMICOLON','print',7,'p_print','parser_build.py',258),
  ('for -> FOR LPAREN for_initilizer condition SEMICOLON expression RPAREN scope','for',8,'p_for','parser_build.py',268),
  ('for_initilizer -> adress','for_initilizer',1,'p_for_initializer','parser_build.py',275),
  ('while -> WHILE LPAREN condition RPAREN scope','while',5,'p_while','parser_build.py',282),
]