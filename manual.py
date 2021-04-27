import os
import json

import time
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog, QLabel, QWidget, QHBoxLayout, \
    QListWidgetItem, QPushButton, QListWidget

from manual_win import Ui_Manual

data = {
    'Anger': 0,
    'Disgust': 0,
    'Fear': 0,
    'Happy': 0,
    'Surprise': 0,
    'Sad': 0,
    'Neutral': 0,
    'Unknown': 0
}
mark_list = ['Anger', 'Disgust', 'Fear', 'Happy', 'Surprise', 'Sad', 'Neutral', 'Unknown']
global vid_path     #视频库url
global path_list    #播放列表中视频url列表
path_list = []
global name_list
name_list = []
global cur_vid
cur_vid = -1
global vid_num
vid_num = 0

global is_marked
is_marked = []

class Manual(QMainWindow, Ui_Manual):
    def __init__(self, parent=None):
        super(Manual, self).__init__(parent=parent)
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget_videoplay)
        self.sld_video_pressed = False
        self.player.positionChanged.connect(self.change_sld)

        self.clicked()
        self.slider()

    # 帮助文档
    def help(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '帮助', '视频情感数据标注系统帮助文档')
        msgBox.exec_()

    # 关于
    def about_us(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', '视频情感数据标注系统')
        msgBox.setIconPixmap(QPixmap("./YYY.jpg"))
        msgBox.exec_()

# --------------------------------------- 视频播放部分 ---------------------------------------------- #

    # 选择视频播放库
    def select_vid(self):
        file = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        if file != '':
            global vid_path
            vid_path = file
            self.play_l(file)
            # print(vid_path)

    # 获取视频播放路径
    def get_video_url(self):
        global cur_vid
        i = self.play_list.currentItem()
        cur_vid = self.play_list.row(i)
        url_str = path_list[cur_vid]
        url = QUrl(url_str)
        print(cur_vid)
        self.player.setMedia(QMediaContent(url))
        self.player.play()
        return url

    # 播放列表
    def play_l(self, video_dir):
        global path_list
        global vid_num
        global name_list
        path_list = []
        for root, dirs, files in os.walk(video_dir):
            for video_name in files:
                ext = os.path.splitext(video_name)[1]  # 获取后缀名
                if ext == '.mp4':
                    path_list.append(vid_path + "/" + video_name)
                    name_list.append(video_name)
                    vid_num += 1
                    self.add_video_item(video_name)
        for i in range(vid_num):
            is_marked.append(0)

        #print(is_marked)

        # print(vid_num)

    # 在播放列表添加单个视频
    def add_video_item(self, vid_name):
        ship_photo = 'D:/产学研/界面ui/test/t.png'
        # 总Widget
        wight = QListWidget()
        # 布局
        layout_main = QHBoxLayout()                            # 总体横向布局
        # 图片显示
        map_l = QLabel()
        map_l.setFixedSize(10, 10)
        maps = QPixmap(ship_photo).scaled(15, 15)
        map_l.setPixmap(maps)
        layout_left = QHBoxLayout()                            # 左边的横向布局
        layout_right = QHBoxLayout()                           # 右边的横向布局
        layout_left.addWidget(map_l)
        layout_right.addWidget(QLabel(vid_name))
        layout_main.addLayout(layout_left)                     # 右边布局填充入总布局
        layout_main.addLayout(layout_right)
        wight.setLayout(layout_main)                           # 为Widget设置总布局
        item = QListWidgetItem()                               # 创建QListWidgetItem对象
        item.setSizeHint(QSize(200, 50))                       # 设置QListWidgetItem大小
        widget = wight
        self.play_list.addItem(item)                           # 添加item
        self.play_list.setItemWidget(item, widget)             # 为item设置widget

    # 下一条视频
    def nextvideo(self):
        global vid_num, cur_vid
        print(vid_num)
        if cur_vid+1 == vid_num:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '已经是最后一条视频了！')
            msgBox.exec_()
        elif cur_vid <= vid_num-1:
            cur_vid += 1
            path = QUrl(path_list[cur_vid])
            self.player.setMedia(QMediaContent(path))
        elif cur_vid == -1:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '请先选择视频库！')
            msgBox.exec_()

            # 上一条视频
    def prevideo(self):
        global cur_vid
        if cur_vid > 0:
            cur_vid -= 1
            path = QUrl(path_list[cur_vid])
            self.player.setMedia(QMediaContent(path))
        elif cur_vid == -1:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '请先选择视频库！')
            msgBox.exec_()
        else:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '已经是第一条视频了！')
            msgBox.exec_()

    # 暂停
    def pause_video(self):
        self.player.pause()

    # 视频播放
    def play_video(self):
        self.player.play()

    def move_sld(self, position):
        self.sld_video_pressed = True
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            #self.lab_video.setText("%.2f%%" % position)

    def press_sld(self):
        self.sld_video_pressed = True
        print("pressed")

    def release_sld(self):
        self.sld_video_pressed = False

    def change_sld(self, position):
        if not self.sld_video_pressed:  # 进度条被鼠标点击时不更新
            #position = self.player.position()
            self.videoLength = self.player.duration() + 0.1
            self.play_slider.setValue(round((position / self.videoLength) * 100))

    def click_sld(self, position):
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
        else:
            self.play_slider.setValue(0)

