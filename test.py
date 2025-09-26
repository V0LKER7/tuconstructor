from Constructor import Constructor
from MoveThrought import MoveThrought
from CopyThrought import CopyThrought

left = MoveThrought(1, 5, 0)
right = MoveThrought(left.endState(), 5, 1)
# copy = CopyThrought(left.endState(), 1, 1, 1)
constr = Constructor([left, right], 10)
constr.build("test.tu4")