#####################################################
#              Auther : hatem ben tayeb             #
#              Email : hatemtayeb2@gmail.com        #
#              Script : eval_perform                #
#              Subjet : evaluation de performance   #
#####################################################



import sys
import time
import os
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox, QFormLayout, QPushButton, QLabel, QLineEdit, \
    QVBoxLayout, QTableWidget,QProgressBar,QTableWidgetItem


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
        self.nbrF = QLineEdit("1")
        self.tht = QLabel("Thinking time")
        self.thtF = QLineEdit("1")
        self.T = QLabel("Durée d\'observation")
        self.TF = QLineEdit("1")
        self.blk = QLabel("Nombre de bloque")
        self.blkF = QLineEdit("1")
        self.start = QPushButton("Start")
        self.clear = QPushButton("clear")
        self.progbar = QProgressBar()

        #-------------------------------------------------
        self.qb1 = QGroupBox("View DATA")
        self.qV = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(50)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["BTcpu1", "BTdisk1", "BTcpu2", "BTdisk2", "BTcpu3", "BTdisk3"])

        #self.table.resizeColumnsToContents()

        self.AsymTR = QPushButton("Asymptote Temps de Reponse")
        self.AsymDS = QPushButton("Asymptote Debit du systeme")
        self.load   = QPushButton("Load Data")


        #-------------------------------------------------
        self.qb1.setLayout(self.qV)
        self.qV.addWidget(self.table)
        self.qV.addWidget(self.load)
        self.qV.addWidget(self.AsymTR)
        self.qV.addWidget(self.AsymDS)

        self.qf.addRow(self.nbr, self.nbrF)
        self.qf.addRow(self.tht, self.thtF)
        self.qf.addRow(self.T, self.TF)
        self.qf.addRow(self.blk, self.blkF)
        self.qf.addRow(self.start,self.clear)
        self.qf.addRow(self.progbar)
        self.qb.setLayout(self.qf)
        self.grid.addWidget(self.qb,0,0)
        self.grid.addWidget(self.qb1,1,0)
        self.setLayout(self.grid)
        #-------------------------------------------------
        self.x = int(self.TF.text())
        self.start.clicked.connect(lambda: progress(self, int(self.TF.text())))
        self.AsymTR.clicked.connect(lambda :plot_data())
        self.load.clicked.connect(lambda :setDaTa(self))
        self.clear.clicked.connect(lambda :clearData())


def clearData():
    os.system('rm *.{csv,txt}')


def progress(self,n):
    for i in range(1,n+1):
        time.sleep(int(self.thtF.text()))
        x=(i/n)*100
        self.progbar.setValue(x)
        os.system(os.path.join("test","disk_cpu.sh")+" "+self.blkF.text()+" "+ self.nbrF.text())


def setDaTa(self):

    if(int(self.blkF.text())==1):
        cp=0
        with open('finaldisk.csv','r') as f:
            xx= f.read().split(',')
            for i in xx:

                  if i != None:
                      self.table.setItem(cp, 1, QTableWidgetItem(str(i)))
                      cp += 1
                  else:
                      pass

            cp1 = 0
            with open('finalcpu.csv', 'r') as f:
                xx = f.read().split(',')
                for i in xx:

                    if i != None:
                        self.table.setItem(cp1, 0, QTableWidgetItem(str(i)))

                        cp1 += 1
                    else:
                        pass

    elif(int(self.blkF.text())==2):
        cp2 = 0
        with open('finaldisk.csv', 'r') as f:
            xx = f.read().split(',')
            for i in xx:

                if i != None:
                    self.table.setItem(cp2, 3, QTableWidgetItem(str(i)))
                    cp2 += 1
                else:
                    pass

            cp3 = 0
            with open('finalcpu.csv', 'r') as f:
                xx = f.read().split(',')
                for i in xx:

                    if i != None:
                        self.table.setItem(cp3, 2, QTableWidgetItem(str(i)))

                        cp3 += 1
                    else:
                        pass

    else:
        cp4 = 0
        with open('finaldisk.csv', 'r') as f:
            xx = f.read().split(',')
            for i in xx:

                if i != None:
                    self.table.setItem(cp4, 5, QTableWidgetItem(str(i)))
                    cp4 += 1
                else:
                    pass

            cp5 = 0
            with open('finalcpu.csv', 'r') as f:
                xx = f.read().split(',')
                for i in xx:

                    if i != None:
                        self.table.setItem(cp5, 4, QTableWidgetItem(str(i)))

                        cp5 += 1
                    else:
                        pass


def plot_data():
    plt.xlim(50)
    plt.ylim(6)
    plt.hlines(1.99,0,20,'r','-')
    plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv) #definir l'application gloabal
    appp = app_eval() # notre application de type widget
    appp.show() #afficher notre application
    sys.exit(app.exec_())#exécuter



