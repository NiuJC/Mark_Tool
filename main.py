import sys

from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

import main_win
from manual import Manual


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent=parent)
        ui= main_win.Ui_Marking_System()
        ui.setupUi(self)

    def help(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '帮助', '视频情感数据标注系统帮助文档')
        msgBox.exec_()

    def about_us(self):
        msgBox=QMessageBox(QMessageBox.NoIcon,'关于','视频情感数据标注系统')
        msgBox.setIconPixmap(QPixmap("./YYY.jpg"))
        msgBox.exec_()

    def jump_to_manual(self):
        self.ui_1 = Manual()
        self.ui_1.show()

    #def jump_to_machine(self):
        #self.ui_2 = Machine()
        #self.ui_2.show()

    def jump_to_analysis(self):
        pass

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    ui=MainWindow()
    ui.show()
    sys.exit(app.exec_())