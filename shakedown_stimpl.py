from stimpl.expression import *
from stimpl.runtime import *

if __name__=='__main__':

    program = Print(Ne(BooleanLiteral(True), BooleanLiteral(True)))
    run_stimpl(program)
    print( 1!=1)
