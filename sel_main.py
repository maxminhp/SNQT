import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtWidgets import QMainWindow
from Ui_init import Ui_MainWindow 
import call_main,main_qm
from qfluentwidgets import PushButton

class CallMain(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        #获取屏幕分辨率数据
        #screen_width = QApplication.desktop().screenGeometry().width()  
        #screen_height = QApplication.desktop().screenGeometry().height()
        #xfl_x =QApplication.desktop().logicalDpiX()
        #sfl= xfl_x/96
        #self.setGeometry(int((screen_width/3)*sfl),int((screen_height/3)*sfl),int((screen_width/4)*sfl),int((screen_height/4)*sfl))
        #self.layoutMain =self.findChild(QtWidgets.QLayout,'layoutMain')
        self.PushQuit = self.findChild(PushButton,'PushQuit')
        self.PushGMY.clicked.connect(self.Call_GMY)
        self.PushQM.clicked.connect(self.Call_QM)
        self.PushQuit.clicked.connect(self.Call_Quit)
        

    def Call_GMY(self):
        main_gmy.show()

    def Call_QM(self):
        qmmain_qm.show()

    def Call_Quit(self):
        self.close()

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    main=CallMain()
    main_gmy = call_main.CallMain()
    qmmain_qm = main_qm.CallMain()
    main.show()
    sys.exit(app.exec_())