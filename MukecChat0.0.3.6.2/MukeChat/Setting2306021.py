# -*- coding: utf-8 -*-
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QDialogButtonBox, QDesktopWidget

setting_date_path = 'mukechat_file/setting_date.txt'
setting_date = []
with open(setting_date_path, 'r') as f:
    setting_date = json.load(f)

icon_path = 'mukechat_file/logo.ico'


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 350)
        Dialog.setMinimumSize(QtCore.QSize(450, 350))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.key = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key.sizePolicy().hasHeightForWidth())
        self.key.setSizePolicy(sizePolicy)
        self.key.setMinimumSize(QtCore.QSize(50, 0))
        self.key.setMaximumSize(QtCore.QSize(150, 16777215))
        self.key.setAlignment(QtCore.Qt.AlignCenter)
        self.key.setObjectName("key")
        self.horizontalLayout_4.addWidget(self.key)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.key_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.key_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.key_lineEdit.setObjectName("key_lineEdit")
        self.horizontalLayout_4.addWidget(self.key_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.temperature = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperature.sizePolicy().hasHeightForWidth())
        self.temperature.setSizePolicy(sizePolicy)
        self.temperature.setMinimumSize(QtCore.QSize(120, 0))
        self.temperature.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("")
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")
        self.horizontalLayout_3.addWidget(self.temperature)
        self.temperature_horizontalSlider = QtWidgets.QSlider(Dialog)
        self.temperature_horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.temperature_horizontalSlider.setMaximum(200)
        self.temperature_horizontalSlider.setPageStep(1)
        self.temperature_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.temperature_horizontalSlider.setObjectName("temperature_horizontalSlider")
        self.horizontalLayout_3.addWidget(self.temperature_horizontalSlider)
        self.temperature_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.temperature_lineEdit.setEnabled(False)
        self.temperature_lineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.temperature_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.temperature_lineEdit.setObjectName("temperature_lineEdit")
        self.horizontalLayout_3.addWidget(self.temperature_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.max_tokens = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_tokens.sizePolicy().hasHeightForWidth())
        self.max_tokens.setSizePolicy(sizePolicy)
        self.max_tokens.setMinimumSize(QtCore.QSize(120, 0))
        self.max_tokens.setMaximumSize(QtCore.QSize(150, 16777215))
        self.max_tokens.setToolTip("")
        self.max_tokens.setAlignment(QtCore.Qt.AlignCenter)
        self.max_tokens.setObjectName("max_tokens")
        self.horizontalLayout_2.addWidget(self.max_tokens)
        self.max_tokens_horizontalSlider = QtWidgets.QSlider(Dialog)
        self.max_tokens_horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max_tokens_horizontalSlider.setMinimum(1)
        self.max_tokens_horizontalSlider.setMaximum(2048)
        self.max_tokens_horizontalSlider.setPageStep(1)
        self.max_tokens_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.max_tokens_horizontalSlider.setObjectName("max_tokens_horizontalSlider")
        self.horizontalLayout_2.addWidget(self.max_tokens_horizontalSlider)
        self.max_tokens_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.max_tokens_lineEdit.setEnabled(False)
        self.max_tokens_lineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.max_tokens_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.max_tokens_lineEdit.setObjectName("max_tokens_lineEdit")
        self.horizontalLayout_2.addWidget(self.max_tokens_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.top_p = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_p.sizePolicy().hasHeightForWidth())
        self.top_p.setSizePolicy(sizePolicy)
        self.top_p.setMinimumSize(QtCore.QSize(120, 0))
        self.top_p.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.top_p.setFont(font)
        self.top_p.setAutoFillBackground(False)
        self.top_p.setAlignment(QtCore.Qt.AlignCenter)
        self.top_p.setObjectName("top_p")
        self.horizontalLayout.addWidget(self.top_p)
        self.top_p_horizontalSlider = QtWidgets.QSlider(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_p_horizontalSlider.sizePolicy().hasHeightForWidth())
        self.top_p_horizontalSlider.setSizePolicy(sizePolicy)
        self.top_p_horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.top_p_horizontalSlider.setMaximum(100)
        self.top_p_horizontalSlider.setSingleStep(1)
        self.top_p_horizontalSlider.setPageStep(1)
        self.top_p_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.top_p_horizontalSlider.setObjectName("top_p_horizontalSlider")
        self.horizontalLayout.addWidget(self.top_p_horizontalSlider)
        self.top_p_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.top_p_lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_p_lineEdit.sizePolicy().hasHeightForWidth())
        self.top_p_lineEdit.setSizePolicy(sizePolicy)
        self.top_p_lineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.top_p_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.top_p_lineEdit.setObjectName("top_p_lineEdit")
        self.horizontalLayout.addWidget(self.top_p_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok).setText("确定")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("取消")
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)

        # 滚动条事件绑定
        self.temperature_horizontalSlider.valueChanged.connect(
            # self.temperature_num_change
            lambda num: self.temperature_lineEdit.setText(str(num / 100))
        )
        self.max_tokens_horizontalSlider.valueChanged.connect(
            # self.max_tokens_num_change
            lambda num: self.max_tokens_lineEdit.setText(str(num))
        )
        # 绑定匿名表达式都可以在文本框显示数值，全部绑定方法后不行了，最后一个要是匿名方法才行，不然就数据就不能显示文本框
        self.top_p_horizontalSlider.valueChanged.connect(
            # self.top_p_num_change
            lambda num: self.top_p_lineEdit.setText(str(num / 100))
        )

        self.buttonBox.accepted.connect(self.buttonBox_accepted)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def buttonBox_accepted(self):
        global setting_date
        setting_date = {
            'api_key': self.key_lineEdit.text(),
            'temperature': self.temperature_horizontalSlider.value() / 100,
            'max_tokens': self.max_tokens_horizontalSlider.value(),
            'top_p': self.top_p_horizontalSlider.value() / 100
        }
        with open(setting_date_path, 'w') as f:
            json.dump(setting_date, f)

        self.Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))
        Dialog.setWindowIcon(QIcon(icon_path))
        self.key.setText(_translate("Dialog", "密钥"))
        self.key_lineEdit.setPlaceholderText(_translate("Dialog", "输入你的密钥"))
        self.temperature.setText(_translate("Dialog", "temperature"))
        self.max_tokens.setText(_translate("Dialog", "max_tokens"))
        self.top_p.setText(_translate("Dialog", "top_p"))

    def data_init(self):
        self.key_lineEdit.setText(setting_date['api_key'])
        temperature = int(setting_date['temperature'] * 100)
        self.temperature_horizontalSlider.setValue(temperature)
        self.max_tokens_horizontalSlider.setValue(setting_date['max_tokens'])
        top_p = int(setting_date['top_p'] * 100)
        self.top_p_horizontalSlider.setValue(top_p)
        pass


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        center_pointer = QDesktopWidget().availableGeometry().center()
        print(center_pointer)
        x = center_pointer.x()
        y = center_pointer.y()
        win_w =770
        win_h =350
        self.move(x - win_w // 2, y - win_h // 2)

        dialog = Ui_Dialog()
        dialog.setupUi(self)
        dialog.data_init()


if __name__ == '__main__':
    app = QApplication([])
    dialog = MyDialog()
    dialog.show()
    app.exec()
