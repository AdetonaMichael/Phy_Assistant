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
    db = sqlite3.connect('phy_assistant2.db')
    page_id = 1
    
    #creating cursor object for performing database query
    controller = db.cursor()
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handel_buttons()
        self.navigate()
        
        #Applying JSON Stylesheet
        loadJsonStyle(self, self.ui)
         
        #displaying the window
        self.show()
        
        # #qstackwidgets naviation 
        self.ui.prev.clicked.connect(lambda: self.ui.stackedWidget.slideToPreviousWidget())
        self.ui.nxt.clicked.connect(lambda: self.ui.stackedWidget.slideToNextWidget())

        self.ui.formula_list_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.formula_list_page))
        self.ui.solved_examples_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solved_examples_page))
        
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
        self.ui.update_update_btn.clicked.connect(self.update)
        
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
       self.ui.note_content.insertPlainText (str(result[2]))
       
    #creting function to connect to next page
    def next_page(self):
        next_id = MainWindow.page_id
        sql = "SELECT * FROM Topics WHERE id=%d"%(next_id)
        MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchone()
        self.ui.single_count_btn.setText(str(result[0]))
        self.ui.note1_label.setText(str(result[1])) 
        self.ui.note_content.setText (str(result[2]))
        self.ui.formula_list_content.setText(str(result[4]))
        self.ui.solved_examples_content.setText(str(result[3]))
        MainWindow.page_id = MainWindow.page_id + next_id
        print(("the length of the result is: {}".format(len(result))))
    
    def prev_page(self):
        prev_id = MainWindow.page_id-1
        sql = "SELECT * FROM Topics WHERE id=%d"%(prev_id)
        MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchone()
        print(result)
        MainWindow.page_id = prev_id
    
    def get_count(self):
        sql = "SELECT COUNT(*) FROM Topics"
        MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchall() 
        return result
    
    def navigate(self):
        sql = 'SELECT * FROM Topics'
        result = MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchone()
        
        #defining and the widget in the textbox interface
        self.ui.update_count_label.setText(str(result[0]))
        self.ui.update_note_title.setText(str(result[1]))
        self.ui.update_note_content.setText(str(result[2]))
        self.ui.update_solved_examples_content.setText(str(result[3]))
        self.ui.update_formula_list_content.setText(str(result[4]))

    
    def update(self):
        #defining and the widget in the textbox interface
        id = int(self.ui.update_count_label.text())
        title_ = str(self.ui.update_note_title.text())
        content_ = str(self.ui.update_note_content.acceptRichText())
        examples_  = str(self.ui.update_solved_examples_content.acceptRichText())
        formula_list_  = str(self.ui.update_formula_list_content.acceptRichText())
        
        row = (title_, content_, examples_, formula_list_, id)
        sql = '''UPDATE Topics SET title=?, content=?, examples=?, formula_list=? where id = ?'''
        MainWindow.controller.execute(sql,row)
        MainWindow.db.commit()
        
   
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.get_count()
    window.show()
    sys.exit(app.exec_())
        
#executing the application 
if __name__ == "__main__":
    main()
   
    