# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogLyrics.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgLyrics(object):
    def setupUi(self, dlgLyrics):
        if not dlgLyrics.objectName():
            dlgLyrics.setObjectName(u"dlgLyrics")
        dlgLyrics.resize(493, 687)
        self.actionLyrics = QAction(dlgLyrics)
        self.actionLyrics.setObjectName(u"actionLyrics")
        self.actionTextSpeichern = QAction(dlgLyrics)
        self.actionTextSpeichern.setObjectName(u"actionTextSpeichern")
        self.buttonBox = QDialogButtonBox(dlgLyrics)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 640, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.gbLyrics = QGroupBox(dlgLyrics)
        self.gbLyrics.setObjectName(u"gbLyrics")
        self.gbLyrics.setGeometry(QRect(20, 30, 451, 131))
        self.layoutWidget = QWidget(self.gbLyrics)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 251, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbSinger = QLabel(self.layoutWidget)
        self.lbSinger.setObjectName(u"lbSinger")

        self.horizontalLayout.addWidget(self.lbSinger)

        self.leSinger = QLineEdit(self.layoutWidget)
        self.leSinger.setObjectName(u"leSinger")

        self.horizontalLayout.addWidget(self.leSinger)

        self.layoutWidget1 = QWidget(self.gbLyrics)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 251, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbSong = QLabel(self.layoutWidget1)
        self.lbSong.setObjectName(u"lbSong")

        self.horizontalLayout_2.addWidget(self.lbSong)

        self.leSong = QLineEdit(self.layoutWidget1)
        self.leSong.setObjectName(u"leSong")

        self.horizontalLayout_2.addWidget(self.leSong)

        self.pbSuchen = QPushButton(self.gbLyrics)
        self.pbSuchen.setObjectName(u"pbSuchen")
        self.pbSuchen.setGeometry(QRect(340, 70, 88, 34))
        self.teSongText = QTextEdit(dlgLyrics)
        self.teSongText.setObjectName(u"teSongText")
        self.teSongText.setGeometry(QRect(20, 200, 451, 411))
        self.lbText = QLabel(dlgLyrics)
        self.lbText.setObjectName(u"lbText")
        self.lbText.setGeometry(QRect(20, 170, 58, 18))
        self.pbSpeichern = QPushButton(dlgLyrics)
        self.pbSpeichern.setObjectName(u"pbSpeichern")
        self.pbSpeichern.setGeometry(QRect(20, 640, 88, 34))

        self.retranslateUi(dlgLyrics)
        self.buttonBox.accepted.connect(dlgLyrics.accept)
        self.buttonBox.rejected.connect(dlgLyrics.reject)
        self.pbSuchen.clicked.connect(self.actionLyrics.trigger)

        QMetaObject.connectSlotsByName(dlgLyrics)
    # setupUi

    def retranslateUi(self, dlgLyrics):
        dlgLyrics.setWindowTitle(QCoreApplication.translate("dlgLyrics", u"Song Texte", None))
        self.actionLyrics.setText(QCoreApplication.translate("dlgLyrics", u"Lyrics", None))
#if QT_CONFIG(tooltip)
        self.actionLyrics.setToolTip(QCoreApplication.translate("dlgLyrics", u"Suche Songtext", None))
#endif // QT_CONFIG(tooltip)
        self.actionTextSpeichern.setText(QCoreApplication.translate("dlgLyrics", u"TextSpeichern", None))
#if QT_CONFIG(tooltip)
        self.actionTextSpeichern.setToolTip(QCoreApplication.translate("dlgLyrics", u"Speichert angezeigten Liedtext", None))
#endif // QT_CONFIG(tooltip)
        self.gbLyrics.setTitle(QCoreApplication.translate("dlgLyrics", u"S\u00e4nger/Titel", None))
        self.lbSinger.setText(QCoreApplication.translate("dlgLyrics", u"S\u00e4nger:", None))
        self.lbSong.setText(QCoreApplication.translate("dlgLyrics", u"Lied:     ", None))
        self.pbSuchen.setText(QCoreApplication.translate("dlgLyrics", u"Suchen", None))
        self.lbText.setText(QCoreApplication.translate("dlgLyrics", u"Text:", None))
        self.pbSpeichern.setText(QCoreApplication.translate("dlgLyrics", u"Speichern", None))
    # retranslateUi

