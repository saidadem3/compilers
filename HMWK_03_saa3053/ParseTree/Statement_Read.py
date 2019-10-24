# Adem, Said
# saa3053
# 2019-10-23
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Read() :
  def __init__( self, lineNum, idList ) :
    self.m_NodeType = 'Statement_Read'

    self.m_LineNum  = lineNum
    self.m_ID_List = idList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum, f'STATEMENT (READ)', fp )
    
    dumpHeaderLine( indent+1, self.m_LineNum,
      f'ID LIST [{len(self.m_ID_List)}]', fp )

    for s in self.m_ID_List :
      s.dump( indent+2, fp = fp )

#---------#---------#---------#---------#---------#--------#