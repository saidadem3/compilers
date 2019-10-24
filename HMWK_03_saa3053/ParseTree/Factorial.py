# Adem, Said
# saa3053
# 2019-10-23
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Factorial() :
  def __init__( self, lineNum, left, op ) :
    self.m_NodeType = 'Factorial'

    self.m_LineNum  = lineNum
    self.m_Op       = op
    self.m_Left    = left

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'UNARY_OP {self.m_Op!r}', fp )

    self.m_Left.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#