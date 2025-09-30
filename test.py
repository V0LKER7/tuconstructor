from Constructor import Constructor
from CopySymbol import CopySymbol
from CopyThroughtBeforeRight import CopyThroughtBeforeRight
from MoveThrought import MoveThrought
from CopyThrought import CopyThrought
from SliceNumber import SliceNumber
from DeleteWordBeforeSymbol import DeleteWordBeforeSymbol
from Subtraction import Subtraction

left = MoveThrought(2, 0)
copy = CopyThrought(2,1,1)
right = MoveThrought(2, 1)
copy1 = CopyThroughtBeforeRight(1)
slicen = SliceNumber(1,1,1)
sub = Subtraction()
delete = DeleteWordBeforeSymbol()
constr = Constructor([sub], 10)
constr.build("test.tu4")