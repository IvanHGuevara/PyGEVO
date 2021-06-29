class ScenarioBuilder:

    def __init__(self) -> None:
        self.stringBuild = "FloatLayout:" + "\n"
        self.stringBuild = self.stringBuild + "\t" + "canvas:" + "\n"
        self.figureCounter = 0

    def createEShape(self, width, coordinateX, coordinateY, coordinateZ, coordinateK):
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba:" + str(coordinateX) + "," + str(coordinateY) + "," +  str(coordinateZ) + "," +  str(coordinateK) +  "\n"
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

    def createLShape(self, width, coordinateX, coordinateY):  
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba:" + "0, 1" + "," + str(coordinateX) + "," + str(coordinateY)  +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateX) + ","  + str(coordinateY+50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateX+50) + ","  + str(coordinateY) +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.figureCounter = self.figureCounter + 1
        return self.figureCounter
    
    def createSquare(self, width, coordinateX, coordinateY):
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba:" + str(coordinateX) + "," + str(coordinateY) + "," +  "0, 1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Rectangle: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "pos:" + str(coordinateX) + ","  + str(coordinateY) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "size:" + str(width) + ","  + str(width) + "\n"
        self.figureCounter = self.figureCounter + 1
        return self.figureCounter

    def createTriangle(self, width, coordinateX, coordinateY):  
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Color: " + "\n" 
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" +"rgba:" + str(coordinateX) + "," + "0" + "," + str(coordinateY) + "," +  "1" +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "Line: " +  "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "points: " + str(coordinateX) + ","  + str(coordinateY) + ","  + str(coordinateX+50) + ","  + str(coordinateY) + "," + str(coordinateX+50) + "," + str(coordinateY+50) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "width: " + str(width) + "\n"
        self.stringBuild = self.stringBuild + "\t" + "\t" + "\t" + "close: " + "True" + "\n"
        self.figureCounter = self.figureCounter + 1
        return self.figureCounter