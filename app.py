
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox, QFormLayout, QPushButton, QLabel, QLineEdit, \
    QVBoxLayout, QTableWidget


class app_eval(QWidget):

    def __init__(self):
        super(app_eval,self).__init__()
        self.setGeometry(100, 200, 355, 500)
        self.setWindowTitle("evaluation de perfermance ")
        grid = QGridLayout()
        grid.addWidget(input_data(self),0,0)
        grid.addWidget(view_data(self),1,0)
        self.setLayout(grid)


def input_data(self):
    qb = QGroupBox("input rquired DATA")
    qf = QFormLayout()
    nbr = QLabel("Nombre de requete")
    nbrF = QLineEdit()
    tht = QLabel("Thinking time")
    thtF = QLineEdit()
    T = QLabel("durée d\'observation")
    TF = QLineEdit()
    start = QPushButton("Start")
    qf.addRow(nbr,nbrF)
    qf.addRow(tht,thtF)
    qf.addRow(T,TF)
    qf.addRow(start)
    qb.setLayout(qf)

    return qb

def view_data(self):
    qb = QGroupBox("View DATA")
    qV = QVBoxLayout()
    table = QTableWidget()
    table.setRowCount(6)
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels(["BTcpu1","BTdisk1","BTcpu2","BTdisk2","BTcpu3","BTdisk3"])

    table.resizeColumnsToContents()

    AsymTR = QPushButton("Asymptote Temps de Reponse")
    AsymDS = QPushButton("Asymptote Debit du systeme")

    qV.addWidget(table)
    qV.addWidget(AsymTR)
    qV.addWidget(AsymDS)

    qb.setLayout(qV)

    return qb



if __name__ == '__main__':
    app = QApplication(sys.argv) #definir l'application gloabal
    appp = app_eval() # notre application de type widget
    appp.show() #afficher notre application
    sys.exit(app.exec_())#exécuter



