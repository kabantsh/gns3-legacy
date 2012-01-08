#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007-2011 GNS3 Development Team (http://www.gns3.net/team).
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
# code@gns3.net
#

import sys, os, traceback

# current version of GNS3
VERSION = "0.8.2-BETA"
VERSION_INTEGER = 0x000802

try:
    from PyQt4 import QtCore, QtGui
except ImportError:
    sys.stderr.write("Can't import Qt modules, PyQt is probably not installed ...\n")
    sys.exit(False)

#if QtCore.QT_VERSION < 0x0400501:
if QtCore.QT_VERSION < 0x0000001:
    raise RuntimeError, "Need Qt v4.5.1 or higher, but got v%s" % QtCore.QT_VERSION_STR

if QtCore.PYQT_VERSION < 0x040500:
#if QtCore.PYQT_VERSION < 0x040000:
    raise RuntimeError, "Need PyQt v4.5 or higher, but got v%s" % QtCore.PYQT_VERSION_STR

#if sys.version_info < (2, 6):
if sys.version_info < (2, 5):
    raise RuntimeError, "Need Python 2.5 or higher"

VBOXVER_REQUIRED = 4.1
VBOXVER_STR = ""
VBOXVER_FLOAT = 0.0
VBOXVER_REQUIRED1_MAJOR = 4
VBOXVER_REQUIRED1_MINOR = 1

try:
    from vboxapi import VirtualBoxManager
    g_VBoxmgr = VirtualBoxManager(None, None)
    VBOXVER_MAJOR = int(g_VBoxmgr.vbox.version.split('.')[0])
    VBOXVER_MINOR = int(g_VBoxmgr.vbox.version.split('.')[1])
    VBOXVER_STR = g_VBoxmgr.vbox.version
    VBOXVER_FLOAT = float(str(VBOXVER_MAJOR)+'.'+str(VBOXVER_MINOR))   
except:
    print "WARNING: vboxapi module cannot be loaded ! You can proceed, but VirtualBox functionality will not be locally available."
    g_VBoxmgr = 0
    VBOXVER_MAJOR = 0
    VBOXVER_MINOR = 0

def exceptionHook(type, value, tb):

    lines = traceback.format_exception(type, value, tb)
    print "---------Traceback lines (saved in exception.log)----------"
    print "\n" . join(lines)
    print "-----------------------------------------------------------"
    try:
    	logfile = open('exception.log','a')
    	logfile.write("\n" . join(lines))
    	logfile.close()
    except:
    	pass

# catch exceptions to write them in a file
sys.excepthook=exceptionHook

if __name__ == '__main__':
    # __file__ is not supported by py2exe and py2app
    if hasattr(sys, "frozen"):
        GNS3_RUN_PATH = os.path.dirname(os.path.abspath(sys.executable))
    else:
        GNS3_RUN_PATH = os.path.dirname(os.path.abspath(__file__))

    # change current working directory to GNS3_RUN_PATH for relative paths to work correctly
    os.chdir(GNS3_RUN_PATH)
    source_path = GNS3_RUN_PATH + os.sep + 'src'
    if os.access(source_path, os.F_OK):
        sys.path.append(source_path)

if len(sys.argv) > 1 and sys.argv[1].startswith("-psn"):
    del sys.argv[1]

import GNS3.Main