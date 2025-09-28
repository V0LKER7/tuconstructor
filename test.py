from Constructor import Constructor
from CopySymbol import CopySymbol
from MoveThrought import MoveThrought
from CopyThrought import CopyThrought

left = MoveThrought(1, 1, 0)
# left1 = MoveThrought(left.endState(), 1, 0)

# right = MoveThrought(left.endState(), 5, 1)
copy = CopySymbol(left.endState(), 1, 1)
constr = Constructor([left, copy], 10)
constr.build("test.tu4")