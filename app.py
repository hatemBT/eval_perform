
import sys
import time
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox, QFormLayout, QPushButton, QLabel, QLineEdit, \
    QVBoxLayout, QTableWidget,QProgressBar


class app_eval(QWidget):

    def __init__(self):
        super(app_eval,self).__init__()
        self.setGeometry(100, 200, 355, 500)
        self.setWindowTitle("evaluation de perfermance ")
        self.grid = QGridLayout()
        #-------------------------------------------------
        self.qb = QGroupBox("input rquired DATA")
        self.qf = QFormLayout()
        self.nbr = QLabel("Nombre de requete")
        self.nbrF = QLineEdit("0")
        self.tht = QLabel("Thinking time")
        self.thtF = QLineEdit("0")
        self.T = QLabel("durée d\'observation")
        self.TF = QLineEdit("0")
        self.start = QPushButton("Start")
        self.progbar = QProgressBar()
        self.start.clicked.connect(lambda: progress(self,int(self.TF.text())))
        self.x = int(self.TF.text())
        self.qf.addRow(self.nbr, self.nbrF)
        self.qf.addRow(self.tht, self.thtF)
        self.qf.addRow(self.T, self.TF)
        self.qf.addRow(self.start)
        self.qf.addRow(self.progbar)
        self.qb.setLayout(self.qf)
        #-------------------------------------------------
        self.qb1 = QGroupBox("View DATA")
        self.qV = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["BTcpu1", "BTdisk1", "BTcpu2", "BTdisk2", "BTcpu3", "BTdisk3"])

        self.table.resizeColumnsToContents()

        self.AsymTR = QPushButton("Asymptote Temps de Reponse")
        self.AsymDS = QPushButton("Asymptote Debit du systeme")

        self.qV.addWidget(self.table)
        self.qV.addWidget(self.AsymTR)
        self.qV.addWidget(self.AsymDS)

        self.qb1.setLayout(self.qV)
        #-------------------------------------------------
        self.grid.addWidget(self.qb,0,0)
        self.grid.addWidget(self.qb1,1,0)
        self.setLayout(self.grid)

def progress(self,n):
    for i in range(n+1):
        time.sleep(1)
        x=(i/n)*100

        self.progbar.setValue(x)






if __name__ == '__main__':
    app = QApplication(sys.argv) #definir l'application gloabal
    appp = app_eval() # notre application de type widget
    appp.show() #afficher notre application
    sys.exit(app.exec_())#exécuter



