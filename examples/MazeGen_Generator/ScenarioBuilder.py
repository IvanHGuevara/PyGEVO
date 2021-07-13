class ScenarioBuilder:

    def __init__(self) -> None:
        self.figureCounter = 0

    def returnAccordingScore(self, width):
        if width > 500:
            raise Exception("Invalid scenario")
        else:
            return 1

    def addHeader(self):
        self.stringBuild = "StackLayout:" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "canvas:" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "points: 100,100,100,1150,1500,1150,1500,100,100,100" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "points: 150,150,175,175,200,150" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "width: 5" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "close: True" + "\n"

    def createEShape(self, width, coordinateX, coordinateY, coordinateZ, coordinateK, checkSize = False):
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateZ) + ","  + str(coordinateK) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(round((coordinateX + coordinateK)/2)) + ","  + str(coordinateX) +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(round((coordinateX + coordinateK)/2)) + ","  + str(round((coordinateX + coordinateK)/2)) + ","  + str(round((coordinateX + coordinateK)/2)) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateK) + ","  + str(round((coordinateX + coordinateK)/2)) + ","  + str(coordinateK) +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.figureCounter = self.figureCounter + 1
        return self.figureCounter

    def createLShape(self, width, coordinateX, coordinateY, checkSize = False):  
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateX) + ","  + str(coordinateY+50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateX+50) + ","  + str(coordinateY) +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.figureCounter = self.figureCounter + 1
        return self.figureCounter
    
    def createSquare(self, width, coordinateX, coordinateY, checkSize = False):
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size:" + str(width) + ","  + str(width) + "\n"
        self.figureCounter = self.figureCounter + # self.returnAccordingScore(width)
        return self.figureCounter

    def createTriangle(self, width, coordinateX, coordinateY, checkSize = False):  
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba: 1, 1, 1, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateX+50) + ","  + str(coordinateY) + "," + str(coordinateX+50) + "," + str(coordinateY+50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "close: " + "True" + "\n"
        self.figureCounter = self.figureCounter + 1
        return self.figureCounter