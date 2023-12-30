from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from graphs import * 


#generate_lung() 
# Load the UI file
app = QApplication([])
windows = loadUi("interface.ui")
#modify the input level
level="low" 
def on_textchanged(index):
                print(index)
                global level
                #level=text
                level = windows.level.itemText(index) 
windows.level.currentIndexChanged.connect(on_textchanged)  

#connect buttons to the graphs
windows.chronic_lung.clicked.connect(lambda: generate_lung(level) ) 
windows.coughing_blood.clicked.connect(lambda: generate_blood(level) ) 
windows.breath_shortness.clicked.connect(lambda: generate_breath(level) ) 
windows.chest_pain.clicked.connect(lambda: generate_chest(level) ) 
windows.obesity.clicked.connect(lambda: generate_obesity(level) ) 

# Connect the buttons to their respective functions
windows.exit.clicked.connect(app.quit)

windows.show()
app.exec_() 
