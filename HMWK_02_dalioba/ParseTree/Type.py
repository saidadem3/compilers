# Adem, Said
# saa3053
# 2019-10-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Type() :
  def __init__( self, lineNum, declType ) :
    self.m_NodeType = 'Type'

    self.m_LineNum  = lineNum
    self.m_Type     = declType

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'TYPE ({self.m_Type!r})', fp )

#---------#---------#---------#---------#---------#--------#
