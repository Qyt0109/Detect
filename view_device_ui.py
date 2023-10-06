# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_device.ui'
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
        MainWindow.resize(700, 419)
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
        self.pushButton_menu = QPushButton(self.frame_image_status)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setIconSize(QSize(48, 48))

        self.horizontalLayout_4.addWidget(self.pushButton_menu)

        self.label_section_info = QLabel(self.frame_image_status)
        self.label_section_info.setObjectName(u"label_section_info")

        self.horizontalLayout_4.addWidget(self.label_section_info)


        self.horizontalLayout_2.addWidget(self.frame_image_status, 0, Qt.AlignLeft)

        self.frame = QFrame(self.frame_connection)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_bluetooth = QLabel(self.frame)
        self.label_bluetooth.setObjectName(u"label_bluetooth")
        self.label_bluetooth.setMinimumSize(QSize(28, 28))
        self.label_bluetooth.setMaximumSize(QSize(28, 28))
        self.label_bluetooth.setPixmap(QPixmap(u":/PNG/Resources/PNG/BluetoothOn.png"))
        self.label_bluetooth.setScaledContents(True)
        self.label_bluetooth.setIndent(2)

        self.horizontalLayout_3.addWidget(self.label_bluetooth)

        self.pushButton_noity = QPushButton(self.frame)
        self.pushButton_noity.setObjectName(u"pushButton_noity")

        self.horizontalLayout_3.addWidget(self.pushButton_noity)

        self.pushButton_power_off = QPushButton(self.frame)
        self.pushButton_power_off.setObjectName(u"pushButton_power_off")
        self.pushButton_power_off.setIconSize(QSize(48, 48))

        self.horizontalLayout_3.addWidget(self.pushButton_power_off)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_connection, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_5)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_slot1 = QPushButton(self.frame_menu)
        self.pushButton_slot1.setObjectName(u"pushButton_slot1")
        self.pushButton_slot1.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.pushButton_slot1)

        self.pushButton_slot2 = QPushButton(self.frame_menu)
        self.pushButton_slot2.setObjectName(u"pushButton_slot2")
        self.pushButton_slot2.setIconSize(QSize(48, 48))

        self.verticalLayout_6.addWidget(self.pushButton_slot2)


        self.horizontalLayout_10.addWidget(self.frame_menu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_capture_image = QWidget()
        self.page_capture_image.setObjectName(u"page_capture_image")
        self.horizontalLayout = QHBoxLayout(self.page_capture_image)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_image = QFrame(self.page_capture_image)
        self.frame_image.setObjectName(u"frame_image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_image.sizePolicy().hasHeightForWidth())
        self.frame_image.setSizePolicy(sizePolicy1)
        self.frame_image.setAutoFillBackground(False)
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_image)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_image = QLabel(self.frame_image)
        self.label_image.setObjectName(u"label_image")
        font = QFont()
        font.setPointSize(48)
        self.label_image.setFont(font)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_image)

        self.frame_info = QFrame(self.page_capture_image)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_info)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_info_header = QLabel(self.frame_info)
        self.label_info_header.setObjectName(u"label_info_header")
        self.label_info_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_info_header, 0, Qt.AlignTop)

        self.plainTextEdit_info = QPlainTextEdit(self.frame_info)
        self.plainTextEdit_info.setObjectName(u"plainTextEdit_info")
        font1 = QFont()
        font1.setPointSize(18)
        self.plainTextEdit_info.setFont(font1)
        self.plainTextEdit_info.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_info)

        self.frame_3 = QFrame(self.frame_info)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_accept = QPushButton(self.frame_3)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        self.pushButton_accept.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.pushButton_accept, 0, Qt.AlignLeft)

        self.pushButton_send = QPushButton(self.frame_3)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.pushButton_send, 0, Qt.AlignVCenter)

        self.pushButton_delete = QPushButton(self.frame_3)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.pushButton_delete, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_info, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.page_capture_image)
        self.page_query = QWidget()
        self.page_query.setObjectName(u"page_query")
        self.horizontalLayout_9 = QHBoxLayout(self.page_query)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_image_query = QFrame(self.page_query)
        self.frame_image_query.setObjectName(u"frame_image_query")
        sizePolicy1.setHeightForWidth(self.frame_image_query.sizePolicy().hasHeightForWidth())
        self.frame_image_query.setSizePolicy(sizePolicy1)
        self.frame_image_query.setAutoFillBackground(False)
        self.frame_image_query.setFrameShape(QFrame.StyledPanel)
        self.frame_image_query.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_image_query)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_image_query = QLabel(self.frame_image_query)
        self.label_image_query.setObjectName(u"label_image_query")
        self.label_image_query.setFont(font)
        self.label_image_query.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_image_query, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.frame_image_query)

        self.frame_info_2 = QFrame(self.page_query)
        self.frame_info_2.setObjectName(u"frame_info_2")
        self.frame_info_2.setFrameShape(QFrame.StyledPanel)
        self.frame_info_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_info_header_query = QLabel(self.frame_info_2)
        self.label_info_header_query.setObjectName(u"label_info_header_query")
        self.label_info_header_query.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_info_header_query, 0, Qt.AlignTop)

        self.plainTextEdit_info_query = QPlainTextEdit(self.frame_info_2)
        self.plainTextEdit_info_query.setObjectName(u"plainTextEdit_info_query")
        self.plainTextEdit_info_query.setFont(font1)
        self.plainTextEdit_info_query.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.plainTextEdit_info_query)

        self.frame_4 = QFrame(self.frame_info_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_status_icon = QLabel(self.frame_2)
        self.label_status_icon.setObjectName(u"label_status_icon")

        self.horizontalLayout_5.addWidget(self.label_status_icon)

        self.label_status_info = QLabel(self.frame_2)
        self.label_status_info.setObjectName(u"label_status_info")
        self.label_status_info.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_status_info)


        self.horizontalLayout_7.addWidget(self.frame_2, 0, Qt.AlignBottom)

        self.pushButton_delete_query = QPushButton(self.frame_4)
        self.pushButton_delete_query.setObjectName(u"pushButton_delete_query")
        self.pushButton_delete_query.setIconSize(QSize(48, 48))

        self.horizontalLayout_7.addWidget(self.pushButton_delete_query, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.frame_query = QFrame(self.frame_info_2)
        self.frame_query.setObjectName(u"frame_query")
        self.frame_query.setFrameShape(QFrame.StyledPanel)
        self.frame_query.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_query)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_previous = QPushButton(self.frame_query)
        self.pushButton_previous.setObjectName(u"pushButton_previous")
        self.pushButton_previous.setEnabled(False)
        self.pushButton_previous.setIconSize(QSize(48, 48))

        self.horizontalLayout_8.addWidget(self.pushButton_previous)

        self.label_index = QLabel(self.frame_query)
        self.label_index.setObjectName(u"label_index")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.label_index.setFont(font2)
        self.label_index.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_index)

        self.pushButton_next = QPushButton(self.frame_query)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setIconSize(QSize(48, 48))

        self.horizontalLayout_8.addWidget(self.pushButton_next)


        self.verticalLayout_5.addWidget(self.frame_query, 0, Qt.AlignBottom)


        self.horizontalLayout_9.addWidget(self.frame_info_2, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_query)
        self.page_noity = QWidget()
        self.page_noity.setObjectName(u"page_noity")
        self.horizontalLayout_11 = QHBoxLayout(self.page_noity)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_6 = QFrame(self.page_noity)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_noity_header = QFrame(self.frame_6)
        self.frame_noity_header.setObjectName(u"frame_noity_header")
        self.frame_noity_header.setFrameShape(QFrame.StyledPanel)
        self.frame_noity_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_noity_header)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_noity_header)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_noity_header_icon = QLabel(self.frame_10)
        self.label_noity_header_icon.setObjectName(u"label_noity_header_icon")

        self.horizontalLayout_15.addWidget(self.label_noity_header_icon)

        self.label_noity_header_info = QLabel(self.frame_10)
        self.label_noity_header_info.setObjectName(u"label_noity_header_info")
        self.label_noity_header_info.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_noity_header_info)


        self.horizontalLayout_12.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.pushButton_noity_clear = QPushButton(self.frame_noity_header)
        self.pushButton_noity_clear.setObjectName(u"pushButton_noity_clear")

        self.horizontalLayout_12.addWidget(self.pushButton_noity_clear, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_noity_header, 0, Qt.AlignTop)

        self.frame_noity_body = QFrame(self.frame_6)
        self.frame_noity_body.setObjectName(u"frame_noity_body")
        sizePolicy.setHeightForWidth(self.frame_noity_body.sizePolicy().hasHeightForWidth())
        self.frame_noity_body.setSizePolicy(sizePolicy)
        self.frame_noity_body.setFrameShape(QFrame.StyledPanel)
        self.frame_noity_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_noity_body)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_noity_body_info = QLabel(self.frame_noity_body)
        self.label_noity_body_info.setObjectName(u"label_noity_body_info")
        sizePolicy.setHeightForWidth(self.label_noity_body_info.sizePolicy().hasHeightForWidth())
        self.label_noity_body_info.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(36)
        self.label_noity_body_info.setFont(font3)
        self.label_noity_body_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_noity_body_info)


        self.verticalLayout_7.addWidget(self.frame_noity_body)

        self.frame_noity_footer = QFrame(self.frame_6)
        self.frame_noity_footer.setObjectName(u"frame_noity_footer")
        self.frame_noity_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_noity_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_noity_footer)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_noity_ok = QPushButton(self.frame_noity_footer)
        self.pushButton_noity_ok.setObjectName(u"pushButton_noity_ok")

        self.horizontalLayout_14.addWidget(self.pushButton_noity_ok, 0, Qt.AlignHCenter)

        self.pushButton_noity_try_again = QPushButton(self.frame_noity_footer)
        self.pushButton_noity_try_again.setObjectName(u"pushButton_noity_try_again")

        self.horizontalLayout_14.addWidget(self.pushButton_noity_try_again, 0, Qt.AlignHCenter)

        self.pushButton_noity_cancel = QPushButton(self.frame_noity_footer)
        self.pushButton_noity_cancel.setObjectName(u"pushButton_noity_cancel")

        self.horizontalLayout_14.addWidget(self.pushButton_noity_cancel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_noity_footer, 0, Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_noity)

        self.horizontalLayout_10.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_menu.setText("")
        self.label_section_info.setText(QCoreApplication.translate("MainWindow", u"THI\u1ebeT B\u1eca TRUY C\u1eacP KHO D\u1eee LI\u1ec6U \u1ea2NH VI PH\u1ea0M", None))
        self.label_bluetooth.setText("")
        self.pushButton_noity.setText("")
        self.pushButton_power_off.setText("")
        self.pushButton_slot1.setText("")
        self.pushButton_slot2.setText("")
        self.label_image.setText("")
        self.label_info_header.setText(QCoreApplication.translate("MainWindow", u"Capture image", None))
        self.pushButton_accept.setText("")
        self.pushButton_send.setText("")
        self.pushButton_delete.setText("")
        self.label_image_query.setText("")
        self.label_info_header_query.setText(QCoreApplication.translate("MainWindow", u"Query image", None))
        self.label_status_icon.setText("")
        self.label_status_info.setText(QCoreApplication.translate("MainWindow", u"TR\u1ea0NG TH\u00c1I:\n"
"\u0110\u00e3 g\u1eedi", None))
        self.pushButton_delete_query.setText("")
        self.pushButton_previous.setText("")
        self.label_index.setText(QCoreApplication.translate("MainWindow", u"1/42", None))
        self.pushButton_next.setText("")
        self.label_noity_header_icon.setText("")
        self.label_noity_header_info.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng b\u00e1o", None))
        self.pushButton_noity_clear.setText("")
        self.label_noity_body_info.setText(QCoreApplication.translate("MainWindow", u"N\u1ed9i dung th\u00f4ng b\u00e1o", None))
        self.pushButton_noity_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_noity_try_again.setText(QCoreApplication.translate("MainWindow", u"Th\u1eed l\u1ea1i", None))
        self.pushButton_noity_cancel.setText(QCoreApplication.translate("MainWindow", u"Hu\u1ef7", None))
    # retranslateUi

