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

'''
     #col_0 = 
for i in range(len()):
            Widget = QLabel()
            Widget.setText(time[i])
            Widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            schedule.addWidget(Widget,i,0)

      #col_1 = schedule
for i in range(len(task)):
            taskWidget = QLabel()
            taskWidget.setText(task[i])
            taskWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            schedule.addWidget(taskWidget,i,1)
'''


'''
        self.push_button_0.setText(time[0])
        self.push_button_1.setText(time[1])
        self.push_button_2.setText(time[2])
        self.push_button_3.setText(time[3])
        self.push_button_4.setText(time[4])
        self.push_button_5.setText(time[5])
        self.push_button_6.setText(time[6])
        self.push_button_7.setText(time[7])
        self.push_button_8.setText(time[8])
        self.push_button_9.setText(time[9])
'''

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
        labels = [QLabel(self.page1) for time in times ] 
        [ label.setText(time) for label, time in zip(labels, times) ]
        [ self.label_layout.addWidget(label) for label in labels ]
            
    def add_buttons(self):
        buttons = [QPushButton(self.page1) for task in tasks]
        [ button.setText(task) for button, task in zip(buttons,tasks)]
        [ self.button_layout.addWidget(button) for button in buttons ]


app = QApplication([])

window = MainWindow()
window.show()

app.exec()