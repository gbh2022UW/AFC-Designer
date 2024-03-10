import PySimpleGUI as sg
sg.theme("DarkPurple5")

class GUI:
    def __init__(self):
        self.windows = {}
        self.windows["Welcome"] = WelcomeTemplate(self)
        self.windowStack = []
        self.activeWindow = None
    
    def SwitchWindow(self, newWindow, closePrevious = True):
        if not self.activeWindow == None:
            self.windowStack.append(self.activeWindow)
            if closePrevious:
                self.activeWindow.close()
        self.activeWindow = self.windows[newWindow] 
        self.activeWindow.Activate()
        
    def GoBack(self):
        if len(self.windowStack) > 0:
            nextWindow = self.windowStack[-1]
            self.windowStack.pop()
            self.SwitchWindow(nextWindow)

    
    
def WelcomeTemplate(parent):
    layout = [
        [sg.Text("Welcome to AFC Designer!", font = ("Times New Roman", 24))],
        [sg.Button("Load Drones", key = "??TEST??")]
        
    ]
    window = WelcomeWindow(sg.Window("AFC Designer", layout), parent)
    return window

class Window():
    def __init__(self, window, parent):
        self.window = window
        self.parent = parent
        self.eventFunctions = []

    def Activate(self):
        while True:
            event, values = self.window.read()

            self.RunEvents(event, values)

            if event == "??Back??":
                self.parent.GoBack()
            if event == sg.WIN_CLOSED:
                break

    def RunEvents(self, event, values):
        for function in self.eventFunctions:
            function(event, values)

class WelcomeWindow(Window):
    def __init__(self, window, parent):
        self.window = window
        self.parent = parent
        self.eventFunctions = [self.TestButton]

    def TestButton(self, event, values):
        if event == "??TEST??":
            print("GAYYYY")
    