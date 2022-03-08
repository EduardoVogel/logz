from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QLabel, QLineEdit, QMessageBox

global key_login, contator_login

contator_login = 0
key_login = [0,0,0,0]

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        #carrega o uic
        uic.loadUi('logz.ui', self)

        # definir botões e widgets
        self.button_Hide    = self.findChild(QPushButton, "Hide")
        self.button_Show    = self.findChild(QPushButton, "Show")
        self.button_Next    = self.findChild(QPushButton, "Next")
        self.button_Previous = self.findChild(QPushButton, "Previous")
        self.button_Number1 = self.findChild(QPushButton, "Number_1")
        self.button_Number2 = self.findChild(QPushButton, "Number_2")
        self.button_Number3 = self.findChild(QPushButton, "Number_3")
        self.button_Number4 = self.findChild(QPushButton, "Number_4")
        self.button_Number5 = self.findChild(QPushButton, "Number_5")
        self.button_Number6 = self.findChild(QPushButton, "Number_6")
        self.button_Number7 = self.findChild(QPushButton, "Number_7")
        self.button_Number8 = self.findChild(QPushButton, "Number_8")
        self.button_Number9 = self.findChild(QPushButton, "Number_9")
        self.button_Number0 = self.findChild(QPushButton, "Number_0")
        self.button_Login   = self.findChild(QPushButton, "Logar")

        self.lineEdit_Login = self.findChild(QLineEdit, "lineEdit_Login")

        #imagens
        self.image_Broca1 = self.findChild(QLabel, "Broca1")
        self.image_Broca2 = self.findChild(QLabel, "Broca2")
        self.image_Broca3 = self.findChild(QLabel, "Broca3")
        self.image_Broca4 = self.findChild(QLabel, "Broca4")
        self.image_Broca5 = self.findChild(QLabel, "Broca5")
        self.imagem_User = self.findChild(QLabel, "imagem_User")

        #check box
        self.Check_Broca1 = self.findChild(QCheckBox, "Check_Broca1")
        self.Check_Broca2 = self.findChild(QCheckBox, "Check_Broca2")
        self.Check_Broca3 = self.findChild(QCheckBox, "Check_Broca3")
        self.Check_Broca4 = self.findChild(QCheckBox, "Check_Broca4")
        self.Check_Broca5 = self.findChild(QCheckBox, "Check_Broca5")

        # clicar no botao
        self.button_Hide.clicked.connect(self.hide_unhid)
        self.button_Show.clicked.connect(self.mostrar)
        self.button_Number1.clicked.connect(self.key_User)
        self.button_Number2.clicked.connect(self.key_User)
        self.button_Number3.clicked.connect(self.key_User)
        self.button_Number4.clicked.connect(self.key_User)
        self.button_Number5.clicked.connect(self.key_User)
        self.button_Number6.clicked.connect(self.key_User)
        self.button_Number7.clicked.connect(self.key_User)
        self.button_Number8.clicked.connect(self.key_User)
        self.button_Number9.clicked.connect(self.key_User)
        self.button_Number0.clicked.connect(self.key_User)
        self.button_Login.clicked.connect(self.Confirm_key)

        self.show()

    #recebe a senha do usuario e armazena
    def key_User(self):

        global contator_login, var
        sender = self.sender()
        soma = contator_login

        if contator_login < 4:
            if sender.text() == '1':
                key_login[contator_login] = 1
            elif sender.text() == '2':
                key_login[contator_login] = 2
            elif sender.text() == '3':
                key_login[contator_login] = 3
            elif sender.text() == '4':
                key_login[contator_login] = 4
            elif sender.text() == '5':
                key_login[contator_login] = 5
            elif sender.text() == '6':
                key_login[contator_login] = 6
            elif sender.text() == '7':
                key_login[contator_login] = 7
            elif sender.text() == '8':
                key_login[contator_login] = 8
            elif sender.text() == '9':
                key_login[contator_login] = 9
            elif sender.text() == '0':
                key_login[contator_login] = 0

            contator_login = soma + 1
            var = self.lineEdit_Login.text()
            self.lineEdit_Login.setText(var + "*")
        else:
            contator_login = 0
            self.show_Popup()
            self.lineEdit_Login.setText("")
            key_login[0] = 0
            key_login[1] = 0
            key_login[2] = 0
            key_login[3] = 0
        print(key_login, contator_login)

    #popUp para quando der mais de 4 caracteres
    def show_Popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro login")
        msg.setText("Limite de caracteres atingido!!!")
        print("Limite de caracteres atingido!!!")
        x = msg.exec()

    #confirma o login
    def Confirm_key(self):
        if key_login[0] == 1 and key_login[1] == 2 and key_login[2] == 3 and key_login[3] == 4:
            msg = QMessageBox()
            msg.setWindowTitle("Login")
            msg.setText("Login Realizado com sucesso!")
            print("Login realizado")
            x = msg.exec()
            self.show_unhid()
            self.hide_login()

    #esconde login após logar
    def hide_login(self):
        self.button_Login.hide()
        self.imagem_User.hide()
        self.lineEdit_Login.hide()
        self.button_Number1.hide()
        self.button_Number2.hide()
        self.button_Number3.hide()
        self.button_Number4.hide()
        self.button_Number5.hide()
        self.button_Number6.hide()
        self.button_Number7.hide()
        self.button_Number8.hide()
        self.button_Number9.hide()
        self.button_Number0.hide()
        self.button_Next.hide()
        self.button_Previous.hide()

    #mostra itens após login
    def show_unhid(self):
        self.image_Broca1.raise_()
        self.image_Broca2.raise_()
        self.image_Broca3.raise_()
        self.image_Broca4.raise_()
        self.image_Broca5.raise_()
        self.Check_Broca1.raise_()
        self.Check_Broca2.raise_()
        self.Check_Broca3.raise_()
        self.Check_Broca4.raise_()
        self.Check_Broca5.raise_()
        self.button_Hide.raise_()
        self.button_Show.raise_()
        self.button_Next.raise_()
        self.button_Previous.raise_()

    #mostra itens após login
    def mostrar(self):
        self.image_Broca1.show()
        self.image_Broca2.show()
        self.image_Broca3.show()
        self.image_Broca4.show()
        self.image_Broca5.show()
        self.Check_Broca1.show()
        self.Check_Broca2.show()
        self.Check_Broca3.show()
        self.Check_Broca4.show()
        self.Check_Broca5.show()
        self.button_Hide.show()
        self.button_Show.show()
        self.button_Next.show()
        self.button_Previous.show()

    #esconde itens se não estiver logado
    def hide_unhid(self):
        self.image_Broca1.hide()
        self.image_Broca2.hide()
        self.image_Broca3.hide()
        self.image_Broca4.hide()
        self.image_Broca5.hide()
        self.Check_Broca1.hide()
        self.Check_Broca2.hide()
        self.Check_Broca3.hide()
        self.Check_Broca4.hide()
        self.Check_Broca5.hide()


app = QApplication([])
UIWindow = UI()
app.exec()
