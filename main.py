from appJar import gui

class Character:
    def __init__(self, name, hp, maxHp):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp

class Item:
    def __init__(self, name, properties):
        pass

class Inventory:
    items = []
    index = 0
    def __init__(self):
        pass

    def getItems():
        return self.items

    def setItems():
        self.items = items

    def getItem(item_name):
        for item in items:
            if item_name == item["name"]:
                return item
            else:
                error("No {} found".format(item_name))

    def addItem(item):
        item["index"] = self.index
        self.index += 1
        items.append(item)

    def removeItem(item):
        pass

#Utilities
def error(input_text):
    print(input_text)

#GUI stuff

def parseInput(button):
    a.setTextArea("Out", (a.getEntry("In") + "\n"))
    a.setEntry("In", "")

def useItems(button):
    pass

def combineItems(button):
    pass

def dropItems(button):
    pass

##GUIConfig

a = gui()
a.setTitle("Title")
a.setSize(600,450)

#Tabs
a.startTabbedFrame("TabbedFrame")

##IO
a.startTab("IOTab")
a.setStretch("both")
a.setSticky("news")
a.addScrolledTextArea("Out")

a.setSticky("nw")
a.setStretch("column")
a.addLabel("StatusBar", "Hello World!")
a.setSticky("new")
a.addEntry("In")
a.setEntrySubmitFunction("In", parseInput)
a.stopTab()

##Inv
a.startTab("InventoryTab")
a.setStretch("both")
a.setSticky("news")
a.addListBox("Inv", "", 0, 0, 1, 6)
a.setStretch("none")
a.addButton("Use", useItems, 0, 1)
a.addButton("Combine", combineItems, 1, 1)
a.addButton("Drop", dropItems, 2, 1)
a.stopTab()

##Char
a.startTab("CharacterTab")
a.addLabelOptionBox("Head", ["item1", "item2"])
a.stopTab()

##Misc
a.stopTabbedFrame()

##Setup
c = Character("TestName", 10, 10)

a.go()
