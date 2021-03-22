import sys
sys.path.append('../')
from utils_.grammarWrapper import GrammarWrapper
from utils_.cythonFunctions.mapper import Mapper

grammar = None
mapper = None

def initialise_test():
    grammar = GrammarWrapper("BNF_test_1.bnf") 
    mapper = Mapper(grammar)
    mapper.toMatrixBNF()
    return mapper

def test_grammar():
    mapper = initialise_test()
    assert(mapper.grammar.getVWords()) == ['<inicio>', '<sig>', '<matiz>'] 

