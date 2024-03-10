import os
import DataManager as DM
import getpass
import DroneManager as DRM
import LogManager as LM
import csv
import GUI

username = getpass.getuser()

DM.afcPath = os.path.join(os.path.join(r"C:\Users", username), "AFC Save Files")
if not os.path.exists(DM.afcPath):
    os.mkdir(DM.afcPath)

DM.designerPath = os.path.join(DM.afcPath, "AFC Designer")
if not os.path.exists(DM.designerPath):
    os.mkdir(DM.designerPath)

DM.dataPath = os.path.join(DM.designerPath, "data.csv")
if not os.path.exists(DM.dataPath):
    DM.data = DM.dataDefaults
    dataCSV = open(DM.dataPath, "w")
    fieldnames = dict.fromkeys(DM.data)
    dataWriter = csv.DictWriter(dataCSV, fieldnames)
    dataWriter.writeheader()
    dataWriter.writerow(DM.data)
else:
    dataCSV = open(DM.dataPath, "r")
    dataReader = csv.DictReader(dataCSV)
    for row in dataReader:
        for dataValue in row:
            DM.data[dataValue] = row[dataValue]

DM.logPath = os.path.join(DM.designerPath, "logs")
if not os.path.exists(DM.logPath):
    os.mkdir(DM.logPath)

DM.data["logNumber"] = len(os.listdir(DM.logPath)) + 1
DM.masterLog = LM.Log(DM.data["logNumber"])

DM.dronePath = os.path.join(DM.designerPath, "Drone Save Files")
if not os.path.exists(DM.dronePath):
    os.mkdir(DM.dronePath)
else:
    droneNames = os.listdir(DM.dronePath)
    for droneName in droneNames:
        if os.path.isdir(os.path.join(DM.dronePath, droneName)):
            DM.drones.append(DRM.Drone(droneName))
        else:
            DM.masterLog.addLine("Could not recognize " + droneName + " as a drone save file")


gui = GUI.GUI()
gui.SwitchWindow("Welcome")

'''DM.drones.append(DRM.Drone("New Drone 100", data = {
    "hv" : 69
}))'''


dataCSV = open(DM.dataPath, "w")
fieldnames = dict.fromkeys(DM.data)
dataWriter = csv.DictWriter(dataCSV, fieldnames)
dataWriter.writeheader()
dataWriter.writerow(DM.data)

for drone in DM.drones:
    drone.Save()

finalLog = DM.masterLog.compile()
logName = "log" + str(DM.masterLog.number) + ".txt"
logFile = open(os.path.join(DM.logPath, logName), "w")
logFile.write(finalLog)
logFile.close()


