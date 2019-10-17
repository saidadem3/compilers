# Adem, Said
# saa3053
# 2019-10-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Declaration() :
  def __init__( self, lineNum, typeDecl, identifier, expression ) :
    self.m_NodeType = 'Statement_Decleration'

    self.m_LineNum  = lineNum
    self.m_Type     = typeDecl
    self.m_ID       = identifier
    self.m_Expr     = expression

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (DECLARATION)', fp )

    self.m_Type.dump ( indent +1, fp=fp)        
    self.m_ID.dump( indent +1, fp = fp)
    self.m_Expr.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#