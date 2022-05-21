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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 820)
        MainWindow.setMinimumSize(QSize(1000, 820))
        MainWindow.setMaximumSize(QSize(1000, 820))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(9, 9, 272, 810))
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
        self.pushButton_2.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.checkBox = QCheckBox(self.horizontalFrame)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.checkBox.setFont(font1)

        self.verticalLayout_3.addWidget(self.checkBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton = QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.chooseFilm = QPushButton(self.horizontalFrame)
        self.chooseFilm.setObjectName(u"chooseFilm")
        sizePolicy.setHeightForWidth(self.chooseFilm.sizePolicy().hasHeightForWidth())
        self.chooseFilm.setSizePolicy(sizePolicy)
        self.chooseFilm.setFont(font)

        self.verticalLayout_3.addWidget(self.chooseFilm)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(281, 11, 702, 808))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(700, 400))
        self.label_2.setPixmap(QPixmap(u"../data/dst.jpg"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(700, 400))
        self.label.setMaximumSize(QSize(700, 400))
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.setPixmap(QPixmap(u"../data/dst.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz film", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Zapis", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Wybierz miejsce", None))
        self.chooseFilm.setText(QCoreApplication.translate("MainWindow", u"Wybierz film", None))
        self.label_2.setText("")
        self.label.setText("")
    # retranslateUi

