from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartScreen = QtWidgets.QFrame(self.centralwidget)
        self.StartScreen.setGeometry(QtCore.QRect(10, 10, 631, 401))
        self.StartScreen.setStyleSheet("QFrame {\n"
"background-color: rgb(255, 255, 255);\n"
"   border-radius: 10px;\n"
"}")
        self.StartScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartScreen.setObjectName("StartScreen")
        self.progressBar = QtWidgets.QProgressBar(self.StartScreen)
        self.progressBar.setGeometry(QtCore.QRect(30, 360, 571, 31))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"background-color: rgb(236, 236, 236);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"text-align :center;\n"
"border-style:none;\n"
"}\n"
"QProgressBar::chunk {\n"
"border-radius:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.0113636, y1:0.5, x2:0.994318, y2:0.517, stop:0 rgba(62, 2, 104, 5), stop:1 rgba(62, 2, 104, 1));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.StartScreen)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(280, 329, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(65, 95, 109);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.StartScreen)
        self.label_2.setGeometry(QtCore.QRect(210, 70, 211, 201))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background:url(Icons/2.png);\n"
"backgroung-repeat: no-repeat;\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/123456.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.StartScreen)
        self.label_4.setGeometry(QtCore.QRect(-90, 140, 211, 201))
        self.label_4.setStyleSheet("background-image: url(Icons/1.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/Background.png"))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.StartScreen)
        self.label_3.setGeometry(QtCore.QRect(540, 0, 211, 201))
        self.label_3.setStyleSheet("background-image: url(Icons/1.png);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/Background.png"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.StartScreen)
        self.label_5.setGeometry(QtCore.QRect(270, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(62, 2, 104);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Loading"))
        self.label_5.setText(_translate("MainWindow", "MQC"))
# import start
