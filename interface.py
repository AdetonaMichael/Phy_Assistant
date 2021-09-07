# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from custom_qstacked_widgets import *
from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 889)
        icon = QIcon()
        icon.addFile(u":/icons/icons/atom.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
""
                        "        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushB"
                        "utton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
""
                        "{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QCombo"
                        "Box::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"    "
                        "  width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
""
                        "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
""
                        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1"
                        ":0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* "
                        "spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}"
                        "\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434"
                        ", stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicat"
                        "or:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
""
                        "\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Home = QTabWidget(self.centralwidget)
        self.Home.setObjectName(u"Home")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Home.setFont(font)
        self.Home.setStyleSheet(u"padding:0px;")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QCustomSlideMenu(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setStyleSheet(u"padding:0px;")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.calculate_anser_button_7 = QPushButton(self.frame)
        self.calculate_anser_button_7.setObjectName(u"calculate_anser_button_7")
        self.calculate_anser_button_7.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;\n"
"color:white;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/atom2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.calculate_anser_button_7.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.calculate_anser_button_7)

        self.notes_button_7 = QPushButton(self.frame)
        self.notes_button_7.setObjectName(u"notes_button_7")
        self.notes_button_7.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;\n"
"color:white;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/note.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.notes_button_7.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.notes_button_7)

        self.solved_examples_button_7 = QPushButton(self.frame)
        self.solved_examples_button_7.setObjectName(u"solved_examples_button_7")
        self.solved_examples_button_7.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;\n"
"color:white;")
        self.solved_examples_button_7.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.solved_examples_button_7)

        self.formula_list_button_7 = QPushButton(self.frame)
        self.formula_list_button_7.setObjectName(u"formula_list_button_7")
        self.formula_list_button_7.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;\n"
