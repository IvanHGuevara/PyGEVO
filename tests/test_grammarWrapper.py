
from .grammarContainer import GrammarContainer
from ..core.domain.grammarWrapper import GrammarWrapper


def initialise_test():
    return GrammarWrapper.createFromString(GrammarContainer.grammarController()) 

def test_grammarMethods():
    grammar = initialise_test()
    assert(grammar.getVWords()) == ['<begin>', '<next>', '<action>']
    assert(grammar.getProductionRules()) == ['left <next>', 'right <next>', 'forward <action>', 'back <action>', 'forward <begin>', 'back <begin>', '<next>', '<EOF>', 'hit', 'down', 'shoot', '<EOF>'] 
    assert(grammar.getProductionRulesForPosition(0)) == ['left <next>', 'right <next>']

