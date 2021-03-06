
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from mySlider import myVideoSlider

class Ui_Manual(object):
    def setupUi(self, Manual):
        Manual.setObjectName("Manual")
        Manual.resize(1395, 826)
        self.centralwidget = QtWidgets.QWidget(Manual)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_select_vid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select_vid.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.btn_select_vid.setObjectName("btn_select_vid")
        self.play_slider = myVideoSlider(self.centralwidget)
        self.play_slider.setGeometry(QtCore.QRect(280, 670, 891, 31))
        self.play_slider.setOrientation(QtCore.Qt.Horizontal)
        self.play_slider.setObjectName("play_slider")
        self.widget_videoplay = QVideoWidget(self.centralwidget)
        self.widget_videoplay.setGeometry(QtCore.QRect(290, 20, 881, 641))
        self.widget_videoplay.setStyleSheet("\n""background-image: url(:/pic/bg.jpg);")
        self.widget_videoplay.setObjectName("widget_videoplay")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1200, 500, 141, 21))
        self.label_2.setObjectName("label_2")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(1200, 720, 171, 31))
        self.btn_submit.setObjectName("btn_submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1200, 20, 211, 31))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.frame_num = QtWidgets.QLCDNumber(self.centralwidget)
        self.frame_num.setGeometry(QtCore.QRect(1100, 710, 71, 41))
        self.frame_num.setObjectName("frame_num")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1040, 710, 51, 41))
        self.label_3.setObjectName("label_3")
        self.play_list = QtWidgets.QListWidget(self.centralwidget)
        self.play_list.setGeometry(QtCore.QRect(10, 90, 251, 661))
        self.play_list.setObjectName("play_list")
        self.mark_list = QtWidgets.QListWidget(self.centralwidget)
        self.mark_list.setGeometry(QtCore.QRect(1200, 530, 171, 171))
        self.mark_list.setObjectName("mark_list")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1200, 50, 160, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_anger = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_anger.setObjectName("btn_anger")
        self.verticalLayout.addWidget(self.btn_anger)
        self.btn_disgust = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_disgust.setObjectName("btn_disgust")
        self.verticalLayout.addWidget(self.btn_disgust)
        self.btn_fear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_fear.setObjectName("btn_fear")
        self.verticalLayout.addWidget(self.btn_fear)
        self.btn_happy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_happy.setObjectName("btn_happy")
        self.verticalLayout.addWidget(self.btn_happy)
        self.btn_surprise = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_surprise.setObjectName("btn_surprise")
        self.verticalLayout.addWidget(self.btn_surprise)
        self.btn_sad = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_sad.setObjectName("btn_sad")
        self.verticalLayout.addWidget(self.btn_sad)
        self.btn_neutral = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_neutral.setObjectName("btn_neutral")
        self.verticalLayout.addWidget(self.btn_neutral)
        self.btn_unknown = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_unknown.setObjectName("btn_unknow")
        self.verticalLayout.addWidget(self.btn_unknown)
        self.btn_next_vid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next_vid.setGeometry(QtCore.QRect(860, 720, 111, 31))
        self.btn_next_vid.setObjectName("btn_next_vid")
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setGeometry(QtCore.QRect(570, 720, 111, 31))
        self.btn_play.setObjectName("btn_play")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(720, 720, 111, 31))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_pre_vid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pre_vid.setGeometry(QtCore.QRect(420, 720, 111, 31))
        self.btn_pre_vid.setObjectName("btn_pre_vid")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.label_4.setObjectName("label_4")
        Manual.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Manual)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1395, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Manual.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Manual)
        self.statusbar.setObjectName("statusbar")
        Manual.setStatusBar(self.statusbar)
        self.action_men = QtWidgets.QAction(Manual)
        self.action_men.setObjectName("action_men")
        self.action_machine = QtWidgets.QAction(Manual)
        self.action_machine.setObjectName("action_machine")
        self.actionhelp = QtWidgets.QAction(Manual)
        self.actionhelp.setObjectName("actionhelp")
        self.actionabout = QtWidgets.QAction(Manual)
        self.actionabout.setObjectName("actionabout")
        self.action_analysis = QtWidgets.QAction(Manual)
        self.action_analysis.setObjectName("action_analysis")
        self.actionpre_making = QtWidgets.QAction(Manual)
        self.actionpre_making.setObjectName("actionpre_making")
        self.menu.addAction(self.action_men)
        self.menu.addAction(self.action_machine)
        self.menu.addAction(self.action_analysis)
        self.menu.addAction(self.actionpre_making)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Manual)
        QtCore.QMetaObject.connectSlotsByName(Manual)

    def retranslateUi(self, Manual):
        _translate = QtCore.QCoreApplication.translate
        Manual.setWindowTitle(_translate("Manual", "MainWindow"))
        self.btn_select_vid.setText(_translate("Manual", "???????????????"))
        self.label_2.setText(_translate("Manual", "???????????????"))
        self.btn_submit.setText(_translate("Manual", "??????"))
        self.label.setText(_translate("Manual", "????????????"))
        self.label_3.setText(_translate("Manual", "?????????"))
        self.btn_anger.setText(_translate("Manual", "Anger"))
        self.btn_disgust.setText(_translate("Manual", "Disgust"))
        self.btn_fear.setText(_translate("Manual", "Fear"))
        self.btn_happy.setText(_translate("Manual", "Happy"))
        self.btn_surprise.setText(_translate("Manual", "Surprise"))
        self.btn_sad.setText(_translate("Manual", "Sad"))
        self.btn_neutral.setText(_translate("Manual", "Neutral"))
        self.btn_unknown.setText(_translate("Manual", "Unknown"))
        self.btn_next_vid.setText(_translate("Manual", "?????????"))
        self.btn_play.setText(_translate("Manual", "??????"))
        self.btn_pause.setText(_translate("Manual", "??????"))
        self.btn_pre_vid.setText(_translate("Manual", "?????????"))
        self.label_4.setText(_translate("Manual", "??????????????????"))
        self.menu.setTitle(_translate("Manual", "&??????"))
        self.action_men.setText(_translate("Manual", "welcome_window"))
        self.action_machine.setText(_translate("Manual", "machine_marking"))
        self.actionhelp.setText(_translate("Manual", "help"))
        self.actionabout.setText(_translate("Manual", "about"))
        self.action_analysis.setText(_translate("Manual", "analysis"))
        self.actionpre_making.setText(_translate("Manual", "pre_making"))


