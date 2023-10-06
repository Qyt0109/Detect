# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(603, 316)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_connection = QFrame(self.centralwidget)
        self.frame_connection.setObjectName(u"frame_connection")
        self.frame_connection.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);")
        self.frame_connection.setFrameShape(QFrame.StyledPanel)
        self.frame_connection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_connection)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 3, 10, 3)
        self.frame_image_status = QFrame(self.frame_connection)
        self.frame_image_status.setObjectName(u"frame_image_status")
        self.frame_image_status.setFrameShape(QFrame.StyledPanel)
        self.frame_image_status.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_image_status)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_image_status_icon = QLabel(self.frame_image_status)
        self.label_image_status_icon.setObjectName(u"label_image_status_icon")

        self.horizontalLayout_4.addWidget(self.label_image_status_icon)

        self.label_image_status_info = QLabel(self.frame_image_status)
        self.label_image_status_info.setObjectName(u"label_image_status_info")

        self.horizontalLayout_4.addWidget(self.label_image_status_info)

        self.label_map_icon = QLabel(self.frame_image_status)
        self.label_map_icon.setObjectName(u"label_map_icon")

        self.horizontalLayout_4.addWidget(self.label_map_icon)

        self.label_map_info = QLabel(self.frame_image_status)
        self.label_map_info.setObjectName(u"label_map_info")

        self.horizontalLayout_4.addWidget(self.label_map_info)


        self.horizontalLayout_2.addWidget(self.frame_image_status, 0, Qt.AlignLeft)

        self.frame = QFrame(self.frame_connection)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_bluetooth = QLabel(self.frame)
        self.label_bluetooth.setObjectName(u"label_bluetooth")

        self.horizontalLayout_3.addWidget(self.label_bluetooth)

        self.label_internet = QLabel(self.frame)
        self.label_internet.setObjectName(u"label_internet")

        self.horizontalLayout_3.addWidget(self.label_internet)

        self.label_server = QLabel(self.frame)
        self.label_server.setObjectName(u"label_server")

        self.horizontalLayout_3.addWidget(self.label_server)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_connection, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_capture_image = QWidget()
        self.page_capture_image.setObjectName(u"page_capture_image")
        self.horizontalLayout = QHBoxLayout(self.page_capture_image)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_camera = QFrame(self.page_capture_image)
        self.frame_camera.setObjectName(u"frame_camera")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_camera.sizePolicy().hasHeightForWidth())
        self.frame_camera.setSizePolicy(sizePolicy)
        self.frame_camera.setAutoFillBackground(False)
        self.frame_camera.setFrameShape(QFrame.StyledPanel)
        self.frame_camera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_camera)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_camera_frame = QLabel(self.frame_camera)
        self.label_camera_frame.setObjectName(u"label_camera_frame")

        self.verticalLayout_3.addWidget(self.label_camera_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_camera)

        self.frame_info = QFrame(self.page_capture_image)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.label_capture_image_info = QLabel(self.frame_info)
        self.label_capture_image_info.setObjectName(u"label_capture_image_info")

        self.verticalLayout.addWidget(self.label_capture_image_info, 0, Qt.AlignTop)

        self.plainTextEdit_history_event = QPlainTextEdit(self.frame_info)
        self.plainTextEdit_history_event.setObjectName(u"plainTextEdit_history_event")
        self.plainTextEdit_history_event.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_history_event)


        self.horizontalLayout.addWidget(self.frame_info, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.page_capture_image)
        self.page_view_image_info = QWidget()
        self.page_view_image_info.setObjectName(u"page_view_image_info")
        self.horizontalLayout_5 = QHBoxLayout(self.page_view_image_info)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_view_image = QFrame(self.page_view_image_info)
        self.frame_view_image.setObjectName(u"frame_view_image")
        sizePolicy.setHeightForWidth(self.frame_view_image.sizePolicy().hasHeightForWidth())
        self.frame_view_image.setSizePolicy(sizePolicy)
        self.frame_view_image.setFrameShape(QFrame.StyledPanel)
        self.frame_view_image.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_view_image)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_view_image = QLabel(self.frame_view_image)
        self.label_view_image.setObjectName(u"label_view_image")

        self.verticalLayout_5.addWidget(self.label_view_image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.frame_view_image)

        self.frame_3 = QFrame(self.page_view_image_info)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_view_image_info = QLabel(self.frame_3)
        self.label_view_image_info.setObjectName(u"label_view_image_info")

        self.verticalLayout_4.addWidget(self.label_view_image_info)

        self.plainTextEdit_view_image_info = QPlainTextEdit(self.frame_3)
        self.plainTextEdit_view_image_info.setObjectName(u"plainTextEdit_view_image_info")
        self.plainTextEdit_view_image_info.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.plainTextEdit_view_image_info)


        self.horizontalLayout_5.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_view_image_info)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.horizontalLayout_6 = QHBoxLayout(self.page_test)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_2 = QFrame(self.page_test)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_test_icon = QLabel(self.frame_4)
        self.label_test_icon.setObjectName(u"label_test_icon")

        self.horizontalLayout_7.addWidget(self.label_test_icon, 0, Qt.AlignLeft)

        self.label_test_info = QLabel(self.frame_4)
        self.label_test_info.setObjectName(u"label_test_info")
        sizePolicy.setHeightForWidth(self.label_test_info.sizePolicy().hasHeightForWidth())
        self.label_test_info.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_test_info)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.label_test_text = QLabel(self.frame_2)
        self.label_test_text.setObjectName(u"label_test_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_test_text.sizePolicy().hasHeightForWidth())
        self.label_test_text.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(24)
        self.label_test_text.setFont(font)
        self.label_test_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_test_text)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_test)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.frame_fn = QFrame(self.centralwidget)
        self.frame_fn.setObjectName(u"frame_fn")
        self.frame_fn.setFrameShape(QFrame.StyledPanel)
        self.frame_fn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_fn)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_fn1 = QPushButton(self.frame_fn)
        self.pushButton_fn1.setObjectName(u"pushButton_fn1")

        self.horizontalLayout_8.addWidget(self.pushButton_fn1)

        self.pushButton_fn2 = QPushButton(self.frame_fn)
        self.pushButton_fn2.setObjectName(u"pushButton_fn2")

        self.horizontalLayout_8.addWidget(self.pushButton_fn2)

        self.pushButton_fn3 = QPushButton(self.frame_fn)
        self.pushButton_fn3.setObjectName(u"pushButton_fn3")

        self.horizontalLayout_8.addWidget(self.pushButton_fn3)

        self.pushButton_fn4 = QPushButton(self.frame_fn)
        self.pushButton_fn4.setObjectName(u"pushButton_fn4")

        self.horizontalLayout_8.addWidget(self.pushButton_fn4)


        self.verticalLayout_2.addWidget(self.frame_fn, 0, Qt.AlignHCenter|Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_image_status_icon.setText("")
        self.label_image_status_info.setText("")
        self.label_map_icon.setText("")
        self.label_map_info.setText("")
        self.label_bluetooth.setText("")
        self.label_internet.setText("")
        self.label_server.setText("")
        self.label_camera_frame.setText("")
        self.label_capture_image_info.setText(QCoreApplication.translate("MainWindow", u"Capture image", None))
        self.label_view_image.setText("")
        self.label_view_image_info.setText(QCoreApplication.translate("MainWindow", u"Xem th\u00f4ng tin h\u00ecnh \u1ea3nh vi ph\u1ea1m", None))
        self.label_test_icon.setText("")
        self.label_test_info.setText(QCoreApplication.translate("MainWindow", u"G\u1eecI TH\u00c0NH C\u00d4NG", None))
        self.label_test_text.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e3 g\u1eedi c\u0103n c\u1ee9 vi ph\u1ea1m\n"
"T\u1ef1 \u0111\u1ed9ng \u0111\u00f3ng th\u00f4ng b\u00e1o n\u00e0y sau 3s", None))
        self.pushButton_fn1.setText("")
        self.pushButton_fn2.setText("")
        self.pushButton_fn3.setText("")
        self.pushButton_fn4.setText("")
    # retranslateUi

