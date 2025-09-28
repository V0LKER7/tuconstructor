from Constructor import Constructor
from CopySymbol import CopySymbol
from MoveThrought import MoveThrought
from CopyThrought import CopyThrought

left = MoveThrought(2, 0)
copy = CopyThrought(2,1,1)
right = MoveThrought(2, 1)
constr = Constructor([left, copy, copy, right], 10)
constr.build("test.tu4")