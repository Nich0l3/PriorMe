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
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Task", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    

app = QApplication([])

window = MainWindow()
window.show()

app.exec()


