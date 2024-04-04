# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(140, 550, 101, 31))
        self.idx_show = QLabel(Widget)
        self.idx_show.setObjectName("idx_show")
        self.idx_show.setGeometry(QRect(140, 510, 101, 31))
        self.idx_label = QLabel(Widget)
        self.idx_label.setObjectName("idx_label")
        self.idx_label.setGeometry(QRect(70, 510, 71, 31))
        self.jump_button = QPushButton(Widget)
        self.jump_button.setObjectName("jump_button")
        self.jump_button.setGeometry(QRect(250, 550, 111, 31))
        self.textBrowser_1 = QTextBrowser(Widget)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.textBrowser_1.setGeometry(QRect(80, 200, 311, 141))
        self.textBrowser_2 = QTextBrowser(Widget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(470, 200, 301, 141))
        self.textBrowser_3 = QTextBrowser(Widget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(80, 350, 311, 141))
        self.textBrowser_4 = QTextBrowser(Widget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(470, 350, 301, 141))
        self.textBrowsers = [self.textBrowser_1, self.textBrowser_2, self.textBrowser_3, self.textBrowser_4]
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(250, 510, 121, 31))
        self.progressBar.setValue(0)
        self.dst_label = QLabel(Widget)
        self.dst_label.setObjectName("dst_label")
        self.dst_label.setGeometry(QRect(70, 550, 71, 31))
        self.label_1 = QLabel(Widget)
        self.label_1.setObjectName("label_1")
        self.label_1.setGeometry(QRect(50, 260, 16, 21))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(440, 260, 16, 21))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(50, 410, 16, 21))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(440, 410, 16, 21))
        self.prev_button = QPushButton(Widget)
        self.prev_button.setObjectName("prev_button")
        self.prev_button.setGeometry(QRect(390, 510, 91, 31))
        self.next_button = QPushButton(Widget)
        self.next_button.setObjectName("next_button")
        self.next_button.setGeometry(QRect(390, 550, 91, 31))
        self.lineEdit_1 = QLineEdit(Widget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(510, 550, 31, 31))
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(580, 550, 31, 31))
        self.lineEdit_3 = QLineEdit(Widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(650, 550, 31, 31))
        self.lineEdit_4 = QLineEdit(Widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(720, 550, 31, 31))
        self.lineEdits = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4]
        self.tips_label = QLabel(Widget)
        self.tips_label.setObjectName("tips_label")
        self.tips_label.setGeometry(QRect(510, 509, 151, 31))
        self.greater_label_1 = QLabel(Widget)
        self.greater_label_1.setObjectName("greater_label_1")
        self.greater_label_1.setGeometry(QRect(560, 550, 16, 31))
        self.greater_label_2 = QLabel(Widget)
        self.greater_label_2.setObjectName("greater_label_2")
        self.greater_label_2.setGeometry(QRect(630, 550, 16, 31))
        self.greater_label_3 = QLabel(Widget)
        self.greater_label_3.setObjectName("greater_label_3")
        self.greater_label_3.setGeometry(QRect(700, 550, 16, 31))
        self.save_button = QPushButton(Widget)
        self.save_button.setObjectName("save_button")
        self.save_button.setGeometry(QRect(670, 510, 91, 31))
        self.material_browser = QTextBrowser(Widget)
        self.material_browser.setObjectName("material_browser")
        self.material_browser.setGeometry(QRect(80, 40, 211, 121))
        self.instruct_browser = QTextBrowser(Widget)
        self.instruct_browser.setObjectName("instruct_browser")
        self.instruct_browser.setGeometry(QRect(360, 40, 411, 121))
        self.instruct_label = QLabel(Widget)
        self.instruct_label.setObjectName("instruct_label")
        self.instruct_label.setGeometry(QRect(35, 90, 31, 21))
        self.material_label = QLabel(Widget)
        self.material_label.setObjectName("material_label")
        self.material_label.setGeometry(QRect(320, 90, 31, 21))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle("标注工具")
        self.idx_label.setText("当前索引")
        self.idx_show.setText("0")
        self.jump_button.setText("跳转")
        self.dst_label.setText("目标索引")
        self.label_1.setText("1")
        self.label_2.setText("2")
        self.label_3.setText("3")
        self.label_4.setText("4")
        self.prev_button.setText("上一个")
        self.next_button.setText("下一个")
        self.save_button.setText("确认")
        self.lineEdit_1.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.tips_label.setText("请按顺序排列答案序号")
        self.greater_label_1.setText(">")
        self.greater_label_2.setText(">")
        self.greater_label_3.setText(">")
        self.instruct_label.setText("指令")
        self.material_label.setText("素材")

