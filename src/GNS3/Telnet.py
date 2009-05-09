# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (C) 2007-2008 GNS3 Dev Team
#
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
# Contact: contact@gns3.net
#

import sys, cmd
import subprocess as sub
import GNS3.Globals as globals
from GNS3.Utils import translate, debug
from PyQt4 import QtCore, QtGui

def connect(host, port, name):
        """ Start a telnet console and connect to it
        """

        try:
            console = globals.GApp.systconf['general'].term_cmd
            if console:
                console = console.replace('%h', host)
                console = console.replace('%p', str(port))
                console = console.replace('%d', name)
                debug('Start console with: ' + console)
                if globals.GApp.systconf['general'].use_shell:
                    sub.Popen(console, shell=True)
                else:
                    sub.Popen(console)
            else:
                if sys.platform.startswith('darwin'):
                    sub.Popen("/usr/bin/osascript -e 'tell application \"Terminal\" to do script with command \"telnet " + host + " " + str(port) +"; exit\"'", shell=True)
                elif sys.platform.startswith('win'):
                    sub.Popen("start telnet " +  host + " " + str(port), shell=True)
                else:
                    sub.Popen("xterm -T " + name + " -e 'telnet " + host + " " + str(port) + "' > /dev/null 2>&1 &", shell=True)
        except (OSError, IOError), e:
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, translate("connect", "Console"), console + ': ' + e.strerror)
            return (False)
        return (True)
