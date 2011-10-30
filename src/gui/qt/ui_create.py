# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created: Fri Oct 28 20:11:40 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(710, 368)
        Wizard.setWindowTitle(QtGui.QApplication.translate("Wizard", "Wizard", None, QtGui.QApplication.UnicodeUTF8))
        Wizard.setOptions(QtGui.QWizard.HaveHelpButton|QtGui.QWizard.IndependentPages)
        self.wizardPage_intro = QtGui.QWizardPage()
        self.wizardPage_intro.setTitle(QtGui.QApplication.translate("Wizard", "Tomb", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_intro.setSubTitle(QtGui.QApplication.translate("Wizard", "tomb creation", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_intro.setObjectName(_fromUtf8("wizardPage_intro"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage_intro)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.wizardPage_intro)
        self.label.setText(QtGui.QApplication.translate("Wizard", "This wizard will guide you to the creation of a tomb.<br> It will be fun!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        Wizard.addPage(self.wizardPage_intro)
        self.wizardPage_tomb_size = QtGui.QWizardPage()
        self.wizardPage_tomb_size.setObjectName(_fromUtf8("wizardPage_tomb_size"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wizardPage_tomb_size)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.wizardPage_tomb_size)
        self.label_2.setText(QtGui.QApplication.translate("Wizard", "Please enter tomb size. Digging the tomb will require some time: usually, one minute per GB, but your mileage may vary. <br>Keep in mind that resizing it in the future is still NOT implemented", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.wizardPage_tomb_size)
        self.label_3.setText(QtGui.QApplication.translate("Wizard", "Enter tomb size, in MB. 1GB=1000MB)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_size = QtGui.QSpinBox(self.wizardPage_tomb_size)
        self.spinBox_size.setMinimum(10)
        self.spinBox_size.setMaximum(100000)
        self.spinBox_size.setProperty("value", 100)
        self.spinBox_size.setObjectName(_fromUtf8("spinBox_size"))
        self.horizontalLayout.addWidget(self.spinBox_size)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        Wizard.addPage(self.wizardPage_tomb_size)
        self.wizardPage_tomb_location = QtGui.QWizardPage()
        self.wizardPage_tomb_location.setObjectName(_fromUtf8("wizardPage_tomb_location"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.wizardPage_tomb_location)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.wizardPage_tomb_location)
        self.label_4.setText(QtGui.QApplication.translate("Wizard", "Where do you want your tomb to be digged?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_tombpath = QtGui.QLineEdit(self.wizardPage_tomb_location)
        self.lineEdit_tombpath.setFrame(True)
        self.lineEdit_tombpath.setPlaceholderText(QtGui.QApplication.translate("Wizard", "/path/to/file.tomb", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_tombpath.setObjectName(_fromUtf8("lineEdit_tombpath"))
        self.horizontalLayout_2.addWidget(self.lineEdit_tombpath)
        self.button_tombpath = QtGui.QPushButton(self.wizardPage_tomb_location)
        self.button_tombpath.setText(QtGui.QApplication.translate("Wizard", "Open file", None, QtGui.QApplication.UnicodeUTF8))
        self.button_tombpath.setObjectName(_fromUtf8("button_tombpath"))
        self.horizontalLayout_2.addWidget(self.button_tombpath)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        Wizard.addPage(self.wizardPage_tomb_location)
        self.wizardPage_key_location = QtGui.QWizardPage()
        self.wizardPage_key_location.setTitle(QtGui.QApplication.translate("Wizard", "Key creation", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_key_location.setSubTitle(QtGui.QApplication.translate("Wizard", "Choose the location for your key", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_key_location.setObjectName(_fromUtf8("wizardPage_key_location"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.wizardPage_key_location)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_5 = QtGui.QLabel(self.wizardPage_key_location)
        self.label_5.setText(QtGui.QApplication.translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Now, you have to decide where to put the <span style=\" font-weight:600;\">key</span> for your tomb<br />You should not leave your key at the door, as this will lower security A LOT</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Also, the keyfile is very small (less than a KB), so disk space is not an issue</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_6.addWidget(self.label_5)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radioButton_usb = QtGui.QRadioButton(self.wizardPage_key_location)
        self.radioButton_usb.setEnabled(False)
        self.radioButton_usb.setText(QtGui.QApplication.translate("Wizard", "On a USB pen (best security)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_usb.setCheckable(True)
        self.radioButton_usb.setChecked(False)
        self.radioButton_usb.setObjectName(_fromUtf8("radioButton_usb"))
        self.verticalLayout_4.addWidget(self.radioButton_usb)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(self.wizardPage_key_location)
        self.label_6.setEnabled(False)
        self.label_6.setText(QtGui.QApplication.translate("Wizard", "If you choose to do so, do not insert it NOW. Do it when you are asked to do so", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.radioButton_near = QtGui.QRadioButton(self.wizardPage_key_location)
        self.radioButton_near.setToolTip(QtGui.QApplication.translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It will be created as a regular file in the same directory of your tomb.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is much easier to use, but also much more <span style=\" font-style:italic;\">insecure</span>: all your security will be guaranteed by your <span style=\" font-weight:600;\">password</span>. If you really want to do this, choose a strong password (lot of random/non-dictionary words, spaces, numbers, odd characters)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_near.setText(QtGui.QApplication.translate("Wizard", "Near to the tomb itself (this is BAD)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_near.setChecked(True)
        self.radioButton_near.setObjectName(_fromUtf8("radioButton_near"))
        self.verticalLayout_5.addWidget(self.radioButton_near)
        self.radioButton_custom = QtGui.QRadioButton(self.wizardPage_key_location)
        self.radioButton_custom.setText(QtGui.QApplication.translate("Wizard", "Specify location", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_custom.setObjectName(_fromUtf8("radioButton_custom"))
        self.verticalLayout_5.addWidget(self.radioButton_custom)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit_custom = QtGui.QLineEdit(self.wizardPage_key_location)
        self.lineEdit_custom.setEnabled(False)
        self.lineEdit_custom.setObjectName(_fromUtf8("lineEdit_custom"))
        self.horizontalLayout_3.addWidget(self.lineEdit_custom)
        self.pushButton_custom = QtGui.QPushButton(self.wizardPage_key_location)
        self.pushButton_custom.setEnabled(False)
        self.pushButton_custom.setText(QtGui.QApplication.translate("Wizard", "Choose location", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_custom.setObjectName(_fromUtf8("pushButton_custom"))
        self.horizontalLayout_3.addWidget(self.pushButton_custom)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.label_11 = QtGui.QLabel(self.wizardPage_key_location)
        self.label_11.setText(QtGui.QApplication.translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Help: </span>the key file is very small, so disk usage is not an issue</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_6.addWidget(self.label_11)
        Wizard.addPage(self.wizardPage_key_location)
        self.wizardPage_progress = QtGui.QWizardPage()
        self.wizardPage_progress.setTitle(QtGui.QApplication.translate("Wizard", "Creating", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_progress.setSubTitle(QtGui.QApplication.translate("Wizard", "Please wait", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage_progress.setObjectName(_fromUtf8("wizardPage_progress"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.wizardPage_progress)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.progressBar = QtGui.QProgressBar(self.wizardPage_progress)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_7.addWidget(self.progressBar)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_progress = QtGui.QLabel(self.wizardPage_progress)
        self.label_progress.setText(QtGui.QApplication.translate("Wizard", "Creating tomb, please wait...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_progress.setObjectName(_fromUtf8("label_progress"))
        self.horizontalLayout_5.addWidget(self.label_progress)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.textBrowser_log = QtGui.QTextBrowser(self.wizardPage_progress)
        self.textBrowser_log.setDocumentTitle(QtGui.QApplication.translate("Wizard", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_log.setHtml(QtGui.QApplication.translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Log</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Log</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_log.setObjectName(_fromUtf8("textBrowser_log"))
        self.verticalLayout_9.addWidget(self.textBrowser_log)
        Wizard.addPage(self.wizardPage_progress)
        self.wizardPage_end = QtGui.QWizardPage()
        self.wizardPage_end.setObjectName(_fromUtf8("wizardPage_end"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.wizardPage_end)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_10 = QtGui.QLabel(self.wizardPage_end)
        self.label_10.setText(QtGui.QApplication.translate("Wizard", "You successfully created the tomb!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_8.addWidget(self.label_10)
        self.checkBox_open = QtGui.QCheckBox(self.wizardPage_end)
        self.checkBox_open.setText(QtGui.QApplication.translate("Wizard", "Open the just-created tomb NOW!", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_open.setChecked(True)
        self.checkBox_open.setTristate(False)
        self.checkBox_open.setObjectName(_fromUtf8("checkBox_open"))
        self.verticalLayout_8.addWidget(self.checkBox_open)
        Wizard.addPage(self.wizardPage_end)
        self.label_3.setBuddy(self.spinBox_size)
        self.label_4.setBuddy(self.lineEdit_tombpath)

        self.retranslateUi(Wizard)
        QtCore.QObject.connect(self.radioButton_custom, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_custom.setEnabled)
        QtCore.QObject.connect(self.radioButton_custom, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.pushButton_custom.setEnabled)
        QtCore.QObject.connect(Wizard, QtCore.SIGNAL(_fromUtf8("currentIdChanged(int)")), self.label_11.hide)
        QtCore.QObject.connect(Wizard, QtCore.SIGNAL(_fromUtf8("helpRequested()")), self.label_11.show)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        pass

