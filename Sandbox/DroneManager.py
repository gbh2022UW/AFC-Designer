import DataManager as DM
import os
import csv

dataTemplate = {
    "weight" #weight of the entire drone in pounds-force
    "ha" #hover acceleration in feet per second squared
    "length" #length of the drone (one propeller to the closest one) in feet
}

class Drone:
    def __init__(self, name, data = None):
        self.name = name
        
        self.savePath = os.path.join(DM.dronePath, name)
        self.saveFile = os.path.join(self.savePath, "saveData.csv")
        if not os.path.exists(self.savePath):
            os.mkdir(self.savePath)
        if not os.path.exists(self.saveFile):
            self.saveData = dict.fromkeys(dataTemplate)
            for dataValue in data:
                self.saveData[dataValue] = data[dataValue]
            DM.masterLog.addLine("Initialized " + name + " drone with the following values: " + str(self.saveData))
        else:
            self.saveData = dict.fromkeys(dataTemplate)
            saveCSV = open(self.saveFile, "r")
            saveReader = csv.DictReader(saveCSV)
            for row in saveReader:
                for saveValue in row:
                    self.saveData[saveValue] = row[saveValue]
            
            DM.masterLog.addLine("Loaded " + name + " drone with the following values: " + str(self.saveData))


    def Save(self):
        saveCSV = open(self.saveFile, "w")
        fieldnames = dict.fromkeys(self.saveData)
        saveWriter = csv.DictWriter(saveCSV, fieldnames)
        saveWriter.writeheader()
        saveWriter.writerow(self.saveData)
        DM.masterLog.addLine("Saved " + self.name + " drone with the following values: " + str(self.saveData))


        
    
