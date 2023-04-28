
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

from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QImage


class FlatButton(QLabel):
    clickedWithReturn = Signal(object)
    clicked = Signal()

    def __init__(self, normal_icon = ":/images/edit_normal.png", hover_icon = ":/images/edit_normal.png", pressed_icon = "", disabled_icon = ""):
        QLabel.__init__(self)

        self.enabled = True
        self.returncode = ""
        
        self.normal_icon = QPixmap.fromImage(QImage(normal_icon))
        self.hover_icon = QPixmap.fromImage(QImage(hover_icon))

        if not pressed_icon :
            self.pressed_icon = QPixmap.fromImage(QImage(hover_icon))
        else:
            self.pressed_icon = QPixmap.fromImage(QImage(pressed_icon))

        if not disabled_icon:
            self.disabled_icon = QPixmap.fromImage(QImage(normal_icon))
        else:
            self.disabled_icon = QPixmap.fromImage(QImage(disabled_icon))

        self.setPixmap(self.normal_icon)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        if self.enabled:
            self.setPixmap(self.pressed_icon)
        self.setFocus()
        event.accept()

    def mouseReleaseEvent(self, event):
        if self.enabled:
            self.setPixmap(self.hover_icon)
        event.accept()
        if not self.returncode:
            self.clicked.emit()
        else:
            self.clickedWithReturn.emit(self.returncode)

    def enterEvent(self, event):
        if self.enabled:
            self.setPixmap(self.hover_icon)
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event):
        if self.enabled:
            self.setPixmap(self.normal_icon)
        QWidget.leaveEvent(self, event)

    def setNormalPixmap(self, pm):
        self.normal_icon = pm
        if not self.disabled_icon:
            self.disabled_icon = pm
        if not self.pressed_icon:
            self.pressed_icon = pm
        if not self.hover_icon:
            self.hover_icon = pm
        self.setPixmap(self.normal_icon)

    def setHoverPixmap(self, pm):
        self.hover_icon = pm
        if not self.pressed_icon:
            self.pressed_icon = pm
