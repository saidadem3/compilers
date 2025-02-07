# Dalio, Brian A.
# dalioba
# 2019-06-07
#---------#---------#---------#---------#---------#--------#
# A simple calculator with variables.

#---------#---------#---------#---------#---------#--------#
# Lexical analysis section.

tokens = (
  'INTEGER', 'REAL', 'ID',
  'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
  'LPAREN', 'RPAREN',
  )

# Tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ID      = r'[a-z_][a-z0-9_]*'

def t_REAL( t ) :
  r'(\d+[eE][-+]?\d+)|((\d*((\.\d)|(\d\,))\d*)([eE][-+]?\d+)?)'
  t.value = float(t.value)
  return t

def t_INTEGER( t ) :
  r'\d+'
  t.value = int(t.value)
  return t

# Ignored characters
t_ignore = " \t"

def t_newline( t ) :
  r'\n+'
  t.lexer.lineno += t.value.count("\n")

def t_error( t ) :
  print( "Illegal character '%s'" % t.value[0] )
  t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

#---------#---------#---------#---------#---------#--------#
# Syntactic section.

# Precedence rules for the arithmetic operators
precedence = (
  ( 'left',  'PLUS', 'MINUS' ),
  ( 'left',  'TIMES', 'DIVIDE' ),
  ( 'right', 'UMINUS' ),
  )

# Dictionary of names (for storing variables)
names = dict()

def p_statement_assign( p ) :
  'statement : ID ASSIGN expression'
  names[ p[1] ] = p[3]

def p_statement_expr( p ) :
  'statement : expression'
  print( p[1] )

def p_expression_binop( p ) :
  '''expression : expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression'''
  if   p[2] == '+' : p[0] = p[1] + p[3]
  elif p[2] == '-' : p[0] = p[1] - p[3]
  elif p[2] == '*' : p[0] = p[1] * p[3]
  elif p[2] == '/' : p[0] = p[1] / p[3]

def p_expression_unop( p ) :
  'expression : MINUS expression %prec UMINUS'
  p[0] = -p[2]

def p_expression_group( p ) :
  'expression : LPAREN expression RPAREN'
  p[0] = p[2]

def p_expression_number( p ) :
  '''expression : INTEGER
                | REAL'''
  p[0] = p[1]

def p_expression_name( p ) :
  'expression : ID'

  try:
    p[0] = names[p[1]]

  except LookupError:
    print( "Undefined name '%s'" % p[1] )
    p[0] = 0

def p_error( p ) :
  print( "Syntax error at '%s'" % p.value )

# Build the parser
import ply.yacc as yacc
yacc.yacc()

#---------#---------#---------#---------#---------#--------#
# Get input and pass it to the parser (which passes it to
# the lexer for scanning) for processing.

while True :
  try :
    s = input( 'calc > ' )

  except EOFError :
    break

  yacc.parse( s )

print()

#---------#---------#---------#---------#---------#--------#
