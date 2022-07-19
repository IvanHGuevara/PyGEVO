import itertools

class RealScenarioBuilder:

    def __init__(self) -> None:
        self.stringBuild = ''
        self.components = []

    def returnAccordingScore(self, width):
        if width > 300:
            raise Exception("Invalid scenario")
        else:
            return 1

    def addHeader(self):
        header = Header()
        self.components.append(header)

    def createProductionLine(self, coordinateX):
        productionLine = ProductionLine(coordinateX)
        self.components.append(productionLine)

    def createHorizontalWall(self, coordinateX, coordinateY):  
        horizontalWall = HorizontalWall(coordinateX, coordinateY)
        self.components.append(horizontalWall)
    
    def createVerticalWall(self, coordinateX, coordinateY):  
        verticalWall = VerticalWall(coordinateX, coordinateY)
        self.components.append(verticalWall)
    
    def createCobot(self, coordinateX):
        cobot = Cobot(coordinateX)
        self.components.append(cobot)
    
    def createRouter(self, coordinateX):
        router = Router(coordinateX)
        self.components.append(router)

    def calculateFitness(self):
        collidingComponents = 0
        componentList = list(itertools.combinations(self.components, 2))
        for component1, component2 in componentList:
            if component1.collideWith(component2):
                #print("El componente es: ", component1)
                #print("El minX es:", component1.minX)
                #print("El maxX es:", component1.maxX)
                #print("El minY es:", component1.minX)
                #print("El maxX es:", component1.maxX)
                #print("El componente es: ", component2)
                #print("El minX es:", component1.minX)
                #print("El maxX es:", component1.maxX)
                #print(component2.minX)
                #print(component2.maxX)
                collidingComponents = collidingComponents + 1
        #print("Cantidad componentes: ", len(self.components))
        #print("Cantidad colliding", collidingComponents)
        #print(self.getStringBuild())
        return len(self.components) - collidingComponents

    def getStringBuild(self):
        for component in self.components:
            self.stringBuild = self.stringBuild + component.stringBuild
            self.stringBuild = self.stringBuild + '\n'
        return self.stringBuild

class ProductionLine:
    
    def __init__(self, coordinateX) -> None:
        self.stringBuild = ''
        self.minX = int(coordinateX)
        self.maxX = int(coordinateX) + 800
        self.minY = int(coordinateX) - 50
        self.maxY = int(coordinateX)
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "rgba: 0, 0, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateX) + ","  + str(coordinateX) + ","  + str(int(coordinateX) - 50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateX) + ","  + str(int(coordinateX) + 800) + ","  + str(coordinateX) +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(int(coordinateX)+ 800)  + ","  + str(coordinateX) + ","  + str(int(coordinateX) + 800) + ","  + str(int(coordinateX) - 50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5"

    def collideWith(self, element):
        return ((element.minX < self.maxX and element.minX > self.minX) or (element.maxX < self.maxX and element.maxX > self.minX) or (element.minY < self.maxY and element.minY > self.minY) or (element.maxY < self.maxY and element.maxY > self.minY))


class HorizontalWall:

    def __init__(self, coordinateX, coordinateY) -> None:
        self.stringBuild = ''
        self.minX = int(coordinateX)
        self.maxX = int(coordinateX) + 350
        self.minY = int(coordinateY)
        self.maxY = int(coordinateY) + 50
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+50) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+100) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+150) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+200) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+250) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+300) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(int(coordinateX)+350) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50"
    
    def collideWith(self, element):
        return ((element.minX < self.maxX and element.minX > self.minX) or (element.maxX < self.maxX and element.maxX > self.minX) or (element.minY < self.maxY and element.minY > self.minY) or (element.maxY < self.maxY and element.maxY > self.minY))

class VerticalWall:

    def __init__(self, coordinateX, coordinateY) -> None:
        self.stringBuild = ''
        self.minX = coordinateX
        self.maxX = coordinateX + 50
        self.minY = coordinateY
        self.maxY = coordinateY + 350
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+100) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+150) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+200) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+250) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+300) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(int(coordinateY)+350) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size: 50, 50"
   
    def collideWith(self, element):
        return ((element.minX < self.maxX and element.minX > self.minX) or (element.maxX < self.maxX and element.maxX > self.minX) or (element.minY < self.maxY and element.minY > self.minY) or (element.maxY < self.maxY and element.maxY > self.minY))

class Cobot: 

    def __init__(self, coordinateX) -> None:
        self.stringBuild = ''
        self.minX = coordinateX
        self.maxX = coordinateX + 50
        self.minY = coordinateX
        self.maxY = coordinateX + 25
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points:" + str(coordinateX) + "," + str(coordinateX) + "," + str(int(coordinateX) + 25) + "," + str(int(coordinateX) + 25) + "," + str(int(coordinateX) + 50) + "," + str(coordinateX)  + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "close: True"

    def collideWith(self, element):
        return ((element.minX < self.maxX and element.minX > self.minX) or (element.maxX < self.maxX and element.maxX > self.minX) or (element.minY < self.maxY and element.minY > self.minY) or (element.maxY < self.maxY and element.maxY > self.minY))

class Router:

    def __init__(self, coordinateX) -> None:
        self.stringBuild = ''
        self.minX = coordinateX
        self.maxX = coordinateX + 50
        self.minY = coordinateX
        self.maxY = coordinateX + 25
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 0, 0, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points:" + str(coordinateX) + "," + str(coordinateX) + "," + str(int(coordinateX) + 25) + "," + str(int(coordinateX) + 25) + "," + str(int(coordinateX) + 50) + "," + str(coordinateX)  + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5"

    def collideWith(self, element):
        return ((element.minX < self.maxX and element.minX > self.minX) or (element.maxX < self.maxX and element.maxX > self.minX) or (element.minY < self.maxY and element.minY > self.minY) or (element.maxY < self.maxY and element.maxY > self.minY))

class Header:

    def __init__(self) -> None:
        self.stringBuild = ''
        self.minX = 100
        self.maxX = 1500
        self.minY = 100
        self.maxY = 1500
        self.stringBuild = "StackLayout:" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "canvas:" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: 100,100,100,1150,1500,1150,1500,100,100,100" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: 150,150,175,175,200,150" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "close: True"

    def collideWith(self, element):
        return ((element.minX < self.minX and element.maxX > self.minX) or (element.maxX > self.maxX and element.minX < self.maxX) or (element.minY < self.minY and element.maxY > self.minY) or (element.maxY > self.maxY and element.minY < self.maxY))