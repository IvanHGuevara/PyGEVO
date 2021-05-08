from .grammarContainer import GrammarContainer
from ..core.domain.grammarWrapper import GrammarWrapper

def initialise_test():
    return GrammarWrapper.createFromString(GrammarContainer.grammarController()) 

def test_grammarMethods():
    grammar = initialise_test()
    assert(grammar.getVWords()) == ['<inicio>', '<sig>', '<matiz>']
    assert(grammar.getProductionRules()) == ['izquierda <sig>', 'derecha <sig>', 'adelantar <matiz>', 'atras <matiz>', 'adelantar <inicio>', 'atras <inicio>', '<sig>', '<EOF>', 'golpear', 'agacharse', 'disparar', '<EOF>'] 
    assert(grammar.getProductionRulesForPosition(0)) == ['izquierda <sig>', 'derecha <sig>']

