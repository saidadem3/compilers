# Adem, Said
# saa3053
# 2019-10-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Elif_List() :
  def __init__( self, lineNum, stmtList ) :
    self.m_NodeType = 'Elif'

    self.m_LineNum  = lineNum
    self.m_StmtList = stmtList[0][1]

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'ELIF LIST [{len(self.m_StmtList)}]', fp )

    for s in self.m_StmtList :
      s.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#