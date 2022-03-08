#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("edu.vogel9@gmaixl.com", "senha!")
msg = "Hello World!"
server.sendmail("edu.vogel9@gmail.com", "edu.smo9@gmail.com", msg)
server.quit()