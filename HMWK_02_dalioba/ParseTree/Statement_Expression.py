# Adem, Said
# saa3053
# 2019-10-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Expression() :
  def __init__( self, lineNum, expr ) :
    self.m_NodeType = 'Statement_Expression'

    self.m_LineNum  = lineNum
    self.m_Expr     = expr

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (EXPRESSION)', fp )

    self.m_Expr.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#
