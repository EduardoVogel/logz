# Form implementation generated from reading ui file 'logz.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Inicio = QtWidgets.QPushButton(self.centralwidget)
        self.Inicio.setGeometry(QtCore.QRect(20, 50, 75, 24))
        self.Inicio.setObjectName("Inicio")
        self.Teste = QtWidgets.QPushButton(self.centralwidget)
        self.Teste.setGeometry(QtCore.QRect(20, 110, 75, 24))
        self.Teste.setObjectName("Teste")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(True)
        self.logo.setGeometry(QtCore.QRect(0, 0, 800, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.Broca1 = QtWidgets.QLabel(self.centralwidget)
        self.Broca1.setGeometry(QtCore.QRect(160, 120, 131, 291))
        self.Broca1.setText("")
        self.Broca1.setPixmap(QtGui.QPixmap("Broca1.PNG"))
        self.Broca1.setScaledContents(True)
        self.Broca1.setObjectName("Broca1")
        self.Broca2 = QtWidgets.QLabel(self.centralwidget)
        self.Broca2.setGeometry(QtCore.QRect(300, 120, 131, 291))
        self.Broca2.setText("")
        self.Broca2.setPixmap(QtGui.QPixmap("Broca2.PNG"))
        self.Broca2.setScaledContents(True)
        self.Broca2.setObjectName("Broca2")
        self.logo.raise_()
        self.Teste.raise_()
        self.Inicio.raise_()
        self.Broca1.raise_()
        self.Broca2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Inicio.setText(_translate("MainWindow", "Inicio"))
        self.Teste.setText(_translate("MainWindow", "Teste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())