"color:white;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/calculate.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.formula_list_button_7.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.formula_list_button_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"border:none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/oau.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(200, 120))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"\n"
"font: 14pt \"Tahoma\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-top:10px;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/physics.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(300, 230))

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.app_description = QLabel(self.frame)
        self.app_description.setObjectName(u"app_description")
        font3 = QFont()
        font3.setPointSize(10)
        self.app_description.setFont(font3)
        self.app_description.setStyleSheet(u"border:none;\n"
"margin:20px;")
        self.app_description.setFrameShape(QFrame.Panel)
        self.app_description.setAlignment(Qt.AlignCenter)
        self.app_description.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.app_description)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.about_button = QPushButton(self.frame)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;")
        self.about_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.about_button)

        self.menu_button = QPushButton(self.frame)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 85, 127);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;")
        self.menu_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.menu_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.my_toggle_button = QPushButton(self.tab)
        self.my_toggle_button.setObjectName(u"my_toggle_button")
        self.my_toggle_button.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.my_toggle_button.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.my_toggle_button)

        self.Home.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_10 = QVBoxLayout(self.page1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.note1_label = QLabel(self.page1)
        self.note1_label.setObjectName(u"note1_label")
        font4 = QFont()
        font4.setFamily(u"hooge 05_54")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.note1_label.setFont(font4)
        self.note1_label.setStyleSheet(u"background-color:rgb(0, 0, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.note1_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.note1_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_note = QPushButton(self.page1)
        self.prev_note.setObjectName(u"prev_note")
        self.prev_note.setStyleSheet(u"padding:10px;")

        self.horizontalLayout_3.addWidget(self.prev_note)

        self.note1_content = QPlainTextEdit(self.page1)
        self.note1_content.setObjectName(u"note1_content")
        self.note1_content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Arial\";")

        self.horizontalLayout_3.addWidget(self.note1_content)

        self.line_2 = QFrame(self.page1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.note1_label_fmlist = QLabel(self.page1)
        self.note1_label_fmlist.setObjectName(u"note1_label_fmlist")
        self.note1_label_fmlist.setFont(font4)
        self.note1_label_fmlist.setStyleSheet(u"background-color:rgb(0, 0, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.note1_label_fmlist.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.note1_label_fmlist)

        self.formula_list_content = QPlainTextEdit(self.page1)
        self.formula_list_content.setObjectName(u"formula_list_content")
        self.formula_list_content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Arial\";")

        self.verticalLayout_7.addWidget(self.formula_list_content)

        self.line_5 = QFrame(self.page1)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_5)

        self.note1_label_se = QLabel(self.page1)
        self.note1_label_se.setObjectName(u"note1_label_se")
        self.note1_label_se.setFont(font4)
        self.note1_label_se.setStyleSheet(u"background-color:rgb(0, 0, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.note1_label_se.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.note1_label_se)

        self.solved_example_content = QPlainTextEdit(self.page1)
        self.solved_example_content.setObjectName(u"solved_example_content")
        self.solved_example_content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Arial\";")

        self.verticalLayout_7.addWidget(self.solved_example_content)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.next_note = QPushButton(self.page1)
        self.next_note.setObjectName(u"next_note")
        self.next_note.setStyleSheet(u"padding:10px;")

        self.horizontalLayout_3.addWidget(self.next_note)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_11 = QVBoxLayout(self.page2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.page2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.scrollArea = QScrollArea(self.page2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1082, 731))
        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 70, 61, 31))
        self.label_14.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(520, 130, 41, 31))
        self.label_15.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(220, 100, 51, 41))
        self.label_16.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 110, 201, 31))
        self.label_17.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.gravity_r = QLineEdit(self.scrollAreaWidgetContents_2)
        self.gravity_r.setObjectName(u"gravity_r")
        self.gravity_r.setGeometry(QRect(270, 160, 71, 31))
        self.gravity_m1 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.gravity_m1.setObjectName(u"gravity_m1")
        self.gravity_m1.setGeometry(QRect(280, 110, 71, 31))
        self.gravity_m2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.gravity_m2.setObjectName(u"gravity_m2")
        self.gravity_m2.setGeometry(QRect(420, 110, 71, 31))
        self.line_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(50, 40, 111, 31))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 10, 151, 41))
        self.label_18.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(230, 160, 41, 31))
        self.label_19.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.line_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(100, 140, 401, 21))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(360, 110, 51, 31))
        self.label_20.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.gravity_answer = QLabel(self.scrollAreaWidgetContents_2)
        self.gravity_answer.setObjectName(u"gravity_answer")
        self.gravity_answer.setGeometry(QRect(580, 120, 191, 61))
        self.gravity_answer.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.calculate_gravity = QPushButton(self.scrollAreaWidgetContents_2)
        self.calculate_gravity.setObjectName(u"calculate_gravity")
        self.calculate_gravity.setGeometry(QRect(800, 130, 111, 51))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page2)
        self.formula_list_page = QWidget()
        self.formula_list_page.setObjectName(u"formula_list_page")
        self.verticalLayout_12 = QVBoxLayout(self.formula_list_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.formula_list_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plainTextEdit = QPlainTextEdit(self.formula_list_page)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_4.addWidget(self.plainTextEdit)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_3 = QLabel(self.formula_list_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"padding:10px;\n"
"background-color:white;\n"
"color:black;\n"
"font: 75 14pt \"Arial\";")

        self.verticalLayout_16.addWidget(self.label_3)

        self.line_6 = QFrame(self.formula_list_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_6)

        self.pushButton_3 = QPushButton(self.formula_list_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding-top:10px;\n"
"")
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(300, 230))

        self.verticalLayout_16.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)


        self.verticalLayout_12.addLayout(self.verticalLayout_14)

        self.stackedWidget.addWidget(self.formula_list_page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"hooge 05_54\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stacked_toggle_button = QPushButton(self.frame_2)
        self.stacked_toggle_button.setObjectName(u"stacked_toggle_button")
        self.stacked_toggle_button.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"padding:10px;")

        self.verticalLayout_9.addWidget(self.stacked_toggle_button)

        self.nxt = QPushButton(self.frame_2)
        self.nxt.setObjectName(u"nxt")
        self.nxt.setStyleSheet(u"padding:10px;")

        self.verticalLayout_9.addWidget(self.nxt)

        self.prev = QPushButton(self.frame_2)
        self.prev.setObjectName(u"prev")
        self.prev.setStyleSheet(u"padding:10px;")

        self.verticalLayout_9.addWidget(self.prev)

        self.page = QPushButton(self.frame_2)
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"padding:10px;")

        self.verticalLayout_9.addWidget(self.page)

        self.page_2 = QPushButton(self.frame_2)
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"padding:10px;")

        self.verticalLayout_9.addWidget(self.page_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.Home.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.Home)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Home.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.calculate_anser_button_7.setText(QCoreApplication.translate("MainWindow", u"Calculate Answer", None))
        self.notes_button_7.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.solved_examples_button_7.setText(QCoreApplication.translate("MainWindow", u"Solved_examples", None))
        self.formula_list_button_7.setText(QCoreApplication.translate("MainWindow", u"Formula List", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Powered By OAU Department Of PhySics", None))
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bed Rock Of Modern Technology", None))
        self.pushButton.setText("")
        self.app_description.setText(QCoreApplication.translate("MainWindow", u"This Application is Specially Designed to Offer Solution to Problems of Engineering Physics-II As per Syllabus of Obafemi Awolowo University revised July 2021", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About PhyAss", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.my_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Phy Assistant Version 1.0", None))
        self.Home.setTabText(self.Home.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.note1_label.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.prev_note.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.note1_content.setPlainText("")
        self.note1_label_fmlist.setText(QCoreApplication.translate("MainWindow", u"Formula List", None))
        self.formula_list_content.setPlainText("")
        self.note1_label_se.setText(QCoreApplication.translate("MainWindow", u"Solved Examples", None))
        self.solved_example_content.setPlainText("")
        self.next_note.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Calculate Answer", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"R^2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"M1=", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"G=6.67x10^-34", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"F=Gm1m2", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"R=", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"M2=", None))
        self.gravity_answer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_gravity.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Formula List", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This Section Shows a list of Formulas", None))
        self.pushButton_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Solved Examples", None))
        self.stacked_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Toggle ", None))
        self.nxt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.page.setText(QCoreApplication.translate("MainWindow", u"Formula List", None))
        self.page_2.setText(QCoreApplication.translate("MainWindow", u"Solved Examples", None))
        self.Home.setTabText(self.Home.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

