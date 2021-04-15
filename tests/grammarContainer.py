class GrammarContainer:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def grammarMaths():
        return """<f> := (<numbers><basicOperators><f>)
                 <basicOperators> := +|-|*|/|square|root
                 <numbers> := <integer><numbers>|<f>"""

    @staticmethod
    def grammarController():
        return """<begin> := left <next>|right <next>
                  <next> := forward <action>|back <action>|forward <begin>|back <begin>|<next>|<EOF>
                  <action> := hit|down|shoot|<EOF>"""
    