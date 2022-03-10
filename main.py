from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QLabel, QLineEdit
import Excel_Pandas
global key_login, cont_login, user

user = ''
cont_login = 0
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

        self.lineEdit_Login = self.findChild(QLineEdit, "lineEdit_Login")

        #imagens
        self.image_1 = self.findChild(QLabel, "Broca1")
        self.image_2 = self.findChild(QLabel, "Broca2")
        self.image_3 = self.findChild(QLabel, "Broca3")
        self.image_4 = self.findChild(QLabel, "Broca4")
        self.image_5 = self.findChild(QLabel, "Broca5")
        self.image_User = self.findChild(QLabel, "imagem_User")
        self.image_User_2 = self.findChild(QLabel, "imagem_User_2")
        self.user_logado = self.findChild(QLabel, "user_logado")

        #check box
        self.Check_1 = self.findChild(QCheckBox, "Check_Broca1")
        self.Check_2 = self.findChild(QCheckBox, "Check_Broca2")
        self.Check_3 = self.findChild(QCheckBox, "Check_Broca3")
        self.Check_4 = self.findChild(QCheckBox, "Check_Broca4")
        self.Check_5 = self.findChild(QCheckBox, "Check_Broca5")

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

        self.show()

    #recebe a senha do usuario e armazena
    def key_User(self):

        global cont_login, var, user
        sender = self.sender()
        soma = cont_login

        if cont_login < 4:
            if sender.text() == '1':
                key_login[cont_login] = 1
            elif sender.text() == '2':
                key_login[cont_login] = 2
            elif sender.text() == '3':
                key_login[cont_login] = 3
            elif sender.text() == '4':
                key_login[cont_login] = 4
            elif sender.text() == '5':
                key_login[cont_login] = 5
            elif sender.text() == '6':
                key_login[cont_login] = 6
            elif sender.text() == '7':
                key_login[cont_login] = 7
            elif sender.text() == '8':
                key_login[cont_login] = 8
            elif sender.text() == '9':
                key_login[cont_login] = 9
            elif sender.text() == '0':
                key_login[cont_login] = 0

        cont_login = soma + 1
        var = self.lineEdit_Login.text()
        self.lineEdit_Login.setText(var + "*")

        if (key_login[0] == 1 and key_login[1] == 2 and key_login[2] == 3 and key_login[3] == 4) and cont_login == 4:
            user = "admin"
            self.user_logado.setText(user)
            self.user_logado.setStyleSheet("color:#ffffff;")
            print(key_login, cont_login, user)
            self.show_unhid()
            self.hide_login()

        if cont_login >= 4:
            cont_login = 0
            self.lineEdit_Login.setText("")
            key_login[0] = 0
            key_login[1] = 0
            key_login[2] = 0
            key_login[3] = 0
        print(key_login, cont_login, user)

    #esconde login após logar
    def hide_login(self):
        self.image_User.hide()
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

    #mostra itens após login
    def show_unhid(self):
        self.image_1.raise_()
        self.image_2.raise_()
        self.image_3.raise_()
        self.image_4.raise_()
        self.image_5.raise_()
        self.Check_1.raise_()
        self.Check_2.raise_()
        self.Check_3.raise_()
        self.Check_4.raise_()
        self.Check_5.raise_()
        self.button_Hide.raise_()
        self.button_Show.raise_()
        self.button_Next.raise_()
        self.button_Previous.raise_()
        self.image_User_2.raise_()
        self.user_logado.show()

    #mostra itens após login
    def mostrar(self):
        self.image_1.show()
        self.image_2.show()
        self.image_3.show()
        self.image_4.show()
        self.image_5.show()
        self.Check_1.show()
        self.Check_2.show()
        self.Check_3.show()
        self.Check_4.show()
        self.Check_5.show()
        self.button_Hide.show()
        self.button_Show.show()
        self.button_Next.show()
        self.button_Previous.show()
        self.user_logado.show()
        self.image_User_2.show()
        Excel_Pandas.modificar_banco()

    #esconde itens se não estiver logado
    def hide_unhid(self):
        self.image_1.hide()
        self.image_2.hide()
        self.image_3.hide()
        self.image_4.hide()
        self.image_5.hide()
        self.Check_1.hide()
        self.Check_2.hide()
        self.Check_3.hide()
        self.Check_4.hide()
        self.Check_5.hide()
        self.image_User_2.hide()
        self.user_logado.hide()


app = QApplication([])
UIWindow = UI()
app.exec()
