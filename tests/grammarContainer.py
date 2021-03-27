class GrammarContainer:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def grammarMaths():
        return """<f> := (<numeros><operadoresBasicos><f>)
                 <operadoresBasicos> := +|-|*|/|pote|raiz
                 <numeros> := <enteros><numeros>|<f>"""

    @staticmethod
    def grammarController():
        return """<inicio> := izquierda <sig>|derecha <sig>
                  <sig> := adelantar <matiz>|atras <matiz>|adelantar <inicio>|atras <inicio>|<sig>|<EOF>
                  <matiz> := golpear|agacharse|disparar|<EOF>"""
    