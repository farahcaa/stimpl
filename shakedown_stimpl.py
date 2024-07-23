from stimpl.expression import *
from stimpl.runtime import *

if __name__=='__main__':

    program = Print(Gte(BooleanLiteral(True), BooleanLiteral(True)))
    run_stimpl(program)

