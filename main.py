#########################################################################################
# importation of modules to be used in the program
import os,sys
import sqlite3
import math
from PySide2 import QtCore
from PySide2.QtCore    import *
from PySide2.QtGui     import *
from PySide2.QtWidgets import *
from PyQt5.QtWidgets   import *

# importation of the Graphical user interface file (GUI fILE)
from interface import *

# importation of custom widgets to be used in the program
from Custom_Widgets.Widgets import  loadJsonStyle

#creating the mainwindow class
class MainWindow(QMainWindow):
    # establishing connection to databse
    db = sqlite3.connect('phy_assistant.db')
    page_id = 1
    
    #creating cursor object for performing database query
    controller = db.cursor()
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handel_buttons()
        
        #Applying JSON Stylesheet
        loadJsonStyle(self, self.ui)
         
        #displaying the window
        self.show()
        
        # #qstackwidgets naviation 
        self.ui.prev.clicked.connect(lambda: self.ui.stackedWidget.slideToPreviousWidget())
        self.ui.nxt.clicked.connect(lambda: self.ui.stackedWidget.slideToNextWidget())

        self.ui.page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        
        # adding animation to the code
        self.ui.stackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
        self.ui.stackedWidget.setTransitionSpeed(2000)
        self.ui.stackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.InSine)
        self.ui.stackedWidget.setSlideTransition(True)
        
    #fucntion for managing myown buttons
    def handel_buttons(self):
        self.ui.calculate_gravity.clicked.connect(self.cal_force_of_gravity)
        self.ui.next_note.clicked.connect(self.next_page)
        self.ui.prev_note.clicked.connect(self.prev_page)
    #function to calculate the force of gravity
    def cal_force_of_gravity(self):
        g,m1,m2,r = 6.67*math.pow(10,-34),0,0,0
        m1 = float(self.ui.gravity_m1.text())
        m2 = float(self.ui.gravity_m2.text())
        r  = float(self.ui.gravity_r.text())
        f = g*m1*m2/r**2
        self.ui.gravity_answer.setText(str(f))
    
      #function to pull all data from database
    def pullData(self):
       sql = "SELECT * FROM Topics where id = %d"%(MainWindow.page_id)
       MainWindow.controller.execute(sql)
       result = MainWindow.controller.fetchone()
       self.ui.note1_label.setText(str(result[1])) 
       self.ui.note1_content.insertPlainText (str(result[3]))
       
    #creting function to connect to next page
    def next_page(self):
        next_id = MainWindow.page_id
        sql = "SELECT * FROM Topics WHERE id=%d"%(next_id)
        MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchone()
        self.ui.note1_label.setText(str(result[1])) 
        self.ui.note1_content.insertPlainText (str(result[1]))
        MainWindow.page_id = MainWindow.page_id + next_id
    
    def prev_page(self):
        prev_id = MainWindow.page_id-1
        sql = "SELECT * FROM Topics WHERE id=%d"%(prev_id)
        MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchone()
        print(result)
        MainWindow.page_id = prev_id
   
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.next_page()
    window.show()
    sys.exit(app.exec_())
        
#executing the application 
if __name__ == "__main__":
    main()
   
    