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
from win10toast import ToastNotifier
from PySide2.QtWebEngineWidgets import *

# importation of the Graphical user interface file (GUI fILE)
from interface import *

# importation of custom widgets to be used in the program
from Custom_Widgets.Widgets import  loadJsonStyle
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#creating the mainwindow class
class MainWindow(QMainWindow):
    # establishing connection to databse
    db = sqlite3.connect(resource_path('phy_assistant2.db'))
    page_id = 0.
    
    #creating cursor object for performing database query
    controller = db.cursor()

    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handel_buttons()
        self.navigate()
        self.get_count()
        self.toast = ToastNotifier()
        
        #Applying JSON Stylesheet
        loadJsonStyle(self, self.ui)
         
        #displaying the window
        self.show()
        
        # #qstackwidgets naviation 
        self.ui.prev.clicked.connect(lambda: self.ui.stackedWidget.slideToPreviousWidget())
        self.ui.nxt.clicked.connect(lambda: self.ui.stackedWidget.slideToNextWidget())

        self.ui.formula_list_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.formula_list_page))
        self.ui.solved_examples_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solved_examples_page))
        self.ui.main_note_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        
        # adding animation to the code
        self.ui.stackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
        self.ui.stackedWidget.setTransitionSpeed(2000)
        self.ui.stackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.InSine)
        self.ui.stackedWidget.setSlideTransition(True)
        
    #fucntion for managing myown buttons
    def handel_buttons(self):
        self.ui.next_note.clicked.connect(self.next_page)
        self.ui.prev_note.clicked.connect(self.prev_page)
        self.ui.update_update_btn.clicked.connect(self.update)
        self.ui.update_delete_btn.clicked.connect(self.delete)
        self.ui.update_add_btn.clicked.connect(self.add)
        self.ui.update_refresh_btn.clicked.connect(self.refresh)
        self.ui.momentum_calculate_anser.clicked.connect(self.cal_momentum)
        self.ui.g_calculate_answer.clicked.connect(self.cal_gravity)


    #calculate momentum function
    def cal_momentum(self):
    #    p =  self.ui.momentum_input.text()
       m =  float(self.ui.momentum_mass_input.text())
       v =  float(self.ui.momentum_velocity_input.text())
       ans = m*v
       self.ui.momentum_answer.setText(str(ans))
    #calculate gravitational force of attraction
    def cal_gravity(self):
        g = 6.67408*math.pow(10,-11)
        m1 = float(self.ui.mi_input.text())
        m2 = float(self.ui.m2_input.text())
        r  = float(self.ui.g_radius.text())
        f  = (g*m1*m2)
        dp = math.pow(r,2)
        ans = f/dp
        self.ui.g_answer_input.setText(str(ans));
        self.toast.show_toast(title="Check1", msg="Gravity Calculation Completed Successfully", icon_path=None, threaded=True)

      #function to pull all data from database
    def pullData(self):
       sql = "SELECT * FROM Topics where id = %d"%(MainWindow.page_id)
       MainWindow.controller.execute(sql)
       result = MainWindow.controller.fetchone()
       self.ui.note1_label.setText(str(result[1])) 
       self.ui.note_content.insertPlainText (str(result[2]))
       
    #creting function to connect to next page
    def next_page(self):
        try:
            next_id = MainWindow.page_id
            sql = "SELECT * FROM Topics WHERE id=%d"%(next_id)
            MainWindow.controller.execute(sql)
            result = MainWindow.controller.fetchone()
            self.ui.single_count_btn.setText(str(result[0]))
            self.ui.note1_label.setText(str(result[1])) 
            self.ui.note_content.setText (str(result[2]))
            self.ui.formula_list_content.setText(str(result[4]))
            self.ui.solved_examples_content.setText(str(result[3]))
            MainWindow.page_id += 1
        except:
            MainWindow.page_id += 1
            next_id = MainWindow.page_id
            sql = "SELECT * FROM Topics WHERE id=%d"%(next_id)
            MainWindow.controller.execute(sql)
            result = MainWindow.controller.fetchone()
            self.ui.single_count_btn.setText(str(result[0]))
            self.ui.note1_label.setText(str(result[1])) 
            self.ui.note_content.setText (str(result[2]))
            self.ui.formula_list_content.setText(str(result[4]))
            self.ui.solved_examples_content.setText(str(result[3]))
            MainWindow.page_id += 1 
                
    def prev_page(self):
        try:
            prev_id = MainWindow.page_id-1
            sql = "SELECT * FROM Topics WHERE id=%d"%(prev_id)
            MainWindow.controller.execute(sql)
            result = MainWindow.controller.fetchone()
            self.ui.single_count_btn.setText(str(result[0]))
            self.ui.note1_label.setText(str(result[1])) 
            self.ui.note_content.setText (str(result[2]))
            self.ui.formula_list_content.setText(str(result[4]))
            self.ui.solved_examples_content.setText(str(result[3]))
            MainWindow.page_id = prev_id
        except:
            prev_id = MainWindow.page_id-1
            sql = "SELECT * FROM Topics WHERE id=%d"%(prev_id)
            MainWindow.controller.execute(sql)
            result = MainWindow.controller.fetchone()
            self.ui.single_count_btn.setText(str(result[0]))
            self.ui.note1_label.setText(str(result[1])) 
            self.ui.note_content.setText (str(result[2]))
            self.ui.formula_list_content.setText(str(result[4]))
            self.ui.solved_examples_content.setText(str(result[3]))
            MainWindow.page_id = prev_id
                       
    def get_count(self):
        sql = "SELECT COUNT(*) FROM Topics"
        MainWindow.controller.execute(sql)
        result = MainWindow.controller.fetchall() 
        self.ui.total_count_btn.setText(str(result[0][0]))
        main_result = result[0][0]
        return main_result   
    
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
        
    def refresh(self):
        try:
            id     = int(self.ui.update_count_label.text())
            sql    = 'SELECT * FROM Topics where id=%d'%(id)
            result = MainWindow.controller.execute(sql)
            result = MainWindow.controller.fetchone()
            
            #defining and the widget in the textbox interface
            self.ui.update_count_label.setText(str(result[0]))
            self.ui.update_note_title.setText(str(result[1]))
            self.ui.update_note_content.setText(str(result[2]))
            self.ui.update_solved_examples_content.setText(str(result[3]))
            self.ui.update_formula_list_content.setText(str(result[4]))
        except:
            self.ui.update_note_content.setText("OooPs!... \n No Content Exist For Record with Id of {}".format(id))
            self.ui.update_solved_examples_content.setText("OooPs!... \n No Content Exist For Record with Id of {}".format(id))
            self.ui.update_formula_list_content.setText("OooPs!... \n No Content Exist For Record with Id of {}".format(id))
            self.toast.show_toast(title="Physics Assistant V1.0", msg="Database Refresh Successful", icon_path="icons/atom.ico", threaded=True)
            
            

    # creating function to add data into the database
    def add(self):
        try:
            id_             = int(self.ui.update_count_label.text())
            title_          = str(self.ui.update_note_title.text())
            content_        = str(self.ui.update_note_content.toHtml())
            examples_       = str(self.ui.update_solved_examples_content.toHtml())
            formula_list_   = str(self.ui.update_formula_list_content.toHtml())
            row = (id_, title_, content_, examples_, formula_list_,)
            sql = '''INSERT INTO Topics(id, title, content, examples, formula_list) VALUES(?,?,?,?,?)'''
            MainWindow.controller.execute(sql,row)
            MainWindow.db.commit()
        except:
            self.ui.update_note_content.setText("An Error Occured While Trying to Add Data to the database \n Record Not Inserted to Database...")
            self.ui.update_solved_examples_content.setText("An Error Occured While Trying to Add Data to the database \n Record Not Inserted to Database...")
            self.ui.update_formula_list_content.setText("An Error Occured While Trying to Add Data to the database \n Record Not Inserted to Database...")
        else:
            self.ui.update_note_content.setText("Record Added To Database Successfully!.. \n Click the Refresh Button To Continue ==>")
            self.ui.update_solved_examples_content.setText("Record Added To Database Successfully!.. \n Click the Refresh Button To Continue ==>")
            self.ui.update_formula_list_content.setText("Record Added To Database Successfully!.. \n Click the Refresh Button To Continue ==>")
            self.toast.show_toast(title="Physics Assistant V1.0", msg="Record Successfully Added To The Database", icon_path="icons/atom.ico", threaded=True)
            
        
    
    def update(self):
        try:
            #defining and the widget in the textbox interface
            id              = int(self.ui.update_count_label.text())
            title_          = str(self.ui.update_note_title.text())
            content_        = str(self.ui.update_note_content.toHtml())
            examples_       = str(self.ui.update_solved_examples_content.toHtml())
            formula_list_   = str(self.ui.update_formula_list_content.toHtml())
            
            row = (title_, content_, examples_, formula_list_, id)
            sql = '''UPDATE Topics SET title=?, content=?, examples=?, formula_list=? where id = ?'''
            MainWindow.controller.execute(sql,row)
            MainWindow.db.commit()
        except:
            self.ui.update_note_content.setText("There Was An Error While Trying to Update Database Content")
            self.ui.update_solved_examples_content.setText("There Was An Error While Trying to Update Database Content")
            self.ui.update_formula_list_content.setText("There Was An Error While Trying to Update Database Content")
        else:
            self.ui.update_note_content.setText("Database Update Was Successful... \n Click Refresh Button to Continue ==>")
            self.ui.update_solved_examples_content.setText("Database Update Was Successful... \n Click Refresh Button to Continue ==>")
            self.ui.update_formula_list_content.setText("Database Update Was Successful... \n Click Refresh Button to Continue ==>")
            self.toast.show_toast(title="Physics Assistant V1.0", msg="Update To The Database Was Successful", icon_path="icons/atom.ico", threaded=True)
            
    
    def delete(self):
        try:
            d =int(self.ui.update_count_label.text())
            sql = 'DELETE FROM Topics where id=%d'%(d)
            MainWindow.controller.execute(sql)
            MainWindow.db.commit()
        except:
            self.ui.update_note_content.setText("Unable To Delete Database Record")
            self.ui.update_solved_examples_content.setText("Unable To Delte Database Record...")
            self.ui.update_formula_list_content.setText("Unable To Delete Database Record...")
        else:
            self.ui.update_note_content.setText("Record Deleted Successfully... \n Click Refresh Button to Continue ==>")
            self.ui.update_solved_examples_content.setText("Record Deleted Successfully... \n Click Refresh Button to Continue ==>")
            self.ui.update_formula_list_content.setText("Record Deleted Successfullly... \n Click Refresh Button to Continue ==>")
            self.toast.show_toast(title="Physics Assistant V1.0", msg="Database Record Deleted Successfully!", icon_path="icons/atom.ico", threaded=True)

   
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # web = QWebEngineView()
    # web.load(QUrl('https://thegeonerds.com'))
    # web.show()
    # web1 = QWebEngineView()
    # web1.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
    # web1.load(QUrl('formula.pdf'))
    # web1.show()
    sys.exit(app.exec_())
        
#executing the application 
if __name__ == "__main__":
    main()
   
    