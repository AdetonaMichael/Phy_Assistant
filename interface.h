/********************************************************************************
** Form generated from reading UI file 'interfacezjVziM.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef INTERFACEZJVZIM_H
#define INTERFACEZJVZIM_H

#include <Custom_Widgets.Widgets.h>
#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_3;
    QPushButton *my_toggle_button;
    QCustomSlideMenu *widget;
    QVBoxLayout *verticalLayout_2;
    QFrame *frame;
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_2;
    QPushButton *pushButton_2;
    QLabel *label;
    QPushButton *pushButton;
    QLabel *app_description;
    QHBoxLayout *horizontalLayout;
    QPushButton *about_button;
    QPushButton *menu_button;
    QSpacerItem *verticalSpacer_3;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(454, 531);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        verticalLayout_3 = new QVBoxLayout(centralwidget);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        my_toggle_button = new QPushButton(centralwidget);
        my_toggle_button->setObjectName(QStringLiteral("my_toggle_button"));
        my_toggle_button->setStyleSheet(QStringLiteral("background-color: rgb(170, 0, 0);"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/icons/atom2.ico"), QSize(), QIcon::Normal, QIcon::Off);
        my_toggle_button->setIcon(icon);

        verticalLayout_3->addWidget(my_toggle_button);

        widget = new QCustomSlideMenu(centralwidget);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setMinimumSize(QSize(0, 50));
        verticalLayout_2 = new QVBoxLayout(widget);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        frame = new QFrame(widget);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setStyleSheet(QLatin1String("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        label_2 = new QLabel(frame);
        label_2->setObjectName(QStringLiteral("label_2"));
        QFont font;
        font.setPointSize(12);
        font.setBold(true);
        font.setWeight(75);
        label_2->setFont(font);
        label_2->setAlignment(Qt::AlignCenter);

        verticalLayout_4->addWidget(label_2);

        pushButton_2 = new QPushButton(frame);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/icons/oau.jpg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_2->setIcon(icon1);
        pushButton_2->setIconSize(QSize(60, 60));

        verticalLayout_4->addWidget(pushButton_2);

        label = new QLabel(frame);
        label->setObjectName(QStringLiteral("label"));
        QFont font1;
        font1.setFamily(QStringLiteral("Tahoma"));
        font1.setPointSize(8);
        font1.setBold(false);
        font1.setItalic(false);
        font1.setWeight(50);
        label->setFont(font1);
        label->setStyleSheet(QLatin1String("\n"
"font: 8pt \"Tahoma\";"));
        label->setAlignment(Qt::AlignCenter);

        verticalLayout_4->addWidget(label);

        pushButton = new QPushButton(frame);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setStyleSheet(QLatin1String("background-color: rgb(255, 255, 255);\n"
"padding-top:10px;\n"
""));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/icons/physics.jpg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon2);
        pushButton->setIconSize(QSize(300, 230));

        verticalLayout_4->addWidget(pushButton);

        app_description = new QLabel(frame);
        app_description->setObjectName(QStringLiteral("app_description"));
        QFont font2;
        font2.setPointSize(10);
        app_description->setFont(font2);
        app_description->setStyleSheet(QLatin1String("border:none;\n"
"margin:20px;"));
        app_description->setFrameShape(QFrame::Panel);
        app_description->setAlignment(Qt::AlignCenter);
        app_description->setWordWrap(true);

        verticalLayout_4->addWidget(app_description);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        about_button = new QPushButton(frame);
        about_button->setObjectName(QStringLiteral("about_button"));
        about_button->setStyleSheet(QLatin1String("background-color: rgb(170, 0, 0);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;"));
        about_button->setIcon(icon);

        horizontalLayout->addWidget(about_button);

        menu_button = new QPushButton(frame);
        menu_button->setObjectName(QStringLiteral("menu_button"));
        menu_button->setStyleSheet(QLatin1String("background-color: rgb(170, 0, 0);\n"
"border-radius:60px;\n"
"margin-right:20px;\n"
"margin-left:20px;\n"
"padding:5px;"));
        menu_button->setIcon(icon);

        horizontalLayout->addWidget(menu_button);


        verticalLayout_4->addLayout(horizontalLayout);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_3);


        verticalLayout->addLayout(verticalLayout_4);


        verticalLayout_2->addWidget(frame);


        verticalLayout_3->addWidget(widget);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        my_toggle_button->setText(QString());
        label_2->setText(QApplication::translate("MainWindow", "Powered By OAU Department Of PhySics", nullptr));
        pushButton_2->setText(QString());
        label->setText(QApplication::translate("MainWindow", "Bed Rock Of Modern Technology", nullptr));
        pushButton->setText(QString());
        app_description->setText(QApplication::translate("MainWindow", "This Application is Specially Designed to Offer Solution to Problems of Engineering Physics-II As per Syllabus of Obafemi Awolowo University revised July 2021", nullptr));
        about_button->setText(QApplication::translate("MainWindow", "About PhyAss", nullptr));
        menu_button->setText(QApplication::translate("MainWindow", "Menu", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // INTERFACEZJVZIM_H
