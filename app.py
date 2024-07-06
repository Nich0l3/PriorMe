from gui import *
from edit import *
import json


data_file = open('data.json')
data = json.load(data_file)
data_dict = data.items()

time=[]
task=[]

for key,value in data_dict: # convert into dict items
     time.append(key)
     task.append(value)

print(task)

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


class MainWindow(QMainWindow, Ui_MainWindow,Ui_ediPanel):
    
    def __init__(self) :
        super().__init__()
        self.setupUiGui(self)
        self.retranslateUiGui()

        self.add_labels()

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
        for t in time:
            label = QLabel()
            label.setText(t)
            self.label_layout.addWidget(label)
            

app = QApplication([])

window = MainWindow()
window.show()

app.exec()