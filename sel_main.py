import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QDate
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from Ui_init import Ui_MainWindow 
import call_main,main_qm
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from qfluentwidgets import PushButton

class CallMain(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        #self.Call_GMY = call_main.CallMain()
        #self.PushGMY= self.findChild(PushButton,'pushGMY')
        #self.PushQM= self.findChild(PushButton,'pushQM')
        self.PushQuit = self.findChild(PushButton,'pushQuit')
        self.PushGMY.clicked.connect(self.Call_GMY)
        self.PushQM.clicked.connect(self.Call_QM)
        

    def Call_GMY(self):
        main_gmy.show()

    def Call_QM(self):
        qmmain_qm.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main=CallMain()
    main_gmy = call_main.CallMain()
    qmmain_qm = main_qm.CallMain()
    main.show()
    sys.exit(app.exec_())