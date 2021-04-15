from grammarContainer import GrammarContainer
import sys
sys.path.append('../')
from utils_.grammarWrapper import GrammarWrapper
from utils_.domain_objects.mapper import Mapper


def initialise_test():
    mapper = Mapper(GrammarWrapper.createFromString(GrammarContainer.grammarController()))
    mapper.toMatrixBNF()
    return mapper

def test_check_creation_matrix():
    # Matrix creation for production rules
    mapper = initialise_test()
    assert((mapper.mBNF[0] == [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]).all() == True)
    assert((mapper.mBNF[1] == [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]).all() == True)
    assert((mapper.mBNF[2] == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]).all() == True)



