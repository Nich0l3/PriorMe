from gui import *
import json


data_file = open('data.json')
data = json.load(data_file)

time=[]
task=[]

for key,value in data.items(): # convert into dict items
     time.append(key)
     task.append(value)

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

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.retranslateUi()


    def retranslateUi(self):
        self.setWindowTitle("MainWindow")

        self.option1.setText('schedule')
        self.option1.clicked.connect(self.showSchedule)

        self.label.setText(task[0])
        self.label_2.setText(task[1])
        self.label_3.setText(task[2])
        self.label_4.setText(task[3])
        self.label_5.setText(task[4])
        self.label_6.setText(task[5])
        self.label_7.setText(task[6])
        self.label_8.setText(task[7])
        self.label_9.setText(task[8])
        self.label_10.setText(task[9])

        self.pushButton.setText(time[0])
        self.pushButton_2.setText(time[1])
        self.pushButton_3.setText(time[2])
        self.pushButton_4.setText(time[3])
        self.pushButton_5.setText(time[4])
        self.pushButton_6.setText(time[5])
        self.pushButton_7.setText(time[6])
        self.pushButton_8.setText(time[7])
        self.pushButton_9.setText(time[8])
        self.pushButton_10.setText(time[9])


    def showSchedule(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()


