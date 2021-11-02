# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogEpic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgEpic(object):
    def setupUi(self, dlgEpic):
        if not dlgEpic.objectName():
            dlgEpic.setObjectName(u"dlgEpic")
        dlgEpic.resize(487, 378)
        icon = QIcon()
        icon.addFile(u"../../../Bilder/Icons/icons8-europa-96.png", QSize(), QIcon.Normal, QIcon.Off)
        dlgEpic.setWindowIcon(icon)
        self.actionGetEpic = QAction(dlgEpic)
        self.actionGetEpic.setObjectName(u"actionGetEpic")
        self.layoutWidget = QWidget(dlgEpic)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 436, 61))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbDatum = QLabel(self.layoutWidget)
        self.lbDatum.setObjectName(u"lbDatum")

        self.horizontalLayout.addWidget(self.lbDatum)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.layoutWidget1 = QWidget(dlgEpic)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(170, 320, 285, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buttonBox = QDialogButtonBox(self.layoutWidget1)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.gbTransfer = QGroupBox(dlgEpic)
        self.gbTransfer.setObjectName(u"gbTransfer")
        self.gbTransfer.setGeometry(QRect(200, 180, 251, 121))
        self.gbTransfer.setStyleSheet(u"QGroupBox { background-color:  rgb(185,211,238); border: 3px solid rgb(255, 0, 0); }")
        self.progressBar = QProgressBar(self.gbTransfer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 80, 118, 23))
        self.progressBar.setValue(0)
        self.widget = QWidget(self.gbTransfer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 239, 20))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbCountPreText = QLabel(self.widget)
        self.lbCountPreText.setObjectName(u"lbCountPreText")

        self.horizontalLayout_5.addWidget(self.lbCountPreText)

        self.lbActualCount = QLabel(self.widget)
        self.lbActualCount.setObjectName(u"lbActualCount")
        self.lbActualCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lbActualCount)

        self.lbConstSlash = QLabel(self.widget)
        self.lbConstSlash.setObjectName(u"lbConstSlash")

        self.horizontalLayout_5.addWidget(self.lbConstSlash)

        self.lbConstCount = QLabel(self.widget)
        self.lbConstCount.setObjectName(u"lbConstCount")

        self.horizontalLayout_5.addWidget(self.lbConstCount)

        self.lbFileID = QLabel(self.gbTransfer)
        self.lbFileID.setObjectName(u"lbFileID")
        self.lbFileID.setGeometry(QRect(10, 30, 31, 18))
        self.lbFileIDName = QLabel(self.gbTransfer)
        self.lbFileIDName.setObjectName(u"lbFileIDName")
        self.lbFileIDName.setGeometry(QRect(50, 30, 171, 18))
        self.lbFileIDName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget2 = QWidget(dlgEpic)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 130, 441, 36))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cbNaturalEnhanced = QComboBox(self.layoutWidget2)
        self.cbNaturalEnhanced.addItem("")
        self.cbNaturalEnhanced.addItem("")
        self.cbNaturalEnhanced.setObjectName(u"cbNaturalEnhanced")

        self.horizontalLayout_3.addWidget(self.cbNaturalEnhanced)

        self.cbDatesAvailable = QComboBox(self.layoutWidget2)
        self.cbDatesAvailable.addItem("")
        self.cbDatesAvailable.addItem("")
        self.cbDatesAvailable.addItem("")
        self.cbDatesAvailable.setObjectName(u"cbDatesAvailable")

        self.horizontalLayout_3.addWidget(self.cbDatesAvailable)

        self.horizontalSpacer = QSpacerItem(108, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pbGetEpic = QPushButton(self.layoutWidget2)
        self.pbGetEpic.setObjectName(u"pbGetEpic")

        self.horizontalLayout_3.addWidget(self.pbGetEpic)


        self.retranslateUi(dlgEpic)
        self.buttonBox.accepted.connect(dlgEpic.accept)
        self.buttonBox.rejected.connect(dlgEpic.reject)
        self.pbGetEpic.clicked.connect(self.actionGetEpic.trigger)

        self.pbGetEpic.setDefault(True)


        QMetaObject.connectSlotsByName(dlgEpic)
    # setupUi

    def retranslateUi(self, dlgEpic):
        dlgEpic.setWindowTitle(QCoreApplication.translate("dlgEpic", u"EPIC (Earth Polychromatic Imaging Camera) Pictures", None))
        self.actionGetEpic.setText(QCoreApplication.translate("dlgEpic", u"GetEpic", None))
#if QT_CONFIG(tooltip)
        self.actionGetEpic.setToolTip(QCoreApplication.translate("dlgEpic", u"EPIC (Earth Polychromatic Imaging Camera) Pictures", None))
#endif // QT_CONFIG(tooltip)
        self.lbDatum.setText(QCoreApplication.translate("dlgEpic", u"Bitte Datum ausw\u00e4hlen:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("dlgEpic", u"dd.MM.yyyy", None))
        self.gbTransfer.setTitle(QCoreApplication.translate("dlgEpic", u"Speichern", None))
        self.lbCountPreText.setText(QCoreApplication.translate("dlgEpic", u"Dateien transferiert: ", None))
        self.lbActualCount.setText(QCoreApplication.translate("dlgEpic", u"0", None))
        self.lbConstSlash.setText(QCoreApplication.translate("dlgEpic", u"/", None))
        self.lbConstCount.setText(QCoreApplication.translate("dlgEpic", u"0", None))
        self.lbFileID.setText(QCoreApplication.translate("dlgEpic", u"ID:", None))
        self.lbFileIDName.setText("")
        self.cbNaturalEnhanced.setItemText(0, QCoreApplication.translate("dlgEpic", u"natural", None))
        self.cbNaturalEnhanced.setItemText(1, QCoreApplication.translate("dlgEpic", u"enhanced", None))

        self.cbDatesAvailable.setItemText(0, QCoreApplication.translate("dlgEpic", u"all", None))
        self.cbDatesAvailable.setItemText(1, QCoreApplication.translate("dlgEpic", u"available", None))
        self.cbDatesAvailable.setItemText(2, QCoreApplication.translate("dlgEpic", u"date", None))

        self.pbGetEpic.setText(QCoreApplication.translate("dlgEpic", u"Ausf\u00fchren", None))
    # retranslateUi

