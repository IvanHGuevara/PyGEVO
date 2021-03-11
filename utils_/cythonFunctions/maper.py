
def toMatrixBNF(bnf):
    lines=bnf.split("\n")
    vWords =[]
    vDefinitions=[]
    mBNF=[]

    #Carga de vectores con reglas y definiciones
    for line in lines:
        line=line.split(":=")
        word=line[0]
        if(word not in vWords):
            vWords.append(word)
        definitions = line[1]
        definitions = definitions.split("|")
        for definition in definitions:
            if (definition not in vDefinitions):
                vDefinitions.append(definition)
            #definition.split(" ")
    #Carga de matriz
    for line in lines:
        line=line.split(":=")
        word = line[0]
        definitions = line[1]
        definitions=definitions.split("|")
        #print("definicion agregada:" + str(definitions))
        mBNF.append([0]*len(vDefinitions))
        for definition in definitions:
            mBNF[vWords.index(word)][vDefinitions.index(definition)]=1
            #print(vWords.index(word))
            #print(vDefinitions.index(definition))
            #print(word+"->"+definition)
            #print(mBNF)
    print(vWords)
    print(vDefinitions)
    for lBnf in mBNF:
        print(lBnf)
    return vWords,vDefinitions,mBNF

def mapBNF(bnf,individues,inicio,y, x, m ):




    i = inicio
    for individue in individues:

        p = 0
        xPosibles = []
        for bit in m[i]:
            if bit == 1:
                xPosibles.append(x[p])
            p = p + 1
        cDefinitions = len(xPosibles)
        n=individue%cDefinitions
        print(str(individue)+"->rest "+str(n)+"-->"+xPosibles[n])

        xDefinition=xPosibles[n]
        for busqueda in y:
           if busqueda in xDefinition:
                inicio=y.index(busqueda)
                print(str(inicio)+" encontrado "+busqueda)
                xDefinition=xDefinition.replace(busqueda,mapBNF(bnf, individues[1:], inicio,y, x, m))

        return xDefinition

        #xDefinition=xPosibles[n]
        #for busqueda in y:
        #    if busqueda in xDefinition:
        #        print("encontrado "+busqueda)

bnf=\
    "<inicio>:=izquierda <sig>|derecha <sig>|atras\n" \
    "<sig>:=adelantar <motriz>|atras <motriz>\n" \
    "<motriz>:=golpear|agacharse|disparar"
y, x, m = toMatrixBNF(bnf)
print(" ")
penotype=mapBNF(bnf,[10,9,11],0,y, x, m)
print(" ")
print(penotype)
