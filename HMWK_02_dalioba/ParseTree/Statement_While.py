# Adem, Said
# saa3053
# 2019-10-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_While() :
  def __init__( self, lineNum, expr, stmtList ) :
    self.m_NodeType = 'Statement_While'

    self.m_LineNum  = lineNum
    self.m_Expr     = expr
    self.m_StmtList = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (WHILE)', fp )

    self.m_Expr.dump( indent+1, fp = fp )
    self.m_StmtList.dump( indent +1, fp = fp)

#---------#---------#---------#---------#---------#--------#