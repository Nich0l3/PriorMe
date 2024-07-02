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
     #col_0 = time
for i in range(len(time)):
            timeWidget = QLabel()
            timeWidget.setText(time[i])
            timeWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            schedule.addWidget(timeWidget,i,0)

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

        self.label.setText("Task")
        self.label_2.setText("Task")
        self.label_3.setText("Task")
        self.label_4.setText("Task")
        self.label_5.setText("Task")
        self.label_6.setText("Task")
        self.label_7.setText("Task")
        self.label_8.setText("Task")
        self.label_9.setText("Task")
        self.label_10.setText("Task")
        self.label_11.setText("Task")

        self.pushButton.setText("PushButton")
        self.pushButton_2.setText("PushButton")
        self.pushButton_12.setText("PushButton")
        self.pushButton_3.setText("PushButton")
        self.pushButton_14.setText("PushButton")
        self.pushButton_6.setText("PushButton")
        self.pushButton_7.setText("PushButton")
        self.pushButton_8.setText("PushButton")
        self.pushButton_9.setText("PushButton")
        self.pushButton_10.setText("PushButton")
        self.pushButton_11.setText("PushButton")
    

app = QApplication([])

window = MainWindow()
window.show()

app.exec()


