# Adem, Said
# saa3053
# 2019-10-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_For() :
  def __init__( self, lineNum, identifier, start, stop, step, stmtList ) :
    self.m_NodeType = 'Statement_While'

    self.m_LineNum  = lineNum
    self.m_Start    = start
    self.m_Stop     = stop
    self.m_Step     = step
    self.m_StmtList = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (FOR)', fp )

    self.m_Start.dump( indent+1, fp = fp )
    self.m_Stop.dump( indent+1, fp = fp )
    # self.m_Step.dump( indent+1, fp = fp )
    self.m_StmtList.dump( indent +1, fp = fp)

#---------#---------#---------#---------#---------#--------#