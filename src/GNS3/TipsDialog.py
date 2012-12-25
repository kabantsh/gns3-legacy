# vim: expandtab ts=4 sw=4 sts=4 fileencoding=utf-8:
#
# Copyright (C) 2007-2010 GNS3 Development Team (http://www.gns3.net/team).
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# http://www.gns3.net/contact
#

from PyQt4 import QtCore, QtGui, QtWebKit
from GNS3.Ui.Form_TipsDialog import Ui_TipsDialog
from GNS3.Utils import translate

class TipsDialog(QtGui.QDialog, Ui_TipsDialog):
    """ TipsDialog class
    """

    def __init__(self, parent):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.webpage = QtCore.QUrl('http://www.gns3.net/')
        self.webView.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
        self.connect(self.webView, QtCore.SIGNAL('linkClicked(const QUrl &)'), self.__urlClicked)
        self.connect(self.webView, QtCore.SIGNAL('loadFinished(bool)'), self.__loadFinished)
        self.webView.load(self.webpage)

    def __urlClicked(self, url):

        if QtGui.QDesktopServices.openUrl(url) == False:
            print "Failed to open the URL: %s\n" % url.toString()

    def __loadFinished(self, result):

        self.disconnect(self.webView, QtCore.SIGNAL('loadFinished(bool)'), self.__loadFinished)
        if result == False:
            QtGui.QMessageBox.information(self, translate("TipsDialog", "Tips page"),  unicode("Couldn't load the online page, trying with your default browser ..."))
            if QtGui.QDesktopServices.openUrl(self.webpage) == False:
                print "Failed to open the URL: %s" % self.webpage.baseFrame().url().toString()
            #url = QtCore.QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath("default_tips.html"))
            #QtGui.QDesktopServices.openUrl(url)
            self.checkBoxDontShowAgain.setChecked(True)
            self.close()
