from datetime import datetime

dt = datetime.now()

topTemplate = "-----Welcome to AFC Designer app created by the AFC Team-----"
bottomTemplate = "----Created on " + str(dt) + "-----"
indentTemplate = "   "

class Log:
    def __init__(self, number):
        self.number = number
        self.masterString = ""
        self.sections = None

    def blank(self, numLines = 1):
        for i in range(0, numLines):
            self.masterString += "\n"

    def addLine(self, line):
        self.masterString += line + "\n"

    def compile(self):
        return topTemplate + "\n\n" + self.masterString + "\n" + bottomTemplate

class Section:
    def __init__(self):
        self.masterString = None
        self.indent = indentTemplate
        self.sections = None
    
    
    
        

    
    