# ------------------------------------------ 标签部分 ----------------------------------------------#

    # 提交
    def submit(self):
        global name_list
        global cur_vid

        if cur_vid == -1:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提醒', '请先选择要标注的视频！')
            msgBox.exec_()
        else:
            items = []
            res = data
            count = self.mark_list.count()                    # 获取mark_list中条目数
            if count == 0:
                msgBox = QMessageBox(QMessageBox.NoIcon, '提醒', '请先选择情感标签！')
                msgBox.exec_()
            else:
                print(count)
                for i in range(count):                            # 遍历mark_list中的内容
                    items.append(self.mark_list.item(i).text())
                for i in range(count):
                    res[items[i]] = 1
                json_res = json.dumps(res, sort_keys=True, indent=4, separators=(',', ':'))
                filename = 'result/'+name_list[cur_vid]+'.json'
                with open(filename, 'w') as f:
                    f.write(json_res)
                for i in mark_list:
                    res[i] = 0

                is_marked[cur_vid] = 1         # 标记过了就设为1
                self.mark_list.clear()         # 清除已选择的标签
                self.nextvideo()
                self.player.play()

    # 显示已经标注过视频的情感标签
    def display_marked(self):
        pass

    # 视频标签选择
    def is_anger(self):
        self.btn_anger.clicked.connect(lambda: self.add_mark_item("Anger"))

    def is_disgust(self):
        self.btn_disgust.clicked.connect(lambda: self.add_mark_item("Disgust"))

    def is_fear(self):
        self.btn_fear.clicked.connect(lambda: self.add_mark_item("Fear"))

    def is_happy(self):
        self.btn_happy.clicked.connect(lambda: self.add_mark_item("Happy"))

    def is_surprise(self):
        self.btn_surprise.clicked.connect(lambda: self.add_mark_item("Surprise"))

    def is_sad(self):
        self.btn_sad.clicked.connect(lambda: self.add_mark_item("Sad"))

    def is_neutral(self):
        self.btn_neutral.clicked.connect(lambda: self.add_mark_item("Neutral"))

    def is_unknown(self):
        self.btn_unknown.clicked.connect(lambda: self.add_mark_item("Unknown"))

    def add_mark_item(self, mark):
        self.mark_list.addItem(mark)

    def remove_mark(self):
        i = self.mark_list.currentItem()
        self.mark_list.takeItem(self.mark_list.row(i))

# -------------------------------------------事件响应函数-------------------------------------------- #
    # 鼠标点击事件
    def clicked(self):
        # 添加标签
        self.is_happy()
        self.is_sad()
        self.is_neutral()
        self.is_unknown()
        self.is_anger()
        self.is_fear()
        self.is_disgust()
        self.is_surprise()
        # 删除标签
        self.mark_list.itemClicked.connect(lambda: self.remove_mark())
        # 提交
        self.btn_submit.clicked.connect(lambda: self.submit())
        # 选择视频
        self.btn_select_vid.clicked.connect(lambda: self.select_vid())
        # 从播放列表选择视频
        self.play_list.itemClicked.connect(lambda: self.get_video_url())
        # 播放视频
        self.btn_play.clicked.connect(lambda: self.play_video())
        # 暂停视频
        self.btn_pause.clicked.connect(lambda: self.pause_video())
        # 下一条
        self.btn_next_vid.clicked.connect(lambda: self.nextvideo())
        # 上一条
        self.btn_pre_vid.clicked.connect(lambda: self.prevideo())

    # 进度条
    def slider(self):
        self.play_slider.setTracking(False)
        self.play_slider.sliderReleased.connect(self.release_sld)
        self.play_slider.sliderPressed.connect(self.press_sld)
        self.play_slider.sliderMoved.connect(self.move_sld)         # 进度条滑动跳转
        self.play_slider.ClickedValue.connect(self.click_sld)       # 进度条点击跳转


