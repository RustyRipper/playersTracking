# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 840)
        MainWindow.setMinimumSize(QSize(700, 840))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient.setSpread(QGradient.ReflectSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(196, 255, 249, 255))
        gradient.setColorAt(1, QColor(110, 183, 172, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(213, 234, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(149, 202, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(42, 85, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(56, 113, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient1.setSpread(QGradient.ReflectSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(196, 255, 249, 255))
        gradient1.setColorAt(1, QColor(110, 183, 172, 255))
        brush7 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush7)
        gradient2 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient2.setSpread(QGradient.ReflectSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(196, 255, 249, 255))
        gradient2.setColorAt(1, QColor(110, 183, 172, 255))
        brush8 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush9 = QBrush(QColor(170, 212, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        brush10 = QBrush(QColor(255, 255, 220, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient3.setSpread(QGradient.ReflectSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(196, 255, 249, 255))
        gradient3.setColorAt(1, QColor(110, 183, 172, 255))
        brush11 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient4.setSpread(QGradient.ReflectSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(196, 255, 249, 255))
        gradient4.setColorAt(1, QColor(110, 183, 172, 255))
        brush12 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        gradient5 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient5.setSpread(QGradient.ReflectSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(196, 255, 249, 255))
        gradient5.setColorAt(1, QColor(110, 183, 172, 255))
        brush13 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        gradient6 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient6.setSpread(QGradient.ReflectSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(196, 255, 249, 255))
        gradient6.setColorAt(1, QColor(110, 183, 172, 255))
        brush14 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        gradient7 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient7.setSpread(QGradient.ReflectSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(196, 255, 249, 255))
        gradient7.setColorAt(1, QColor(110, 183, 172, 255))
        brush15 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        gradient8 = QLinearGradient(0.483, 0.619455, 0, 0.619)
        gradient8.setSpread(QGradient.ReflectSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(196, 255, 249, 255))
        gradient8.setColorAt(1, QColor(110, 183, 172, 255))
        brush16 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush17 = QBrush(QColor(85, 170, 255, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile("../playerstracking/data/icon.bmp", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background:qlineargradient(spread:reflect, x1:0.483, y1:0.619455, x2:0, y2:0.619, stop:0 rgba(196, 255, 249, 255), stop:1 rgba(110, 183, 172, 255))\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.verticalLayout_3 = QVBoxLayout(self.horizontalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.horizontalFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton { \n"
"color:rgb(53, 53, 53);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.284, stop:0 rgba(0, 0, 0, 255), stop:0.0454545 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 25px;\n"
"border:5px solid black\n"
"}\n"
"\n"
"QPushButton:hover { color: rgb(0, 170, 255) }\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.checkBox_2 = QCheckBox(self.horizontalFrame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.checkBox_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.checkBox_2, 0, Qt.AlignHCenter)

        self.checkBox = QCheckBox(self.horizontalFrame)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)
        self.checkBox.setFont(font1)

        self.verticalLayout_3.addWidget(self.checkBox, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        brush18 = QBrush(QColor(53, 53, 53, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        gradient9 = QLinearGradient(1, 1, 0, 0.284)
        gradient9.setSpread(QGradient.PadSpread)
        gradient9.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(0, 0, 0, 255))
        gradient9.setColorAt(0.0454545, QColor(161, 161, 161, 255))
        gradient9.setColorAt(1, QColor(255, 255, 255, 255))
        brush19 = QBrush(gradient9)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        gradient10 = QLinearGradient(1, 1, 0, 0.284)
        gradient10.setSpread(QGradient.PadSpread)
        gradient10.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(0, 0, 0, 255))
        gradient10.setColorAt(0.0454545, QColor(161, 161, 161, 255))
        gradient10.setColorAt(1, QColor(255, 255, 255, 255))
        brush20 = QBrush(gradient10)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush20)
        gradient11 = QLinearGradient(1, 1, 0, 0.284)
        gradient11.setSpread(QGradient.PadSpread)
        gradient11.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(0, 0, 0, 255))
        gradient11.setColorAt(0.0454545, QColor(161, 161, 161, 255))
        gradient11.setColorAt(1, QColor(255, 255, 255, 255))
        brush21 = QBrush(gradient11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush21)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        gradient12 = QLinearGradient(1, 1, 0, 0.284)
        gradient12.setSpread(QGradient.PadSpread)
        gradient12.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(0, 0, 0, 255))
        gradient12.setColorAt(0.0454545, QColor(161, 161, 161, 255))
        gradient12.setColorAt(1, QColor(255, 255, 255, 255))
        brush22 = QBrush(gradient12)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush22)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        gradient13 = QLinearGradient(1, 1, 0, 0.284)
        gradient13.setSpread(QGradient.PadSpread)
        gradient13.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(0, 0, 0, 255))
        gradient13.setColorAt(0.0454545, QColor(161, 161, 161, 255))
        gradient13.setColorAt(1, QColor(255, 255, 255, 255))
        brush23 = QBrush(gradient13)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        gradient14 = QLinearGradient(1, 1, 0, 0.284)
        gradient14.setSpread(QGradient.PadSpread)
        gradient14.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(0, 0, 0, 255))
        gradient14.setColorAt(0.0454545, QColor(161, 161, 161, 255))
        gradient14.setColorAt(1, QColor(255, 255, 255, 255))
        brush24 = QBrush(gradient14)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush24)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        brush25 = QBrush(QColor(84, 84, 84, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush25)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush25)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush25)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.pushButton.setPalette(palette1)
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setFocusPolicy(Qt.StrongFocus)
        self.pushButton.setStyleSheet(u"\n"
"QPushButton { \n"
"color:rgb(53, 53, 53);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.284, stop:0 rgba(0, 0, 0, 255), stop:0.0454545 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 25px;\n"
"border:5px solid black\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:rgb(84, 84, 84);\n"
"color:rgb(53, 53, 53)\n"
"}\n"
"QPushButton:hover { color: rgb(0, 170, 255) }\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_5 = QPushButton(self.horizontalFrame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"\n"
"QPushButton { \n"
"color:rgb(53, 53, 53);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.284, stop:0 rgba(0, 0, 0, 255), stop:0.0454545 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"border:5px solid black\n"
"}\n"
"\n"
"QPushButton:hover { color: rgb(0, 170, 255) }\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.horizontalFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"\n"
"QPushButton { \n"
"color:rgb(53, 53, 53);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.284, stop:0 rgba(0, 0, 0, 255), stop:0.0454545 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"border:5px solid black\n"
"}\n"
"QPushButton:hover { color: rgb(0, 170, 255) }\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.horizontalFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton { \n"
"color:rgb(53, 53, 53);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.284, stop:0 rgba(0, 0, 0, 255), stop:0.0454545 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"border:5px solid black\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: rgb(0, 170, 255) }\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.ButtonStart = QPushButton(self.horizontalFrame)
        self.ButtonStart.setObjectName(u"ButtonStart")
        sizePolicy.setHeightForWidth(self.ButtonStart.sizePolicy().hasHeightForWidth())
        self.ButtonStart.setSizePolicy(sizePolicy)
        self.ButtonStart.setFont(font2)
        self.ButtonStart.setStyleSheet(u"\n"
"QPushButton { \n"
"color:rgb(53, 53, 53);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.284, stop:0 rgba(0, 0, 0, 255), stop:0.0454545 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"border:5px solid black\n"
"}\n"
"\n"
"QPushButton:hover { color: rgb(0, 170, 255) }")

        self.verticalLayout_3.addWidget(self.ButtonStart)


        self.horizontalLayout.addWidget(self.horizontalFrame)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(640, 400))
        self.label_2.setMaximumSize(QSize(720, 400))
        self.label_2.setStyleSheet(u"QLabel{\n"
"background: rgb(112, 112, 112);\n"
"border-radius: 15px;\n"
"border:5px solid black}\n"
"")
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(640, 400))
        self.label.setMaximumSize(QSize(720, 400))
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.setStyleSheet(u"QLabel{\n"
"background: grey;\n"
"border-radius: 15px;\n"
"border:5px solid black}\n"
"")
        self.label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Players Tracker", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz film", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Statyczna kamera", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Zapis", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Wybierz miejsce\n"
"do zapisu", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Boisko", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Dru\u017cyna 1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Dru\u017cyna 2", None))
        self.ButtonStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText("")
        self.label.setText("")
    # retranslateUi

