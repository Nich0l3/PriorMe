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
def retranslateUi(self):
        self.setWindowTitle("MainWindow")

        self.option1.setText('schedule')

        self.label0.setText(task[0])
        self.label1.setText(task[1])
        self.label2.setText(task[2])
        self.label3.setText(task[3])
        self.label4.setText(task[4])
        self.label5.setText(task[5])
        self.label6.setText(task[6])
        self.label7.setText(task[7])
        self.label8.setText(task[8])
        self.label9.setText(task[9])

        self.pushButton0.setText(time[0])
        self.pushButton1.setText(time[1])
        self.pushButton2.setText(time[2])
        self.pushButton3.setText(time[3])
        self.pushButton4.setText(time[4])
        self.pushButton5.setText(time[5])
        self.pushButton6.setText(time[6])
        self.pushButton7.setText(time[7])
        self.pushButton8.setText(time[8])
        self.pushButton9.setText(time[9])
'''

class MainWindow(QMainWindow, Ui_MainWindow,Ui_ediPanel):
    
    def __init__(self) :
        super().__init__()
        self.setupUiGui(self)

        self.retranslateUiGui()

        self.option1.clicked.connect(self.showSchedule)
        

        self.pushButton0.clicked.connect(self.action(self.label0))
        self.pushButton1.clicked.connect(self.action(self.label1))
        self.pushButton2.clicked.connect(self.action(self.label2))
        self.pushButton3.clicked.connect(self.action(self.label3))
        self.pushButton4.clicked.connect(self.action(self.label4))
        self.pushButton5.clicked.connect(self.action(self.label5))
        self.pushButton6.clicked.connect(self.action(self.label6))
        self.pushButton7.clicked.connect(self.action(self.label7))
        self.pushButton8.clicked.connect(self.action(self.label8))
        self.pushButton9.clicked.connect(self.action(self.label9))


    def retranslateUiGui(self):
        self.setWindowTitle("MainWindow")

        self.option1.setText('schedule')

        self.label0.setText(task[0])
        self.label1.setText(task[1])
        self.label2.setText(task[2])
        self.label3.setText(task[3])
        self.label4.setText(task[4])
        self.label5.setText(task[5])
        self.label6.setText(task[6])
        self.label7.setText(task[7])
        self.label8.setText(task[8])
        self.label9.setText(task[9])

        self.pushButton0.setText(time[0])
        self.pushButton1.setText(time[1])
        self.pushButton2.setText(time[2])
        self.pushButton3.setText(time[3])
        self.pushButton4.setText(time[4])
        self.pushButton5.setText(time[5])
        self.pushButton6.setText(time[6])
        self.pushButton7.setText(time[7])
        self.pushButton8.setText(time[8])
        self.pushButton9.setText(time[9])

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

        

app = QApplication([])

window = MainWindow()
window.show()

app.exec()


