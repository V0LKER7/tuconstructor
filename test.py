from Constructor import Constructor
from CopySymbol import CopySymbol
from MoveThrought import MoveThrought
from CopyThrought import CopyThrought
from SliceNumber import SliceNumber

left = MoveThrought(1, 0)
copy = CopyThrought(1,0,0)
right = MoveThrought(2, 1)
slicen = SliceNumber(1,1,1)
constr = Constructor([copy], 10)
constr.build("test.tu4")