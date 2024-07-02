import json
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)
            
from PySide6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

#        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(400,300))

        pagelayout = QHBoxLayout(self)

# adding buttons 
        button_layout = QVBoxLayout()

        btn = QPushButton("schedule")
        btn.pressed.connect(self.activate_tab_1)
#        btn.setFlat(True)
        button_layout.addWidget(btn)

        btn = QPushButton("timer")
        btn.pressed.connect(self.activate_tab_2)
#        btn.setFlat(True)
        button_layout.addWidget(btn)

        pagelayout.addLayout(button_layout)
 

# adding layouts corresponding to button clicks
  
        self.option_layout = QStackedLayout()

  # adding two layouts in stack layout  
        schedule = QGridLayout()
        timer = QVBoxLayout()

  #schedule
      
        data_file = open('data.json')
        data = json.load(data_file)

        time=[]
        task=[]

        for key,value in data.items(): # convert into dict items
            time.append(key)
            task.append(value)

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

        schedule_widget = QWidget()
        schedule_widget.setLayout(schedule)

        self.option_layout.addWidget(schedule_widget)


  #timer
  
        pagelayout.addLayout(self.option_layout)

        pagewidget = QWidget()   
        pagewidget.setLayout(pagelayout)
        self.setCentralWidget(pagewidget)

    def activate_tab_1(self):
        self.option_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.option_layout.setCurrentIndex(1)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()


    
