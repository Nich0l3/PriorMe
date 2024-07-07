from gui import *
from edit import *
import json

data_file = open('data.json')
data = json.load(data_file)
data_dict = data.items()

times=[]
tasks=[]

for key,value in data_dict: # convert into dict items
     times.append(key)
     tasks.append(value)

print(tasks)

labels=[]
buttons=[]

class MainWindow(QMainWindow, Ui_MainWindow,Ui_ediPanel):
    
    def __init__(self) :
        super().__init__()
        self.setupUiGui(self)
        self.retranslateUiGui()

        self.add_labels()
        self.add_buttons()
        self.page1.setPalette(self.palette1)

        self.option1.clicked.connect(self.showSchedule)
    

    def retranslateUiGui(self):
        self.setWindowTitle("MainWindow")
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.option1.setText('schedule')

    def showSchedule(self):
        print('show schedule')
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def action(self, QLabel):
        currentTime = QLabel.text() 
        time = QTime()
        print(time.currentTime())

    def add_labels(self):
        labels = [QLabel() for _ in times]  
        for label, time in zip(labels, times):  
            label.setText(time)
            label.setAlignment(Qt.AlignCenter)
            self.label_layout.addWidget(label) 
        
        #self.label_layout.addStretch()


    def add_buttons(self):
        buttons = [QPushButton(parent=self.page1, text=task) for task in tasks]
        for button, task in zip(buttons, tasks):  
            self.button_layout.addWidget(button) 
            
        #self.button_layout.addStretch()

        


app = QApplication([])

window = MainWindow()
window.show()

app.exec()