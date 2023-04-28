#############################################################################
# Copyright (C) 2023 CrowdWare
#
# This file is part of AzerothClient.
#
#  AzerothClient is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  AzerothClient is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with AzerothClient.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import azerothlib
import asyncio
from enum import Enum
from widgets.flatbutton import FlatButton
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QWidget, QCheckBox, QDockWidget, QComboBox, QTabWidget, QLineEdit, QLabel, QListWidget, QListWidgetItem
from PySide6.QtCore import Signal, Qt, QUrl, QRect, QCoreApplication, QDir, QSettings, QByteArray, QEvent, QSize, QPoint, QAbstractAnimation, QPropertyAnimation
from PySide6.QtQml import QQmlEngine, QQmlComponent
from PySide6.QtGui import QUndoStack, QScreen
from PySide6.QtWebEngineWidgets import QWebEngineView
import resources

# just testing the lib
print(azerothlib.add(3,4))
print(azerothlib.sub(5,1))

calculator_instance = azerothlib.Calculator()
print(calculator_instance.add(2, 3))


class Cls(Enum):
    Warrior = 1,
    Paladin = 2,
    Hunter = 3,
    Rogue = 4,
    Priest = 5,
    DeathKnight = 6,
    Shaman = 7,
    Mage = 8,
    Warlock = 9,
    Druid = 11


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initGui()
        self.readSettings()
        self.statusBar().showMessage(QCoreApplication.translate("MainWindow", "Ready"))

    def closeEvent(self, event):
        self.writeSettings()
        event.accept()

    def writeSettings(self):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, QCoreApplication.organizationName(), QCoreApplication.applicationName())
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())
        settings.setValue("state", self.saveState())
        settings.setValue("host", self.host.text())
        settings.setValue("master", self.master.text())

    def readSettings(self):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, QCoreApplication.organizationName(), QCoreApplication.applicationName())
        pos = settings.value('pos', QPoint(200, 200))
        size = settings.value('size', QSize(400, 400))
        self.move(pos)
        self.resize(size)
        self.restoreState(settings.value("state"))
        self.host.setText(settings.value("host"))
        self.master.setText(settings.value("master"))
        newItem = QListWidgetItem()
        newItem.setText("Eya Priest (3)")
        self.botlist.addItem(newItem)
        newItem = QListWidgetItem()
        newItem.setText("Nebulus Warlock (2)")
        self.botlist.addItem(newItem)

    def initGui(self):
        self.installEventFilter(self)
        self.setWindowTitle(QCoreApplication.applicationName() + " " + QCoreApplication.applicationVersion())
        vbox = QVBoxLayout()
        self.host = QLineEdit()
        self.master = QLineEdit()
        self.botlist = QListWidget()
        vbox.addWidget(QLabel("Host"))
        vbox.addWidget(self.host)
        vbox.addWidget(QLabel("Master"))
        vbox.addWidget(self.master)
        vbox.addWidget(QLabel("Bots"))
        vbox.addWidget(self.botlist)
        
        vln = QHBoxLayout()
        buttonsn = QWidget()
        buttonsn.setLayout(vln)
        addButton = QPushButton("Add")
        vln.addWidget(addButton)
        delButton = QPushButton("Delete")
        vln.addWidget(delButton)
        vln.addStretch() 
        vbox.addWidget(buttonsn)
        content = QWidget()
        content.setLayout(vbox)

        self.navigationdock = QDockWidget(QCoreApplication.translate("MainWindow", "Navigation"), self)
        self.navigationdock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.navigationdock.setWidget(content)
        self.navigationdock.setObjectName("Navigation")
        self.addDockWidget(Qt.LeftDockWidgetArea, self.navigationdock)

        dl = QVBoxLayout()
        dl.addWidget(QLabel("Accountname"))
        self.accountname = QLineEdit()
        self.accountname.setMaximumWidth(200)
        dl.addWidget(self.accountname)
        dl.addWidget(QLabel("Password"))
        self.password = QLineEdit()
        self.password.setMaximumWidth(200)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        dl.addWidget(self.password)
        dl.addWidget(QLabel("Charname"))
        self.charname = QLineEdit()
        self.charname.setMaximumWidth(200)
        dl.addWidget(self.charname)
        self.classname = QComboBox()
        self.classname.setMaximumWidth(200)
        classnames = [cls.name for cls in Cls]
        self.classname.addItems(classnames)
        dl.addWidget(self.classname)
        self.start = QCheckBox("Start")
        dl.addWidget(self.start)
        dl.addStretch()
        tabDetails = QWidget()
        tabDetails.setLayout(dl)
        tabpage = QTabWidget()
        tabpage.addTab(tabDetails, "Details")
        tabScript = QWidget()
        tabpage.addTab(tabScript, "Script")
        ml = QVBoxLayout()
        vl = QHBoxLayout()
        bg = QWidget()
        bg.setLayout(ml)
        buttons = QWidget()
        buttons.setLayout(vl)
        ml.addWidget(tabpage)
        vl.addStretch()
        stopButton = QPushButton("Stop")
        stopButton.setEnabled(False)
        vl.addWidget(stopButton)
        startButton = QPushButton("Start")
        vl.addWidget(startButton)
        ml.addWidget(buttons)
        self.setCentralWidget(bg)

        self.showDock = FlatButton(":/images/edit_normal.png", ":/images/edit_hover.png")
        self.showDock.setToolTip(QCoreApplication.translate("MainWindow", "Show Navigation"))
        self.statusBar().addPermanentWidget(self.showDock)
        self.navigationdock.visibilityChanged.connect(self.dockVisibilityChanged)
        self.showDock.clicked.connect(self.showMenu)

    def dockVisibilityChanged(self, visible):
        self.showDock.setVisible(not visible)

    def showMenu(self):
        self.navigationdock.setVisible(True) 

